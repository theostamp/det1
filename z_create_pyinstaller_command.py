import os
import logging
import glob

def setup_logger():
    logger = logging.getLogger('PyInstallerBuilder')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def create_pyinstaller_command(folder_path):
    logger = setup_logger()
    command = "pyinstaller --noconfirm --clean --exclude-module PyQt5"
    folder_path = os.path.abspath(folder_path)  # Πλήρες μονοπάτι του φακέλου
    
    # Προσθήκη όλων των αρχείων στον φάκελο
    files = glob.glob(os.path.join(folder_path, '*'))  # Προσθέτει όλα τα αρχεία στον φάκελο
    for src_file in files:
        if os.path.isfile(src_file):  # Ελέγχει αν το στοιχείο είναι αρχείο
            dest_path = './data'
            data_string = f'"{src_file};{dest_path}"'
            command += f' --add-data {data_string}'
            logger.debug(f'Added file to bundle: {data_string}')

    command += " main.py"
    logger.info(f'Final PyInstaller command: {command}')
    return command

# Παράδειγμα χρήσης:
folder_path = r'C:\Users\Notebook\DET'
command = create_pyinstaller_command(folder_path)
print("Run this command:\n", command)
