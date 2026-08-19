class Payment:
    def __init__(self, amount, status= "Pending"):
        self.amount = amount
        self.status = status
    
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount, card_num):
        super().__init__(amount)
        self.card_num = card_num

    def process_payment(self):
        super().process_payment()
        print(f"Payment Done by card num {self.card_num}")

class CashOnDelivery(Payment):
    def __init__(self, amount, delivery_address):
        super().__init__(amount)
        self.delivery_address = delivery_address

    def process_payment(self):
        super().process_payment()
        print(f"Cash Collect at deliver address {self.delivery_address}")


class Delivery:
    def __init__(self, delivery_id, rider_name, delivery_fee):
        self.delivery_id = delivery_id
        self.rider_name = rider_name
        self.delivery_fee = delivery_fee

    def get_estimated_time(self):
        print("*****Rider Details*****")
        print(f"Rider Name:{self.rider_name}|Delivery Id:{self.delivery_id}|Delivery Charges:{self.delivery_fee}")


class ExpressDelivery(Delivery):
    def __init__(self, delivery_id, rider_name, delivery_fee, priority_level):
        super().__init__(delivery_id, rider_name, delivery_fee)
        self.priority_level = priority_level

    def get_estimated_time(self):
        super().get_estimated_time()
        print("20-30 mins in delivery")

class StandardDelivery(Delivery):
    def __init__(self, delivery_id, rider_name, delivery_fee):
        super().__init__(delivery_id, rider_name, delivery_fee)

    def get_estimated_time(self):
        super().get_estimated_time()
        print("30-45 minutes in delivery")

class Product:
    def __init__(self,product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_details(self):
        print(f"Product Name:{self.name}|Product Price:{self.price}")

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Customer(User):
    def __init__(self, user_id, name, email, delivery_address):
        super().__init__(user_id, name, email)
        self.delivery_address = delivery_address


class RestaurantOwner(User):
    def __init__(self, user_id, name, email, restaurant_name):
        super().__init__(user_id, name, email)
        self.restaurant_name = restaurant_name

class Restaurant:
    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu = []

    def add_product(self, product_obj):
        self.menu.append(product_obj)


class Order:
    def __init__(self, order_id, customer, restaurant, products, payment, delivery):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.products = products        # List of Product objects
        self.payment = payment          # Payment object
        self.delivery = delivery        # Delivery object

    def calculate_total(self):
        items_total = sum(product.price for product in self.products)
        total_amount = items_total + self.delivery.delivery_fee
        return total_amount

    def __str__(self):
        product_names = ", ".join([p.name for p in self.products])
        return (
            f"\n================ ORDER DETAILS ================\n"
            f"Order ID       : #{self.order_id}\n"
            f"Customer Name  : {self.customer.name}\n"
            f"Address        : {self.customer.delivery_address}\n"
            f"Restaurant     : {self.restaurant.name}\n"
            f"Items Ordered  : {product_names}\n"
            f"Rider Name     : {self.delivery.rider_name}\n"
            f"Payment Status : {self.payment.status}\n"
            f"Total Bill     : PKR {self.calculate_total()}\n"
            f"==============================================="
        )

    def __gt__(self, other):
        return self.calculate_total() > other.calculate_total()



if __name__ == "__main__":
    # 1. Create Products
    p1 = Product(1, "Zinger Burger", 550)
    p2 = Product(2, "Fries", 200)
    p3 = Product(3, "Pizza", 1200)

    # 2. Create Restaurant & Add Products
    rest = Restaurant(101, "KFC Multan")
    rest.add_product(p1)
    rest.add_product(p2)

    # 3. Create Users
    cust1 = Customer(1, "Mudasir", "mudasir@email.com", "Bosal Road, Multan")
    cust2 = Customer(2, "Ali", "ali@email.com", "Gulberg, Lahore")

    # 4. Create Payment Methods
    pay1 = CreditCardPayment(amount=750, card_num=12345678)
    pay2 = CashOnDelivery(amount=1200, delivery_address=cust2.delivery_address)

    # 5. Create Delivery Methods
    del1 = ExpressDelivery(delivery_id=1, rider_name="Ahmad", delivery_fee=150, priority_level="High")
    del2 = StandardDelivery(delivery_id=2, rider_name="Usman", delivery_fee=80)

    # 6. Create Orders
    order1 = Order(501, cust1, rest, [p1, p2], pay1, del1)
    order2 = Order(502, cust2, rest, [p3], pay2, del2)

    # Process Payments & Print Orders
    pay1.process_payment()
    print(order1)

    print("\n-----------------------------------------------")
    
    pay2.process_payment()
    print(order2)

    # 7. Compare Two Orders (__gt__ Dunder Method)
    print("\n--- ORDER COMPARISON ---")
    if order1 > order2:
        print(f"Order #{order1.order_id} is more expensive than Order #{order2.order_id}.")
    else:
        print(f"Order #{order2.order_id} is more expensive than Order #{order1.order_id}.")

