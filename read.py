import matplotlib.pyplot as plt
import numpy as np
import math

def rotate_point(x, y, angle, origin):
    angle_rad = math.radians(angle)
    ox, oy = origin
    px, py = x, y

    qx = ox + math.cos(angle_rad) * (px - ox) - math.sin(angle_rad) * (py - oy)
    qy = oy + math.sin(angle_rad) * (px - ox) + math.cos(angle_rad) * (py - oy)
    return qx, qy

def calculate_center(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

# Εδώ φορτώνουμε τα δεδομένα από το αρχείο tables.txt
# Στον κώδικα σας αυτό θα πρέπει να είναι το πλήρες μονοπάτι του αρχείου
tables_data = []
with open("tables.txt", "r") as file:
    tables_data = file.readlines()

y1_values = [float(box.strip().split()[2]) for box in tables_data]
closest_to_x_axis_index = y1_values.index(min(y1_values))
closest_box = tables_data[closest_to_x_axis_index].strip().split()
_, x1, y1, x2, y2 = map(float, closest_box)
new_origin = calculate_center(x1, y1, x2, y2)

new_centers = []
for line in tables_data:
    _, x1, y1, x2, y2 = map(float, line.strip().split())
    new_centers.append(calculate_center(x1, y1, x2, y2))

fig, ax = plt.subplots(figsize=(12, 8))
step =400
angle =-10

all_x = [c[0] for c in new_centers]
all_y = [c[1] for c in new_centers]
min_x, max_x, min_y, max_y = min(all_x), max(all_x), min(all_y), max(all_y)
width = max_x - min_x
height = max_y - min_y

x_range = np.arange(min_x - width, max_x + width, step)
y_range = np.arange(min_y - height, max_y + height, step)

for x in x_range:
    ax.plot(*zip(*[rotate_point(x, y, angle, new_origin) for y in y_range]), color='grey', linestyle='--', linewidth=0.5)

for y in y_range:
    ax.plot(*zip(*[rotate_point(x, y, angle, new_origin) for x in x_range]), color='grey', linestyle='--', linewidth=0.5)

ax.plot(*zip(*[rotate_point(min_x - width, 0, angle, new_origin), rotate_point(max_x + width, 0, angle, new_origin)]), 
        color='black', linestyle='-', linewidth=2)
ax.plot(*zip(*[rotate_point(0, min_y - height, angle, new_origin), rotate_point(0, max_y + height, angle, new_origin)]), 
        color='black', linestyle='-', linewidth=2)

for i, (cx, cy) in enumerate(new_centers):
    # Πολλαπλασιάστε το x με -1 για την αντιστροφή
    rx, ry = rotate_point(cx , cy , angle, new_origin)
    ax.scatter(rx, ry, color='blue', s=100)
    ax.text(rx, ry, f'{i}', color='red', fontsize=15, ha='right', va='bottom')

ax.set_xlim(min_x - 5*width, max_x +5*width)
ax.set_ylim(min_y - 5*height, max_y + 5*height)

ax.axis('off')

plt.show()
