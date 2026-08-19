# 🍔 Food Delivery System (Python OOP)

A complete Object-Oriented Programming (OOP) implementation of a Food Delivery System in Python. The system handles multiple user types, restaurant menus, dynamic order processing, payment gateways, and delivery tracking.

## 🚀 Key Features & OOP Concepts

- **Inheritance**: 
  - `User` -> `Customer`, `RestaurantOwner` (Hierarchical)
  - `Payment` -> `CreditCardPayment`, `CashOnDelivery`
  - `Delivery` -> `ExpressDelivery`, `StandardDelivery`
- **Aggregation**: `Restaurant` manages a list of `Product` objects (`menu`).
- **Polymorphism**: Overridden `process_payment()` and `get_estimated_time()` methods across derived classes.
- **Dunder Methods**:
  - `__str__`: Formatted print statement for detailed order summaries.
  - `__gt__`: Comparison operator to compare order total amounts directly.

## 🛠️ Project Structure

`food_delivery_system.py` contains all domain models and execution logic:
- `Payment`, `CreditCardPayment`, `CashOnDelivery`
- `Delivery`, `ExpressDelivery`, `StandardDelivery`
- `Product`
- `User`, `Customer`, `RestaurantOwner`
- `Restaurant`
- `Order`

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/food-delivery-system-oop-python.git](https://github.com/MudasirManzoor4461/food-delivery-system-oop-python.git)