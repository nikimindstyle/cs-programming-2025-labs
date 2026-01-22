staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
best = max(staff_shifts, key=lambda x: x["shift_cost"] * x["shifts"]) 
print(f"Максимальная стоимость: {best['name']}: {best['shift_cost'] * best['shifts']}") 