import json
import sqlite3
import datetime
import os

def calculate_time_difference(timestamp):
    now = datetime.datetime.now()
    difference = now - timestamp
    return str(difference).split('.')[0]


def initialize_order_db():
    try:
        with sqlite3.connect('example.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER UNIQUE,
                    table_number INTEGER,
                    product_description TEXT,
                    quantity INTEGER,
                    total_cost REAL,
                    time_diff TEXT,
                    waiter TEXT,
                    order_done BOOLEAN,
                    printed BOOLEAN,
                    timestamp TEXT
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την αρχικοποίηση της βάσης δεδομένων: {e}")

initialize_order_db()

def process_json_file(file_path):
    # print(f"Επεξεργασία αρχείου: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    timestamp_str = data['timestamp']
    try:
        timestamp = datetime.datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        print(f"Σφάλμα μορφοποίησης χρονοσήμανσης: {timestamp_str} - {e}")
        return

    time_diff = calculate_time_difference(timestamp)
    # print(f"Χρονική διαφορά: {time_diff}")
    
    table_number = data.get('table_number')
    product_description = data.get('product_description')
    quantity = data.get('quantity')
    total_cost = data.get('total_cost')
    waiter = data.get('waiter', 'Unknown')
    order_done = data.get('order_done', False)
    printed = data.get('printed', False)
    order_id = data.get('order_id')

    # print(f"Εισαγωγή παραγγελίας: Τραπέζι {table_number}, Περιγραφή: {product_description}, Ποσότητα: {quantity}, Κόστος: {total_cost}")
    insert_or_update_order(order_id, table_number, product_description, quantity, total_cost, time_diff, waiter, order_done, printed, timestamp)

def insert_or_update_order(order_id, table_number, product_description, quantity, total_cost, time_diff, waiter, order_done, printed, timestamp):
    with sqlite3.connect('example.db') as conn:
        cursor = conn.cursor()
        # Έλεγχος αν υπάρχει ήδη το order_id
        cursor.execute("SELECT id FROM orders WHERE order_id = ?", (order_id,))
        result = cursor.fetchone()
        
        if result:
            # Ενημέρωση υπάρχουσας εγγραφής
            try:
                cursor.execute('''
                    UPDATE orders SET 
                    table_number = ?, 
                    product_description = ?, 
                    quantity = ?, 
                    total_cost = ?, 
                    time_diff = ?, 
                    waiter = ?, 
                    order_done = ?, 
                    printed = ?, 
                    timestamp = ? 
                    WHERE order_id = ?
                ''', (table_number, product_description, quantity, total_cost, time_diff, waiter, order_done, printed, timestamp, order_id))
                conn.commit()
                # print("Επιτυχής ενημέρωση στη βάση δεδομένων.")
            except sqlite3.Error as e:
                print(f"Σφάλμα κατά την ενημέρωση στη βάση δεδομένων: {e}")
        else:
            # Εισαγωγή νέας εγγραφής
            try:
                cursor.execute('''
                    INSERT INTO orders (order_id, table_number, product_description, quantity, total_cost, time_diff, waiter, order_done, printed, timestamp) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (order_id, table_number, product_description, quantity, total_cost, time_diff, waiter, order_done, printed, timestamp))
                conn.commit()
                print("Επιτυχής εισαγωγή στη βάση δεδομένων.")
            except sqlite3.Error as e:
                print(f"Σφάλμα κατά την εισαγωγή στη βάση δεδομένων: {e}")


def process_all_json_files(directory):
    # Έλεγχος εάν ο φάκελος υπάρχει, αν όχι δημιουργήστε τον
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' was not found and has been created.")
    
    # Επεξεργασία όλων των JSON αρχείων στον φάκελο
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            process_json_file(os.path.join(directory, filename))

if __name__ == "__main__":
    process_all_json_files('received_orders')
