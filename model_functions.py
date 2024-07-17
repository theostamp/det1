from ultralytics import YOLO
import shutil
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from PIL.ExifTags import TAGS
import cv2
import json
from datetime import datetime
import os
from matplotlib.offsetbox import AnchoredText
import sqlite3
import j

def load_occupied_since_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_occupied_since_data(filename, data):
    for table_number in data:
        if len(data[table_number]) > 2:
            data[table_number] = data[table_number][:2]
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def calculate_duration(occupied_since_list):
    if not occupied_since_list or not isinstance(occupied_since_list, list) or not occupied_since_list:
        return ""
    first_occupied_since = occupied_since_list[0]
    try:
        occupied_since_time = datetime.strptime(first_occupied_since, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return ""
    current_time = datetime.now()
    duration = current_time - occupied_since_time
    return str(duration).split('.')[0]

def create_json_data(occupied_since_data, table_centers):
    json_data = {'tables': []}
    for table_number in range(1, len(table_centers) + 1):
        occupied_since_list = occupied_since_data.get(str(table_number), [])
        occupied_since = occupied_since_list[0] if occupied_since_list else ""
        duration = calculate_duration(occupied_since_list) if occupied_since_list else ""
        center_coordinates = table_centers[table_number - 1]
        json_data['tables'].append({
            'table_number': table_number,
            'occupied_since': occupied_since,
            'duration': duration,
            'center_coordinates': center_coordinates
        })
    return json_data

def run_models(image_path, iou, conf):
    folder_path = r'.\runs'
    shutil.rmtree(folder_path, ignore_errors=True)
    image = cv2.imread(image_path)
    original_width, original_height = image.shape[1], image.shape[0]

    person_conf = conf
    person_iou = iou
    person_model = YOLO('yolov8s-pose.pt')
    results_person = person_model(image, conf=person_conf, iou=person_iou, imgsz=original_width, save=True, save_txt=True)
    keypoints_coordinates = results_person[0].keypoints.xy

    table_bboxes = []
    with open('tables.txt', 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 5:
                table_id, x1, y1, x2, y2 = parts
                x1, y1, x2, y2 = map(float, [x1, y1, x2, y2])
                table_bboxes.append((x1, y1, x2, y2))

    def is_inside(box, point):
        x1, y1, x2, y2 = box
        point_x, point_y = point
        return x1 <= point_x <= x2 and y1 <= point_y <= y2

    table_person_mapping = {i+1: {'count': 0, 'occupied': False} for i in range(len(table_bboxes))}

    if keypoints_coordinates.size(0) > 0:
        for person in keypoints_coordinates:
            for i, bbox in enumerate(table_bboxes):
                for part_index in [7, 8, 9, 10]:
                    if len(person) > part_index and is_inside(bbox, person[part_index]):
                        table_person_mapping[i+1]['count'] += 1
                        table_person_mapping[i+1]['occupied'] = True
                        break

    for table, info in table_person_mapping.items():
        print(f'Στο τραπέζι #{table} βρίσκονται {info["count"]} άτομα.')

    def convert_duration_to_minutes(duration):
        days = 0
        hours = 0
        minutes = 0
        if 'day' in duration or 'days' in duration:
            parts = duration.split(',')
            days_part = parts[0]
            time_part = parts[1].strip() if len(parts) > 1 else '0:0'
            days = int(days_part.split()[0])
            time_parts = list(map(int, time_part.split(':')))
            hours, minutes = time_parts[0], time_parts[1] if len(time_parts) >= 2 else 0
        else:
            time_parts = list(map(int, duration.split(':')))
            hours, minutes = time_parts[0], time_parts[1] if len(time_parts) >= 2 else 0
        total_minutes = (days * 24 * 60) + (hours * 60) + minutes
        return total_minutes

    table_occupation_times = {}
    table_durations = {}

    current_time = datetime.now()
    occupied_since_data = load_occupied_since_data('occupied_since.json')

    for table_number, info in table_person_mapping.items():
        table_number_str = str(table_number)
        if info['count'] > 0:
            if table_number_str not in occupied_since_data:
                occupied_since_data[table_number_str] = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            else:
                occupied_since_data[table_number_str].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        else:
            if table_number_str in occupied_since_data:
                del occupied_since_data[table_number_str]

    print("Δεδομένα προς αποθήκευση:", occupied_since_data)
    save_occupied_since_data('occupied_since.json', occupied_since_data)

    occupied_since_data = load_occupied_since_data('occupied_since.json')
    print("Φορτωμένα δεδομένα:", occupied_since_data)

    json_data = {
        'tables': [
            {
                'table_number': table_number,
                'occupied_since': occupied_since_data.get(str(table_number), [""])[0],
                'duration': calculate_duration(occupied_since_data.get(str(table_number), [""])),
                'center_coordinates': (
                    (table_bboxes[table_number-1][0] + table_bboxes[table_number-1][2]) / 2,
                    (table_bboxes[table_number-1][1] + table_bboxes[table_number-1][3]) / 2
                )
            } for table_number in range(1, len(table_bboxes) + 1)
        ]
    }

    json_data = create_json_data(occupied_since_data, table_bboxes)
    with open('shared_data/occupied_tables.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    background_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    fig, ax = plt.subplots(1, figsize=(12, 9))
    ax.imshow(background_image)

    with open('shared_data/occupied_tables.json', 'r') as json_file:
        table_data = json.load(json_file)['tables']

    for table in table_data:
        table_number = table['table_number']
        occupied_since = table['occupied_since']
        duration = table['duration']

        if occupied_since:
            bbox = table_bboxes[table_number-1]
            center_x = (bbox[0] + bbox[2]) / 2
            center_y = (bbox[1] + bbox[3]) / 2

            duration_minutes = convert_duration_to_minutes(duration)

            text_content = f"Table {table_number}\n{duration_minutes} min"
            text = ax.text(center_x, center_y, text_content, ha='center', va='center', color='white', fontsize=12)
            text.set_bbox(dict(facecolor='red', alpha=0.5, edgecolor='red'))

    plt.axis('off')
    plt.savefig(r'.\tables_visualization.jpg', bbox_inches='tight')
    plt.close(fig)
    plt.close('all')

def identify_tables(image_path, iou, conf):
    folder_path = r'.\runs'
    shutil.rmtree(folder_path, ignore_errors=True)
    keypoints = []

    image = cv2.imread(image_path)
    original_width = image.shape[1]
    original_width, original_height = image.shape[1], image.shape[0]
    img_width = original_width
    table_conf = conf
    table_iou = iou
    table_model = YOLO('yolov8m.pt')

    results_table = table_model(image, conf=table_conf, iou=table_iou, imgsz=original_width, save=True, save_txt=True, classes=[60])

    table_coordinates = results_table[1].boxes.xyxy

    def adjust_box_coordinates(box, width_increase=0.2, height_decrease=0.3):
        x1, y1, x2, y2 = box
        width = x2 - x1
        height = y2 - y1
        width_increase_pixels = width * width_increase / 2
        height_decrease_pixels = height * height_decrease
        modified_x1 = x1 - width_increase_pixels
        modified_x2 = x2 + width_increase_pixels
        modified_y1 = y1
        modified_y2 = y2 - height_decrease_pixels
        return [modified_x1, modified_y1, modified_x2, modified_y2]

    adjusted_table_coordinates = [adjust_box_coordinates(box) for box in table_coordinates]

    with open('tables.txt', 'w') as file:
        for i, box in enumerate(adjusted_table_coordinates):
            line = f'{i} {box[0]} {box[1]} {box[2]} {box[3]}\n'
            file.write(line)

    background_image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    fig, ax = plt.subplots(1, figsize=(12, 9))
    ax.imshow(background_image)
    plt.axis('off')
    for i, box in enumerate(adjusted_table_coordinates):
        rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        plt.text(box[0], box[1], f"Table {i+1}", color='white', fontsize=12)

    plt.savefig(r'.\tables_init.jpg', bbox_inches='tight')
    plt.close(fig)
    plt.close('all')
