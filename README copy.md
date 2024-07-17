cd C:\Users\Notebook\DET
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt

cd C:\Users\Notebook\DET
python -m nuitka --standalone --follow-imports --enable-plugin=pyside6 --module-parameter=torch-disable-jit=no --lto=yes --clang --jobs=4 --output-dir=output `
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




cd C:\Users\Notebook\DET\output\main.dist .\main.exe

cd c:/users/notebook/DET
pyinstaller main.py --onefile

cd C:\Users\Notebook\DET
virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
pyinstaller main.py






pyinstaller main.spec
auto_py_to_exe
pyinstaller z.spec
pyinstaller connect.spec

python copy_files.py


cd C:\Users\Notebook\DET\dist\main
./main.exe

pip install pyinstaller
pyinstaller main.spec

pyinstaller --onefile main.py

pyinstaller z.spec
python main.py

pyinstaller main.spec

pyinstaller z.spec
pyinstaller z.py


