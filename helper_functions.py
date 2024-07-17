import os

def delete_local_received_orders_files(table_number, local_directory='received_orders'):
    try:
        for filename in os.listdir(local_directory):
            if f"table_{table_number}_" in filename:
                os.remove(os.path.join(local_directory, filename))
                print(f"Διαγράφηκε τοπικά το αρχείο: {filename}")
    except Exception as e:
        print(f"Σφάλμα κατά τη διαγραφή τοπικών αρχείων: {e}")
