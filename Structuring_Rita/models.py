from abc import ABC, abstractmethod

class Medicine(ABC):

    def __init__(self, name: str, quantity: int, price: float):

        if not isinstance(name, str):
            raise TypeError("Назва препарату має бути рядком (str)")
        if not isinstance(quantity, int):
            raise TypeError("Кількість має бути цілим числом (int)")
        if not isinstance(price, (float, int)):
            raise TypeError("Ціна має бути числом (float або int)")
        
        self.name = name
        self.quantity = quantity
        self.price = price


    @abstractmethod
    def requires_prescription(self) -> bool:
        pass

    @abstractmethod
    def storage_requirements(self) -> str:
        pass

    def total_price(self) -> float:
        return self.quantity * self.price

    def info(self) -> str:
        prescription_status = "Так" if self.requires_prescription() else "Ні"
        return (
            f"Назва: {self.name}\n"
            f"  - Загальна вартість: {self.total_price():.2f} грн\n"
            f"  - Потрібен рецепт: {prescription_status}\n"
            f"  - Умови зберігання: {self.storage_requirements()}\n"
        )



class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True 

    def storage_requirements(self) -> str:
        return "8–15°C, темне місце"

class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False 

    def storage_requirements(self) -> str:
        return "15–25°C, сухо"

class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "2–8°C, холодильник"

    def total_price(self) -> float:
        base_price = super().total_price() 
        return base_price * 1.10 