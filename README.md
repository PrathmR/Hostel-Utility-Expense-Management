# 🏠 Hostel Utility Expense Management System

A Flask-based web application designed to automate the tracking, calculation, and reporting of hostel utility expenses including electricity, water, and Wi-Fi. The system minimizes manual accounting errors by supporting both manual data entry and bulk CSV uploads, and by generating downloadable billing reports.

---

<img width="1083" height="515" alt="image" src="https://github.com/user-attachments/assets/a66cab88-221a-4221-8371-74034403c2ff" />


## 🚀 Features

* Manual monthly utility entry per room
* Bulk CSV upload for meter readings
* Automated tariff-based bill calculation
* Validation for invalid or negative readings
* Downloadable reports in CSV and JSON formats
* Clean and responsive admin dashboard (Bootstrap 5)
* Modular and scalable Flask architecture

---

## 🧩 Tech Stack

* Backend: Flask (Python)
* Database: SQLite with SQLAlchemy ORM
* Frontend: HTML, Bootstrap 5, JavaScript
* Data Processing: Pandas
* Report Generation: JSON and CSV

---

## 📁 Project Structure

```
hostel_utility_manager/
│
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── instance/
│   └── utility.db
│
├── models/
│   └── models.py
│
├── routes/
│   └── admin_routes.py
│
├── services/
│   ├── calculator.py
│   ├── csv_handler.py
│   └── validator.py
│
├── templates/
│   └── index.html
│
├── static/
├── uploads/
├── reports/
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/PrathmR/Hostel-Utility-Expense-Management
cd Hostel-Utility-Expense-Management
```

### 2. (Optional) Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the Application

```
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📊 CSV Dataset Format

Upload UTF-8 encoded CSV files in the following format:

```
room_no,electricity,water,wifi
101,120,50,1
102,135,45,1
103,98,40,1
104,160,60,1
105,110,48,1
```

---

## ⬇️ Reports & Downloads

* View JSON Report: `/admin/generate-report`
* Download CSV Report: `/admin/download/csv`
* Download JSON Report: `/admin/download/json`

---

## 🎯 Use Case

This system is intended for hostel administrators to automate monthly utility billing, reduce calculation errors, manage room-wise expenses efficiently, and export reports for accounting or auditing purposes.

---

## 🧠 Future Enhancements

* Admin authentication and role management
* PDF bill generation per room
* Monthly and yearly usage analytics
* Student portal for bill viewing
* Cloud deployment (AWS / Render)

---

## 📜 License

This project is open-source and intended for educational, academic, and hackathon use.
