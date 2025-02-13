from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

#dodavanje proizvoda
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mobilni telefon", 500, 10)
p3 = Product("Mis", 10, 20)
manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

#proizvod i ukupna vrednost
manager.display_products()
print("Ukukpna vrednost inventara:", manager.total_inventory_value())



cart = Cart()

#dodavanje proizvoda u korpu
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

#sadrzaj korpe i ukupne vrednosti
cart.display_cart()
print("Total cart value:", cart.calculate_total())