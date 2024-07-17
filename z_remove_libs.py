import os
import shutil
import subprocess

def remove_pycache(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for dir_name in dirs:
            if dir_name == "__pycache__":
                cache_path = os.path.join(root, dir_name)
                print(f"Removing {cache_path}")
                shutil.rmtree(cache_path)

def clear_pip_cache():
    try:
        result = subprocess.run(['pip', 'cache', 'purge'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while clearing pip cache: {e.stderr.decode()}")

def get_installed_packages():
    result = subprocess.run(['pip', 'freeze'], check=True, stdout=subprocess.PIPE)
    packages = result.stdout.decode().splitlines()
    package_names = [pkg.split('==')[0] for pkg in packages]
    return package_names

def uninstall_packages(packages):
    for package in packages:
        try:
            subprocess.run(['pip', 'uninstall', '-y', package], check=True)
            print(f"Successfully uninstalled {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while uninstalling {package}: {e.stderr.decode()}")

def update_requirements_hashes():
    try:
        result = subprocess.run(['pip-compile', '--generate-hashes', '-o', 'requirements.txt', 'requirements.in'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while updating requirements hashes: {e.stderr.decode()}")

# Δώστε τη διαδρομή προς τον κατάλογο του έργου σας
project_dir = r"C:\Users\Notebook\DET"

# Καθαρισμός __pycache__ φακέλων
remove_pycache(project_dir)

# Καθαρισμός pip cache
clear_pip_cache()

# Ενημέρωση του requirements file με σωστά hashes
update_requirements_hashes()

# Απεγκατάσταση όλων των εγκατεστημένων πακέτων
installed_packages = get_installed_packages()
uninstall_packages(installed_packages)
