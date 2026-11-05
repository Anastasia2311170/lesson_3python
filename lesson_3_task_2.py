from smartphone import Smartphone
catalog = [
    Smartphone("Samsung", "Galaxy A20", "8 111 111 11 11"),
    Smartphone("Apple", "iPhone 18 Pro", "8 999 999 00 11"),
    Smartphone("Samsung", "Galaxy A40", "8 111 999 15 17"),
    Smartphone("Xiaomi", "Radmi Note 13 Pro", "8 991 111 12 00"),
    Smartphone("OnePlus", "12", "8 111 111 11 11")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model} -  {phone.number}")
