# booking.py

import sqlite3
from PySide6.QtCore import QDate

class BookingManager:
    def __init__(self, db_path):
        self.db_path = 'booking.db'


    def get_bookings_for_date(self, date):
        """Ανακτά τις κρατήσεις για μια συγκεκριμένη ημερομηνία."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bookings WHERE date = ?", (date.toString("yyyy-MM-dd"),))
        bookings = cursor.fetchall()
        conn.close()
        return bookings

    def book_table(self, table_id, name, phone, date, hour):
        """Κάνει κράτηση για ένα τραπέζι."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO bookings (table_id, name, phone, date, hour) VALUES (?, ?, ?, ?, ?)',
                           (table_id, name, phone, date.toString("yyyy-MM-dd"), hour))
            conn.commit()
        except Exception as e:
            print(f"Σφάλμα κατά την κράτηση: {e}")
        finally:
            conn.close()
