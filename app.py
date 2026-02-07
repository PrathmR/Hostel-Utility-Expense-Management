from flask import Flask, render_template
from config import Config
from models.models import db
from routes.admin_routes import admin
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(admin, url_prefix='/admin')

@app.route('/')
def home():
    return render_template("index.html")   # 🔥 THIS LINE FIXES IT

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    app.run(debug=True)
