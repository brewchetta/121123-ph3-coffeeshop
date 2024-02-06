"""
[OOPD] Customer Object Design:

    • One Customer has Many Orders. 
        --> One-to-Many
    • One Coffee can have Many Customers
        AND
      One Customer can have Many Coffees.
        --> Many-to-Many

[OOPD] Customer Class: Initialization/Properties.

    • METHOD: `Customer.__init__(self, name)`
        --> Customer should be initialized with a name
    • PROPERTY: `Customer.name`
        --> PROPERTY INITIALIZATION: `@property`
            --> Returns name
        --> PROPERTY SETTER: `@name.setter`
            --> Names must be of type str
            --> Names must be between 1 and 15 characters, inclusive
                --> raise Exception if setter fails

[OOPD] Customer Class: Relationships: Basic Methods/Properties.

    • METHOD: `Customer.access_current_orders(self, new_order=None)`
        --> Adds new orders to customer
        --> Returns a list of all orders a customer has ordered
        --> orders must be of type `Order`
        --> Will be called from `Order.__init__`

    • METHOD: `Customer.access_ordered_coffees(self, new_coffee=None)`
        --> Adds new coffees to customer
        --> Returns a unique list of all coffees a customer has ordered.
        --> Coffees must be of type `Coffee`
        --> Will be called from `Order.__init__`

[OOPD] Customer Class: Relationships: Aggregate/Associative Methods. 

    • METHOD: `Customer.check_total_money_spent(self, name_of_coffee=None)`
        --> Calculates total money spent for current customer on coffees.
            --> Return sum of all orders' prices for customer. 
            --> If current customer has no orders, return 0. 
        --> If `name_of_coffee` is provided, calculation is performed for total money spent on specific coffee. 
            --> `name_of_coffee` is NOT of type `Coffee`, but instead is of type `str`.
            --> If `name_of_coffee` does not match any `Coffee.name`, return 0. 
"""

class Customer:
    def __init__(self, name):
        self.name = name
        # A customer has many orders.
        self._orders = []
        # A customer has many coffees.
        self._coffees = []

    # REPRESENTATIONAL DUNDER METHOD: Not required – useful for testing functionality independent of PyTest suites.
    def __repr__(self):
        return f"<Customer(name=`{self.name}`, orders={self.orders}, coffees={self.coffees})>"

    # Initialize Property: `Customer.name`
    @property
    def name(self):
        return self._name
    
    # Functionalize Property with Setter: `Customer.name`
    @name.setter
    def name(self, name):
        # Create validations for data type (str) and length requirements of property
        NAME_IS_STR = (isinstance(name, str))
        NAME_IS_WITHIN_ACCEPTABLE_LENGTH = (1 <= len(name) <= 15)
        
        # Conditionally validate property to set property
        if NAME_IS_STR and NAME_IS_WITHIN_ACCEPTABLE_LENGTH:
            self._name = name
        else:
            raise Exception("Unacceptable data format for `Customer.name`!")
        
    # Add functionality to `Customer.access_current_orders()`
    def access_current_orders(self, new_order=None):
        # Get relative access to <Order> object
        from solutions.order import Order

        # Create validations for data type (Order) and instantiation of property
        ORDER_IS_INSTANTIATED = (new_order is not None)
        ORDER_IS_ORDER = (isinstance(new_order, Order))

        # Conditionally validate property to extend property list
        if ORDER_IS_INSTANTIATED and ORDER_IS_ORDER:
            self._orders.append(new_order)
        return self._orders
    
    # Add functionality to `Customer.access_ordered_coffees()`
    def access_ordered_coffees(self, new_coffee=None):
        # Get relative access to <Coffee> object
        from solutions.coffee import Coffee

        # Create validations for data type (Coffee) and uniqueness of property
        COFFEE_IS_UNIQUE = (new_coffee not in self._coffees)
        COFFEE_IS_COFFEE = (isinstance(new_coffee, Coffee))

        # Conditionally validate property to extend property list
        if COFFEE_IS_UNIQUE and COFFEE_IS_COFFEE:
            self._coffees.append(new_coffee)
        return self._coffees
    
    # Add functionality to `Customer.check_total_money_spent()`
    def check_total_money_spent(self, name_of_coffee=None):
        COFFEE_NAME_GIVEN = (name_of_coffee is not None)
        if COFFEE_NAME_GIVEN:
            total_spending_for_coffee = 0
            for coffee in self._coffees:
                if name_of_coffee == coffee.name:
                    # Sum all order prices for that coffee.
                    for order in self.access_current_orders():
                        if name_of_coffee == order.coffee.name:
                            total_spending_for_coffee += order.price
            return total_spending_for_coffee
        else:
            # Sum all order prices. 
            return sum([order.price for order in self.access_current_orders()])
        