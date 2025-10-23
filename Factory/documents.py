from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Report(Document):
    def render(self) -> str:
        return "Це тіло звіту (Report)... багато даних і графіків."

class Invoice(Document):
    def render(self) -> str:
        return "Це рахунок-фактура (Invoice). Список товарів і сума до оплати."

class Contract(Document):
    def render(self) -> str:
        return "Це юридичний контракт (Contract). Багато тексту дрібним шрифтом."


class DocumentFactory:
    @staticmethod
    def create(doc_type: str) -> Document:
        
        if doc_type == 'report':
            return Report()
        elif doc_type == 'invoice':
            return Invoice()
        elif doc_type == 'contract':
            return Contract()
        else:
            raise ValueError(f"Невідомий тип документа: {doc_type}")