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
