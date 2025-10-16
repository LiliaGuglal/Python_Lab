from models import Medicine, Antibiotic, Vitamin, Vaccine
from typing import List

def print_pharmacy_stock(stock: List[Medicine]):
    print("---- ІНФОРМАЦІЯ ПРО ПРЕПАРАТИ НА СКЛАДІ: ----")
    
    for med in stock:
        print(med.info())


pharmacy_stock = [
    Antibiotic(name="Амоксил", quantity=20, price=150.75),
    Vitamin(name="Вітамін C", quantity=100, price=80.00),
    Vaccine(name="Pfizer", quantity=50, price=500.50)
]

print_pharmacy_stock(pharmacy_stock)