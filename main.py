import config
from db_handler import load_db, save_db
from auth_system import login
from analytics_engine import view_wastage_summary, optimize_tomorrow_budget
from datetime import datetime

def log_new_entry():
    db = load_db()
    print("\n--- LOG DAILY MESS WASTAGE ---")
    date_str = input("Enter Date (YYYY-MM-DD) [Leave blank for Today]: ").strip()
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")

    print("\nSelect Mess:")
    for idx, m in enumerate(config.MESS_LOCATIONS, 1):
        print(f"{idx}. {m}")
    mess = config.MESS_LOCATIONS[int(input("Choice: ")) - 1]

    print("\nSelect Meal: 1. Breakfast | 2. Lunch | 3. Snacks | 4. Dinner")
    meal = config.MEAL_TYPES[int(input("Choice: ")) - 1]

    try:
        prep = float(input("Quantity Prepared (kg): "))
        wasted = float(input("Quantity Wasted (kg): "))
        cost = float(input(f"Cost per kg in INR [Default {config.DEFAULT_COST_PER_KG[meal]}]: ") or config.DEFAULT_COST_PER_KG[meal])

        if wasted > prep:
            print("\n[!] Error: Wasted quantity cannot exceed prepared quantity!")
            return

        db["records"].append({
            "date": date_str,
            "mess": mess,
            "meal": meal,
            "prepared_kg": prep,
            "wasted_kg": wasted,
            "cost_per_kg": cost,
            "financial_loss": wasted * cost
        })
        save_db(db)
        print("\n[✓] Wastage Record successfully logged!")
    except ValueError:
        print("[!] Invalid numerical input.")

def student_rsvp(user_id):
    db = load_db()
    print("\n--- STUDENT MEAL RSVP (FOOD WASTE PREVENTION) ---")
    print("Select Meal for Tomorrow:")
    for idx, m in enumerate(config.MEAL_TYPES, 1):
        print(f"{idx}. {m}")
    meal = config.MEAL_TYPES[int(input("Choice: ")) - 1]

    status_choice = input("Will you eat this meal? (1. Attending / 2. Skipping): ").strip()
    status = "Attending" if status_choice == "1" else "Skipping"

    db["rsvps"].append({
        "student": user_id,
        "meal": meal,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_db(db)
    print(f"\n[✓] RSVP recorded ({status} for {meal}). Thank you for helping reduce mess waste!")

def main():
    print("\n" + "="*50)
    print("   VIT BHOPAL - SMART MESS WASTAGE OPTIMIZER   ")
    print("="*50)
    
    user_id, role = login()
    if not user_id:
        return

    while True:
        if role == "manager":
            print("\n--- MESS MANAGER MENU ---")
            print("1. Log Daily Food Wastage")
            print("2. View Wastage & Financial Analytics")
            print("3. Run Budget Optimizer Engine")
            print("4. Switch User / Exit")
            ch = input("Enter choice (1-4): ").strip()

            if ch == "1":
                log_new_entry()
            elif ch == "2":
                view_wastage_summary()
            elif ch == "3":
                optimize_tomorrow_budget()
            elif ch == "4":
                print("Exiting application...")
                break
        else:
            print("\n--- STUDENT MENU ---")
            print("1. Submit Meal Attendance / Skip RSVP")
            print("2. View Mess Wastage Statistics")
            print("3. Exit")
            ch = input("Enter choice (1-3): ").strip()

            if ch == "1":
                student_rsvp(user_id)
            elif ch == "2":
                view_wastage_summary()
            elif ch == "3":
                print("Exiting application...")
                break

if __name__ == "__main__":
    main()