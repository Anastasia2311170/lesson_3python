from Address import Address
from Mailing import Mailing

from_addr = Address("456276", "Самара", "Куйбышевская", "110", "1")
to_addr = Address("190000", "Рязань", "Невский проспект", "2", "20")

my_mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=600,
    track="RU123456789")

output = (
    f"Отправление {my_mailing.track}"
    f"из {my_mailing.from_address.index}, {my_mailing.from_address.city},"
    f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment}"
    f"в {my_mailing.to_address.index}, {my_mailing.to_address.city},"
    f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - {my_mailing.to_address.apartment}."
    f"Стоимость {my_mailing.cost} рублей.")

print(output)
