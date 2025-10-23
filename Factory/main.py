from documents import DocumentFactory

document_types_to_create = ['report', 'invoice', 'contract']

print("--- Починаємо обробку документів ---")

for doc_type in document_types_to_create:
    print(f"\nЗапит на створення: '{doc_type}'")

    document = DocumentFactory.create(doc_type)
    rendered_doc = document.render()
    
    print(f"Результат:\n{rendered_doc}")

print("-" * 30)

unknown_type = 'brochure'
print(f"\nСпроба створити невідомий тип '{unknown_type}':")
try:
    doc = DocumentFactory.create(unknown_type)
    print(doc.render())
except ValueError as e:
    print(f"Спіймали помилку, як і очікувалось: {e}")