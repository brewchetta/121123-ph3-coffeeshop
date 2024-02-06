class Coffee:
    def __init__(self, name):
        self.name = name
        
    def access_current_orders(self, new_order=None):
        pass
    
    def access_relevant_customers(self, new_customer=None):
        pass
    
    def get_current_number_of_orders(self):
        pass
    
    def calculate_average_price_across_all_orders(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name
        
    def access_current_orders(self, new_order=None):
        pass
    
    def access_ordered_coffees(self, new_coffee=None):
        pass

    def check_total_money_spent(self):
        pass

class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price