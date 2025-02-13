from product import Product
from product_manager import ProductManager

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
print("Total inventory value:", manager.total_inventory_value())