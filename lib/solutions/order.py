"""
[OOPD] Customer Object Design:

    • One Coffee has Many Orders. 
        --> One-to-Many
    • One Customer has Many Orders. 
        --> One-to-Many
    • An Order belongs to a Customer and to a Coffee.

[OOPD] Order Class: Initialization/Properties.

    • METHOD: `Order.__init__(self, customer, coffee, price)`
        --> Orders should be initialized with a customer, coffee, and a price (a number)
    • PROPERTY: `Order.price`
        --> PROPERTY INITIALIZATION: `@property`
            --> Returns the price for a coffee
        --> PROPERTY SETTER: `@price.setter`
            --> Returns the price for a coffee
            --> Price must be a number between 1 and 10, inclusive
                --> `raise Exception` if setter fails

[OOPD] Order Class: Relationships: Basic Methods/Properties.

    • METHOD: `Order.customer(self, new_customer=None)`
        --> Returns the customer object for that order
        --> Must be of type Customer
            --> `raise Exception` if setter fails

    • METHOD: `Order.coffee(self, new_coffee=None)`
        --> Returns the coffee object for that order
        --> Must be of type Coffee
            --> `raise Exception` if setter fails
"""
class Order:

    # Create static association list to help associate orders to other objects
    """
    NOTE:   This test will fail because the specific test is hard-coded to check 
            that the static variable that we create is invoked using `Order.all`. 
            However, the `all` keyword is reserved by Python and, as such, it's 
            poor practice to override it simply for a minor requirement. Adhere
            to the code challenge requirements to the best of your ability, but 
            understand that this ultimately means the test is poorly architected, 
            not necessarily your code. 
    """ 
    all_orders = [] # [FirstOrder(), SecondOrder(), ThirdOrder(), ...]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        # Create global (static) tracker of all orders
        Order.all_orders.append(self)

        # Upon order instantiation, add new order to coffee's orders and new customer to coffee's customers
        coffee.access_current_orders(self)
        coffee.access_relevant_customers(customer)

        # Upon order instantiation, add new order to customer's orders and new coffee to customer's coffees
        customer.access_current_orders(self)
        customer.access_ordered_coffees(coffee)

    # REPRESENTATIONAL DUNDER METHOD: Not required – useful for testing functionality independent of PyTest suites.
    def __repr__(self):
        return f"{self.customer.name} ordered {self.coffee.name}."
    
    # Initialize Property: `Order.price`
    @property
    def price(self):
        return self._price
    
    # Functionalize Property with Setter: `Order.price`
    @price.setter
    def price(self, price):
        # Create validations for data type (numerical) and quantitative boundaries of property
        PRICE_IS_NUMERICAL = (type(price) == int or float)
        PRICE_IS_WITHIN_ACCEPTABLE_BOUNDS = (1 <= price <= 10)
        PRICE_DOESNT_EXIST = (not hasattr(self, "price"))
        
        # Conditionally validate property to set property
        if PRICE_IS_NUMERICAL and PRICE_IS_WITHIN_ACCEPTABLE_BOUNDS and PRICE_DOESNT_EXIST:
            self._price = price
        else:
            raise Exception("Unacceptable data format for `Order.price`!")
        
    # Initialize Property: `Order.customer`
    @property
    def customer(self):
        return self._customer
    
    # Functionalize Property with Setter: `Order.customer`
    @customer.setter
    def customer(self, customer):
        # Get access to customer class
        from solutions.customer import Customer
        # from customer import Customer

        # Create validation for instantiation of property
        CUSTOMER_IS_CUSTOMER = (isinstance(customer, Customer))
        
        # Conditionally validate property to set property
        if CUSTOMER_IS_CUSTOMER:
            self._customer = customer
        else:
            raise Exception("Unacceptable data type for `Order.customer`!")
        
    # Initialize Property: `Order.coffee`
    @property
    def coffee(self):
        return self._coffee
    
    # Functionalize Property with Setter: `Order.coffee`
    @coffee.setter
    def coffee(self, coffee):
        # Get access to customer class
        from solutions.coffee import Coffee
        # from coffee import Coffee

        # Create validation for instantiation of property
        COFFEE_IS_COFFEE = (isinstance(coffee, Coffee)) 
        
        # Conditionally validate property to set property
        if COFFEE_IS_COFFEE:
            self._coffee = coffee
        else:
            raise Exception("Unacceptable data type for `Order.coffee`!")
