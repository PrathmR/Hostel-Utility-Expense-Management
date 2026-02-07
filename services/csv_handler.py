import pandas as pd
from services.validator import validate_usage

def process_csv(path):
    df = pd.read_csv(path)
    records = []

    for _, row in df.iterrows():
        if not all(validate_usage(row[col]) for col in ['electricity', 'water', 'wifi']):
            raise ValueError("Invalid data detected in CSV")

        records.append({
            "room_no": row['room_no'],
            "electricity": float(row['electricity']),
            "water": float(row['water']),
            "wifi": float(row['wifi'])
        })
    return records
