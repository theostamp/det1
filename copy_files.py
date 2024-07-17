import shutil
import os

# Προσδιορίστε τον κεντρικό φάκελο προορισμού
central_destination_folder = 'dist/final'

# Δημιουργία του κεντρικού φακέλου αν δεν υπάρχει
if not os.path.exists(central_destination_folder):
    os.makedirs(central_destination_folder)

# Λίστα των φακέλων και αρχείων που πρέπει να αντιγραφούν
required_files_and_folders = [
    'shared_data',
    'uploaded_images',
    'old_orders',
    'icons',
    'received_orders',
    'runs',
    'tables.txt',
    'products.db',
    'camera_stream.py',
    'connect.py',
    'create_exe.py',
    'create_old_orders.py',
    'database_manager.py',
    'helper_functions.py',
    'interface_ui.py',
    'ip_camera_scan_ui.py',
    'j.py',
    'LoginWindow_ui.py',
    'model_functions.py',
    'reservations.py',
    'scan_camera_ui.py',
    'stats_ui.py',
    'tables_annotations_ui.py',
    'waiters.py',
    'waiters_ui.py',
    'z.py',
    'z_clear_cache.py',
    'z_create_pyinstaller_command.py',
    'z_list_imports.py',
    'z_remove_libs.py',
    'Z_resize_image.py',
]

# Αντιγραφή των αρχείων και φακέλων
for item in required_files_and_folders:
    source = os.path.join(os.getcwd(), item)
    destination = os.path.join(central_destination_folder, item)
    if os.path.isdir(source):
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        shutil.copy2(source, destination)

# Αντιγραφή των εκτελέσιμων αρχείων
for exe_folder in ['main', 'z', 'connect']:
    source = os.path.join('dist', exe_folder, f'{exe_folder}.exe')
    destination = os.path.join(central_destination_folder, f'{exe_folder}.exe')
    shutil.copy2(source, destination)

print("Τα αρχεία και φάκελοι αντιγράφηκαν επιτυχώς στον κεντρικό φάκελο.")
