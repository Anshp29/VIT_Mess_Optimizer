"""
Config file storing VIT Bhopal mess details and global constants.
"""

MESS_LOCATIONS = [
    "Block-1 Boys Mess",
    "Block-2 Boys Mess",
    "Girls Hostel Mess",
    "Food Street / Special Mess"
]

MEAL_TYPES = ["Breakfast", "Lunch", "Snacks", "Dinner"]

# Average cost per kg of cooked food (in INR)
DEFAULT_COST_PER_KG = {
    "Breakfast": 65.0,
    "Lunch": 90.0,
    "Snacks": 45.0,
    "Dinner": 85.0
}