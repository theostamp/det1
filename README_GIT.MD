# Αρχικοποίηση του Git repository
git init

# Προσθήκη του αρχείου .md στο staging area
git add .
# Δημιουργία του πρώτου commit
git commit -m "first commit"
# Δημιουργία του branch με όνομα 'main'
git branch main
# Μετακίνηση στο branch 'main'
git checkout main
# Προσθήκη του απομακρυσμένου αποθετηρίου
git remote add origin https://github.com/theostamp/det1.git
# Αποστολή του branch 'main' στο απομακρυσμένο αποθετήριο
git push -u origin main



python -m nuitka --standalone --enable-plugin=pyside6 `
--module-parameter=torch-disable-jit=no --jobs=16 --output-dir=output `
--nofollow-import-to=IPython `
--include-data-files=shared_data/occupied_tables.json=shared_data/occupied_tables.json `
--include-data-files=icons/*=icons/ `
--include-data-files=tables.txt=tables.txt `
--include-data-files=camera_models.db=camera_models.db `
--include-data-files=example.db=example.db `
--include-data-files=products.db=products.db `
--include-data-files=reserve.db=reserve.db `
--include-data-files=waiters.db=waiters.db `
--include-data-files=tables_occupation.db=tables_occupation.db `
main.py
