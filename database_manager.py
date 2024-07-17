import sqlite3

def initialize_db():
    try:
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    description TEXT,
                    price REAL,
                    amount INTEGER
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την αρχικοποίηση του πίνακα products: {e}")


def initialize_db_tables_occupation():
    try:
        with sqlite3.connect('tables_occupation.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tables (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    table_id INTEGER,
                    occupied_since TEXT,
                    duration TEXT,
                    center_coordinates TEXT,
                    record_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την αρχικοποίηση του πίνακα tables: {e}")
        

def add_record(category, description, price, amount):
    try:
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO products (category, description, price, amount) VALUES (?, ?, ?, ?)',
                           (category, description, price, amount))
            conn.commit()
            print("Εισαγωγή επιτυχής")
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την εισαγωγή: {e}")

def search_database(field, text):
    try:
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            if field not in ['category', 'description', 'price', 'amount']:
                raise ValueError("Invalid field name")
            query = f"SELECT * FROM products WHERE {field} LIKE ?"
            cursor.execute(query, ('%' + text + '%',))
            results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την αναζήτηση στη βάση δεδομένων: {e}")
        return []

def delete_record(record_id):
    try:
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM products WHERE id = ?', (record_id,))
            conn.commit()
            print("Διαγραφή επιτυχής")
    except sqlite3.Error as e:
        print("Σφάλμα κατά τη διαγραφή:", e)
