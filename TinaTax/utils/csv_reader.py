import csv

def load_form():
    payloads = []
    with open("data/form_data.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            payload = {
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"],
                "service": row["service"],
                "message": row["message"],
                "expected_status": int(row["expected_status"]),
            }
            payloads.append(payload)
    return payloads
