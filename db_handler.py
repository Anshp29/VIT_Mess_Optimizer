import json
import os
from datetime import datetime, timedelta
import config

DB_FILE = "vit_mess_records.json"

def init_db():
    """Initializes JSON database and generates 7-day initial data if missing."""
    if not os.path.exists(DB_FILE):
        sample_data = {
            "users": {
                "23bce10001": {"name": "Aman Sharma", "role": "student"},
                "admin_mess": {"name": "Mess Supervisor", "role": "manager"}
            },
            "records": _generate_sample_logs(),
            "rsvps": []
        }
        save_db(sample_data)

def load_db():
    init_db()
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def _generate_sample_logs():
    """Generates realistic past 7 days logs for instant live demonstration."""
    logs = []
    base_date = datetime.now() - timedelta(days=7)
    
    sample_prep = {"Breakfast": 250, "Lunch": 400, "Snacks": 180, "Dinner": 380}
    sample_waste = {"Breakfast": 25, "Lunch": 68, "Snacks": 15, "Dinner": 52}

    for i in range(7):
        date_str = (base_date + timedelta(days=i)).strftime("%Y-%m-%d")
        for meal in config.MEAL_TYPES:
            prep = sample_prep[meal]
            waste = sample_waste[meal]
            cost = config.DEFAULT_COST_PER_KG[meal]
            logs.append({
                "date": date_str,
                "mess": "Block-1 Boys Mess",
                "meal": meal,
                "prepared_kg": prep,
                "wasted_kg": waste,
                "cost_per_kg": cost,
                "financial_loss": waste * cost
            })
    return logs