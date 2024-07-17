# z.spec
block_cipher = None

a = Analysis(
    ['z.py'],
    pathex=['C:\\Users\\Notebook\\DET'],
    binaries=[],
     datas=[
        ('shared_data/occupied_tables.json', 'shared_data'),
        ('tables.txt', '.'),
        ('products.db', '.'),
        ('uploaded_images', 'uploaded_images'),
        ('old_orders', 'old_orders'),
        ('icons', 'icons'),
        ('received_orders', 'received_orders'),
        ('runs', 'runs'),
        # Προσθέστε όλα τα απαραίτητα αρχεία .py
        ('camera_stream.py', '.'),
        ('connect.py', '.'),
        ('create_exe.py', '.'),
        ('create_old_orders.py', '.'),
        ('database_manager.py', '.'),
        ('helper_functions.py', '.'),
        ('interface_ui.py', '.'),
        ('ip_camera_scan_ui.py', '.'),
        ('j.py', '.'),
        ('LoginWindow_ui.py', '.'),
        ('model_functions.py', '.'),
        ('reservations.py', '.'),
        ('scan_camera_ui.py', '.'),
        ('stats_ui.py', '.'),
        ('tables_annotations_ui.py', '.'),
        ('waiters.py', '.'),
        ('waiters_ui.py', '.'),
        ('z.py', '.'),
        ('z_clear_cache.py', '.'),
        ('z_create_pyinstaller_command.py', '.'),
        ('z_list_imports.py', '.'),
        ('z_remove_libs.py', '.'),
        ('Z_resize_image.py', '.'),
        ('yolov8s-pose.pt', '.'),

        # Προσθέστε εδώ όλα τα άλλα αρχεία που χρειάζονται
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='z',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='z',
    dest='dist/z',  # Καθορισμός του φακέλου εξόδου
)
