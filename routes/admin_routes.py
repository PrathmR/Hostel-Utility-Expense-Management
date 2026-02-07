from flask import Blueprint, request, jsonify
from models.models import db, UtilityRecord
from services.calculator import calculate_bill
from services.csv_handler import process_csv
import json, csv, os

admin = Blueprint('admin', __name__)

@admin.route('/add', methods=['POST'])
def add_manual():
    data = request.json
    record = UtilityRecord(**data)
    db.session.add(record)
    db.session.commit()
    return jsonify({"message": "Record added successfully"})

@admin.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    path = os.path.join('uploads', file.filename)
    file.save(path)

    records = process_csv(path)
    for r in records:
        db.session.add(UtilityRecord(**r))
    db.session.commit()

    return jsonify({"message": "CSV uploaded successfully"})

@admin.route('/generate-report', methods=['GET'])
@admin.route('/generate-report', methods=['GET'])
def generate_report():
    data = UtilityRecord.query.all()
    report = []

    for d in data:
        bill = calculate_bill(
            float(d.electricity),
            float(d.water),
            float(d.wifi)
        )

        report.append({
            "room_no": str(d.room_no),  # ✅ force string
            "electricity_cost": float(bill["electricity_cost"]),
            "water_cost": float(bill["water_cost"]),
            "wifi_cost": float(bill["wifi_cost"]),
            "total": float(bill["total"])
        })
        

    # Save JSON
    with open('reports/report.json', 'w') as f:
        json.dump(report, f, indent=4)

    # Save CSV
    with open('reports/report.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=report[0].keys())
        writer.writeheader()
        writer.writerows(report)

    return jsonify(report)
from flask import send_file

@admin.route('/download/csv')
def download_csv():
    return send_file(
        'reports/report.csv',
        as_attachment=True,
        download_name='hostel_utility_report.csv'
    )

@admin.route('/download/json')
def download_json():
    return send_file(
        'reports/report.json',
        as_attachment=True,
        download_name='hostel_utility_report.json'
    )

