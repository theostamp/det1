import os
import shutil
import fnmatch

def get_new_folder_name(base_folder_path):
    counter = 1
    new_folder_path = f"{base_folder_path}_{counter}"

    while os.path.exists(new_folder_path):
        counter += 1
        new_folder_path = f"{base_folder_path}_{counter}"

    return new_folder_path

def should_exclude(file_name, exclusion_patterns):
    for pattern in exclusion_patterns:
        if fnmatch.fnmatch(file_name, pattern):
            return True
    return False

def should_exclude_folder(folder_path, excluded_folders):
    folder_path_normalized = os.path.normpath(folder_path)
    for pattern in excluded_folders:
        if fnmatch.fnmatch(folder_path_normalized, os.path.normpath(pattern)):
            return True
    return False

def copy_folders_with_incremental_names(source_base_folder, target_base_folder, folder_names, exclusion_patterns, excluded_folders, alternative_target=None):
    if not os.path.exists(source_base_folder):
        print(f"Ο κατάλογος πηγής {source_base_folder} δεν υπάρχει.")
        return

    if not os.path.exists(target_base_folder):
        print(f"Ο κατάλογος προορισμού {target_base_folder} δεν υπάρχει.")
        return

    for folder_name in folder_names:
        source_folder = os.path.join(source_base_folder, folder_name)
        if not os.path.exists(source_folder):
            print(f"Ο κατάλογος πηγής {source_folder} δεν υπάρχει.")
            continue

        if should_exclude_folder(source_folder, excluded_folders):
            print(f"Εξαιρέθηκε ο φάκελος: {source_folder}")
            continue

        # Αντιγραφή στον κύριο προορισμό (target_base_folder)
        target_folder = get_new_folder_name(os.path.join(target_base_folder, folder_name))
        os.makedirs(target_folder)
        copy_folder_contents(source_folder, target_folder, exclusion_patterns, excluded_folders)

        # Αντιγραφή στον εναλλακτικό προορισμό (alternative_target)
        if alternative_target:
            alternative_folder = get_new_folder_name(os.path.join(alternative_target, folder_name))
            os.makedirs(alternative_folder)
            copy_folder_contents(source_folder, alternative_folder, exclusion_patterns, excluded_folders)
            
        print(f"Ολοκληρώθηκε η αντιγραφή του φακέλου: {folder_name}")

# Νέα συνάρτηση για την αντιγραφή των περιεχομένων ενός φακέλου
def copy_folder_contents(source_folder, target_folder, exclusion_patterns, excluded_folders):
    for root, dirs, files in os.walk(source_folder):
        rel_root = os.path.relpath(root, source_folder)
        
        # Αφαιρέστε τους εξαιρεθέντες φακέλους από τη λίστα dirs
        dirs[:] = [d for d in dirs if not should_exclude_folder(os.path.join(root, d), excluded_folders)]

        for file in files:
            file_path = os.path.join(root, file)
            if should_exclude(file_path, exclusion_patterns):
                continue

            relative_path = os.path.relpath(file_path, source_folder)
            target_file = os.path.join(target_folder, relative_path)

            target_file_directory = os.path.dirname(target_file)
            if not os.path.exists(target_file_directory):
                os.makedirs(target_file_directory)

            shutil.copy2(file_path, target_file)
            print(f"Αντιγράφηκε: {file_path} σε {target_file}")



# Παράδειγμα χρήσης
source_base_directory = 'C:/Users/Notebook'
target_base_directory = 'E:/backup_project'
alternative_target_directory = 'D:/backup_project'  
folders_to_copy = ['DET', 'django']
exclusion_patterns = ['*.tmp', '*.log', '*.pt','.env','*.env']
excluded_folders = [
    'DET/myenv',
    'C:/Users/Notebook/DET/venv',
    'C:/Users/Notebook/DET/output',
    'DET/build/', 
    'DET/dist', 
    '**/.venv', 
    '**/.env', 
    '**/.git', 
    '**/__pycache__', 
    '**/staticfiles'
]

copy_folders_with_incremental_names(
    source_base_directory, 
    target_base_directory, 
    folders_to_copy, 
    exclusion_patterns, 
    excluded_folders, 
    alternative_target=alternative_target_directory
)
