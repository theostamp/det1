import json
import os
import requests
import time
import sys
import logging

# Ρύθμιση του logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Λάβετε το username ως όρισμα από τη γραμμή εντολών
username = sys.argv[1] if len(sys.argv) > 1 else 'default_username'

def is_valid_json(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return True
    except json.JSONDecodeError:
        return False

def adjust_json_format(data, json_path):
    """
    Προσαρμόζει τα δεδομένα JSON στη μορφή που απαιτεί ο server.
    """
    if "occupied_tables.json" in json_path:
        return {"tables": data}
    elif "products.json" in json_path:
        return {"products": data}
    elif "reservations.json" in json_path:
        return {"reservations": data}
    return data

def upload_json_data(json_path, username):
    tenant_specific_url = f'http://{username}.localhost:8003/upload_json/{username}/'
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        adjusted_data = adjust_json_format(data, json_path)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(tenant_specific_url, json=adjusted_data, headers=headers)
        # print(f"Uploading file: {json_path} to {tenant_specific_url} with data: {adjusted_data}")
        print(f"Uploading file: {json_path} to {tenant_specific_url} ")
        if response.status_code == 200:
            print(f"Αποστολή δεδομένων επιτυχής: {response.text}")
        else:
            print(f"Σφάλμα κατά την αποστολή δεδομένων στο {tenant_specific_url}: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Σφάλμα κατά την αποστολή του αρχείου {json_path} στο {tenant_specific_url}: {e}")

def download_json_data(username):
    tenant_specific_url = f'http://{username}.localhost:8003/list_order_files/{username}/'
    try:
        response = requests.get(tenant_specific_url)
        if response.status_code == 200:
            files = response.json().get('files', [])
            for file_name in files:
                file_response = requests.get(f'http://{username}.localhost:8003/get_order/{username}/{file_name}/')
                if file_response.status_code == 200:
                    file_path = os.path.join('received_orders', file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    with open(file_path, 'wb') as file:
                        file.write(file_response.content)
                    logger.info(f"Αρχείο {file_name} λήφθηκε επιτυχώς.")
                else:
                    logger.error(f"Αποτυχία λήψης του αρχείου {file_name} με κωδικό: {file_response.status_code}")
        else:
            logger.error("Δεν ήταν δυνατή η λήψη της λίστας αρχείων.")
    except Exception as e:
        logger.error(f"Σφάλμα κατά τη λήψη αρχείων από {tenant_specific_url}: {e}")

json_paths = ['shared_data/occupied_tables.json', 'shared_data/products.json', 'shared_data/reservations.json']

logger.info(f"Current working directory: {os.getcwd()}")

while True:
    for json_path in json_paths:
        logger.info(f"Επεξεργασία του αρχείου: {json_path}")
        if is_valid_json(json_path):
            upload_json_data(json_path, username)
        else:
            logger.error(f"Το αρχείο {json_path} δεν είναι έγκυρο JSON.")
        download_json_data(username)
        logger.info("Running operations...")
        time.sleep(15)  # Ρύθμιση της περιόδου επανάληψης σε δευτερόλεπτα

logger.info("Stopping connect.py")
