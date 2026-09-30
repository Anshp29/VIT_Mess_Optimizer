# 🍲 VIT Mess Wastage & Budget Optimizer

A modular Python CLI application developed for automated mess food wastage tracking, monetary loss calculation, and predictive cooking target optimization in university messes.

---

## 🎓 Academic Context

- **Institution:** VIT Bhopal University
- **Course:** Python Essentials
- **Project Goal:** Python Essentials - Evaluated Course Project
- **Repository:** [https://github.com/Anshp29/VIT_Mess_Optimizer](https://github.com/Anshp29/VIT_Mess_Optimizer)

---

## 📌 Key Features

- **Role-Based Access:** Manager portal for wastage logging & analytics; Student portal for RSVP meal skips.
- **Wastage & Loss Tracking:** Monitors meal-wise food cooked vs. wasted (in kg) and computes monetary loss in INR.
- **Predictive Optimizer:** Uses a 3-day moving average combined with real-time student RSVPs to recommend future preparation quantities.
- **Regex Validation:** Enforces strict VIT Registration Number format validation (e.g., `23BCE10245`).
- **Persistent Storage:** Auto-generates and manages persistent records in local JSON (`vit_mess_records.json`).

---

## 🛠️ Project Structure

```text
VIT_Mess_Optimizer/
│
├── main.py               # Application CLI navigation & main menu execution
├── auth_system.py        # Authentication logic & Regex validation engine
├── analytics_engine.py   # Loss calculation algorithms & predictive model
├── db_handler.py          # JSON file I/O handling & sample data generation
├── config.py              # Application settings, pricing, and system constants
└── vit_mess_records.json # Local persistent database storage

💻 Tech Stack
~Language: Python 3.8+

~Paradigm: Object-Oriented Programming (OOP) & Modular Architecture

~Dependencies: Standard Python Libraries (json, os, re, datetime) — Zero external pip dependencies.

⚙️ How to Run
1. Clone the repository:
git clone [https://github.com/Anshp29/VIT_Mess_Optimizer.git](https://github.com/Anshp29/VIT_Mess_Optimizer.git)
cd VIT_Mess_Optimizer
2. Run the program:
python main.py

🔑 Demo Credentials
👨‍💼 1. Mess Manager Portal
Role: Administrator (Full Access)

Username: admin_mess

Password: admin123

Capabilities: Log daily meal wastage, view financial loss analytics, and execute predictive budget optimization.

🎓 2. Student Portal (Existing Record)
Role: Registered Student

Registration Number: 23bce10001

Password: Not Required

Capabilities: Submit meal-cancellation RSVPs and view upcoming mess menus.

🆕 3. Student Portal (New Registration)
Role: Dynamic Registration

Registration Number: Any valid VIT Reg No (e.g., 23BCE10245, 24BIT10050)

Password: Not Required

Capabilities: Automatically validated via built-in Regex pattern (^[0-9]{2}[A-Z]{3}[0-9]{4,5}$).

