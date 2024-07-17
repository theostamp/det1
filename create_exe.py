import os

def generate_pyinstaller_command():
    root_path = r'C:\Users\Notebook\DET'  # Θέστε το μονοπάτι του φακέλου του έργου σας
    data_folders = [f.path for f in os.scandir(root_path) if f.is_dir()]  # Λίστα με όλους τους φακέλους
    add_data_string = ' '.join(f'--add-data "{folder};{os.path.basename(folder)}"' for folder in data_folders)  # Δημιουργεί το κομμάτι της εντολής για κάθε φάκελο
    command = f"pyinstaller {add_data_string} main.py"  # Δημιουργεί την τελική εντολή
    print(command)

generate_pyinstaller_command()



# import os

# def generate_pyinstaller_command():
#     root_path = 'path_to_your_project_folder'  # Θέστε το μονοπάτι του φακέλου του έργου σας
#     py_files = []
#     for root, dirs, files in os.walk(root_path):
#         for file in files:
#             if file.endswith('.py'):
#                 full_path = os.path.join(root, file)
#                 relative_path = os.path.relpath(full_path, root_path)
#                 dest_path = os.path.dirname(relative_path)
#                 py_files.append(f'--add-data "{full_path};{dest_path}"')

#     add_data_string = ' '.join(py_files)  # Δημιουργεί το κομμάτι της εντολής για κάθε Python αρχείο
#     command = f"pyinstaller {add_data_string} your_script.py"  # Δημιουργεί την τελική εντολή
#     print(command)

# generate_pyinstaller_command()

