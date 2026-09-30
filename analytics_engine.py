from db_handler import load_db, save_db
import config

def view_wastage_summary():
    db = load_db()
    records = db["records"]
    
    if not records:
        print("[!] No records available.")
        return

    total_prep = sum(r["prepared_kg"] for r in records)
    total_waste = sum(r["wasted_kg"] for r in records)
    total_loss = sum(r["financial_loss"] for r in records)
    waste_pct = (total_waste / total_prep) * 100 if total_prep > 0 else 0

    print("\n" + "="*68)
    print("         VIT BHOPAL MESS WASTAGE & LOSS ANALYTICS REPORT        ")
    print("="*68)
    print(f"{'Date':<12} | {'Meal':<10} | {'Prepared':<9} | {'Wasted':<9} | {'Loss (INR)':<10}")
    print("-" * 68)

    # Show last 8 records
    for r in records[-8:]:
        print(f"{r['date']:<12} | {r['meal']:<10} | {r['prepared_kg']:<6} kg | {r['wasted_kg']:<6} kg | ₹{r['financial_loss']:<9.2f}")

    print("="*68)
    print(f"Total Prepared Food  : {total_prep:.1f} kg")
    print(f"Total Food Wasted    : {total_waste:.1f} kg ({waste_pct:.2f}% Waste Rate)")
    print(f"Total Financial Loss : ₹{total_loss:,.2f}")
    print("="*68)

def optimize_tomorrow_budget():
    """Predictive Optimizer using 3-day moving average wastage trend."""
    db = load_db()
    records = db["records"]
    rsvps = db.get("rsvps", [])

    print("\n" + "*"*60)
    print("   SMART BUDGET OPTIMIZER & MEAL PREPARATION ENGINE   ")
    print("*"*60)

    for meal in config.MEAL_TYPES:
        meal_logs = [r for r in records if r["meal"] == meal][-3:] # Last 3 days
        if not meal_logs:
            continue
        
        avg_waste = sum(r["wasted_kg"] for r in meal_logs) / len(meal_logs)
        avg_prep = sum(r["prepared_kg"] for r in meal_logs) / len(meal_logs)
        
        # Calculate skipped RSVP count for tomorrow
        skipping_students = len([r for r in rsvps if r["meal"] == meal and r["status"] == "Skipping"])
        rsvp_reduction_kg = skipping_students * 0.4  # Approx 400g food per meal

        recommended_prep = round(avg_prep - (avg_waste * 0.75) - rsvp_reduction_kg, 1)
        potential_saving = round((avg_prep - recommended_prep) * config.DEFAULT_COST_PER_KG[meal], 2)

        print(f"\n▶ Meal: {meal.upper()}")
        print(f"  • Recent Avg Prep      : {avg_prep:.1f} kg")
        print(f"  • Avg Waste Observed   : {avg_waste:.1f} kg")
        print(f"  • Student RSVP Skips   : {skipping_students} students")
        print(f"  ✔ OPTIMAL PREP SUGGESTION : {recommended_prep} kg")
        print(f"  💰 Estimated Daily Saving : ₹{max(0.0, potential_saving)}")
    print("\n" + "*"*60)