import pkg_resources
import subprocess

def save_requirements(filename='libs.txt'):
    # Δημιουργία μιας λίστας με όλα τα εγκατεστημένα πακέτα και τις εκδόσεις τους
    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    
    # Δημιουργία ενός αρχείου με όνομα filename και αποθήκευση των πακέτων και των εκδόσεών τους
    with open(filename, 'w') as f:
        for package, version in installed_packages.items():
            f.write(f'{package}=={version}\n')
    
    print(f'Το αρχείο {filename} δημιουργήθηκε με επιτυχία.')

save_requirements()
