import re
from db_handler import load_db, save_db

def validate_reg_no(reg_no):
    """Validates VIT Reg No format (e.g., 23BCE10245 or admin_mess)."""
    pattern = r"^[0-9]{2}[a-zA-Z]{3}[0-9]{4,5}$"
    if re.match(pattern, reg_no) or reg_no == "admin_mess":
        return True
    return False

def login():
    db = load_db()
    print("\n--- LOGIN SYSTEM ---")
    user_id = input("Enter User ID / VIT Reg No: ").strip().lower()
    
    if user_id in db["users"]:
        user = db["users"][user_id]
        print(f"[✓] Welcome back, {user['name']} ({user['role'].upper()})")
        return user_id, user['role']
    else:
        if validate_reg_no(user_id):
            name = input("Enter Your Full Name: ").strip()
            print("Select Role: 1. Student | 2. Mess Manager")
            role_choice = input("Choice: ").strip()
            role = "manager" if role_choice == "2" else "student"
            
            db["users"][user_id] = {"name": name, "role": role}
            save_db(db)
            print(f"[✓] Account created successfully for {name}!")
            return user_id, role
        else:
            print("[!] Invalid VIT Registration Number format (e.g., 23BCE10045).")
            return None, None