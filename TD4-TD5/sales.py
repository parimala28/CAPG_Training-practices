class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
    
    def get_details(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}"


class Orders:
    def __init__(self, order_id, customer, items, total_amount):
        self.order_id = order_id
        self.customer = customer  
        self.items = items  
        self.total_amount = total_amount
    
    def get_order_summary(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.name}, Items: {', '.join(self.items)}, Total: ${self.total_amount}"


class Transactions:
    def __init__(self):
        self.orders = []
    
    def add_order(self, order):
        if isinstance(order, Orders):
            self.orders.append(order)
            print("Order added successfully!")
        else:
            print("Invalid order object!")
    
    def list_transactions(self):
        return [order.get_order_summary() for order in self.orders]


# Example Usage
customer1 = Customer(1, "pari", "pari@gmail.com")
order1 = Orders(101, customer1, ["IceCream", "Cola"], 1200)

transaction = Transactions()
transaction.add_order(order1)

# List transactions
for summary in transaction.list_transactions():
    print(summary)
