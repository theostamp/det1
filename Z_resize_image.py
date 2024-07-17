from PIL import Image
import os

# Ορίστε τους φακέλους
source_folder = 'uploaded_images_source'
target_folder = 'uploaded_images'

# Δημιουργήστε τον φάκελο προορισμού αν δεν υπάρχει
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# Σημείο στόχου πλάτους
target_width = 640

# Λειτουργία για αλλαγή μεγέθους και αποθήκευση εικόνων
def resize_images(source_folder, target_folder, target_width):
    for filename in os.listdir(source_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(source_folder, filename)
            img = Image.open(img_path)
            width_percent = (target_width / float(img.size[0]))
            target_height = int((float(img.size[1]) * float(width_percent)))
            resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
            resized_img_path = os.path.join(target_folder, filename)
            resized_img.save(resized_img_path)
            print(f"Η εικόνα {filename} αποθηκεύτηκε στο {resized_img_path}")

# Εκτελέστε την λειτουργία αλλαγής μεγέθους
resize_images(source_folder, target_folder, target_width)
