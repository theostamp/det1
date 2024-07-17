import os
import re
import sqlite3
import requests
import json
def initialize_old_orders_db():
    try:
        with sqlite3.connect('example.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS old_orders (
                    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id            INTEGER UNIQUE,
                    table_number        INTEGER,
                    product_description TEXT,
                    quantity            INTEGER,
                    total_cost          REAL,
                    time_diff           TEXT,
                    waiter              TEXT,
                    order_done          BOOLEAN,
                    printed             BOOLEAN,
                    timestamp           TEXT
                );
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την αρχικοποίηση της βάσης δεδομένων: {e}")

initialize_old_orders_db()



def delete_files_from_server(file_list):
    success = True
    for filename in file_list:
        url = f"http://localhost:8080/delete_order_file/{filename}"
        try:
            response = requests.delete(url)
            if response.status_code != 200:
                print(f"Αποτυχία διαγραφής του αρχείου {filename} από τον server. Κωδικός σφάλματος: {response.status_code}")
                success = False
        except requests.RequestException as e:
            print(f"Σφάλμα κατά την αποστολή αιτήματος διαγραφής: {e}")
            success = False
    return success

def update_database_and_delete_local_files(received_orders_dir="received_orders"):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id FROM orders 
        WHERE order_done = 1 AND printed = 0
    ''')
    orders_to_update = cursor.fetchall()

    pattern = re.compile(r"order_table_(\d+)_\d+.json")
    for filename in os.listdir(received_orders_dir):
        match = pattern.match(filename)
        if match and int(match.group(1)) in [order[0] for order in orders_to_update]:
            if delete_files_from_server([filename]):
                cursor.execute('''
                    UPDATE orders 
                    SET printed = 1 
                    WHERE id = ?
                ''', (int(match.group(1)),))

                file_path = os.path.join(received_orders_dir, filename)
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Το αρχείο {filename} διαγράφηκε επιτυχώς από τον τοπικό κατάλογο.")

    conn.commit()
    conn.close()

def copy_order_to_old_orders_and_update(table_number):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            SELECT COUNT(*) FROM orders 
            WHERE table_number = ? AND order_done = 1 AND printed = 0
        ''', (table_number,))
        count = cursor.fetchone()[0]
        
        if count > 0:
            cursor.execute('''
                INSERT INTO old_orders (
                    order_id, 
                    table_number, 
                    product_description, 
                    quantity, 
                    total_cost, 
                    time_diff, 
                    waiter, 
                    order_done, 
                    printed, 
                    timestamp,
                    served_time
                )
                SELECT 
                    order_id, 
                    table_number, 
                    product_description, 
                    quantity, 
                    total_cost, 
                    time_diff, 
                    waiter, 
                    order_done, 
                    printed, 
                    timestamp,
                    served_time
                FROM orders 
                WHERE table_number = ? AND order_done = 1 AND printed = 0
            ''', (table_number,))
            cursor.execute('''
                UPDATE orders 
                SET printed = 1 
                WHERE table_number = ? AND order_done = 1 AND printed = 0
            ''', (table_number,))
            conn.commit()

            cursor.execute('''
                DELETE FROM orders 
                WHERE table_number = ? AND order_done = 1 AND printed = 1
            ''', (table_number,))
        else:
            print("Δεν υπάρχουν εγγραφές προς αντιγραφή για το τραπέζι:", table_number)
    except sqlite3.Error as e:
        print("Σφάλμα κατά την εκτέλεση των ενεργειών στη βάση δεδομένων:", e)
    finally:
        conn.close()
        print("Κλείσιμο της σύνδεσης με τη βάση δεδομένων.")
        update_database_and_delete_local_files()

# Παράδειγμα κλήσης της συνάρτησης
copy_order_to_old_orders_and_update(table_number=1)