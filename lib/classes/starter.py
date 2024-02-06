# Coffee -----< Order >------ Customer

class Coffee:

    def __init__(self, name):
        self.name = name

    @property # GETTER #
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        # set the name
        # the name doesn't change IF its already been created
        # hasattr --> will check if it already has the attribute 'name'
        # coffee_one.name = ????
        if not hasattr(self, "name"):
            self._name = new_name
        else:
            raise Exception("You failed! Cannot change name after instantiation.")
        
    # OBJECT RELATIONSHIP #
    def access_current_orders(self):
        # I need all the orders to look through...
        # return current orders for THIS (self) coffee
        return [ order for order in Order.all_orders if order.coffee == self ]

        # results = []
        # for order in Order.all_orders:
        #     if order.coffee == self:
        #         results.append(order)
        # return results
    
    def access_relevant_customers(self):
        # self is the instance of coffee
        # looking for all customers that made an order of this coffee
        # return those customers
        # chett said we're gonna use list comprehension
        my_customers =  [ order.customer for order in Order.all_orders if order.coffee == self ]
        return list( set(my_customers) )
    
    # AGGREGATE METHODS #
    def get_current_number_of_orders(self):
        # return the length of the current number of orders for this coffee
        return len( self.access_current_orders() )
    
    def calculate_average_price_across_all_orders(self):
        # return the average of prices for self's orders
        prices = [ order.price for order in self.access_current_orders() ]

        # average is the sum / the length
        return sum(prices) / self.get_current_number_of_orders()
        # get_current_number_of_orders will be the length

class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, new_name):
        # make sure the name is a string
        # make sure the name is between 1 and 15
        # if it is then...
        if type(new_name) == str and 1 <= len(new_name) <= 15:
            # set the name to the new_name
            self._name = new_name
        # OR
        else:
            # raise exception if it's not good
            raise Exception("ITS NO GOOD")

    # OBJECT RELATIONSHIP #
    def access_current_orders(self):
        return [ order for order in Order.all_orders if order.customer == self ]
    
    def access_ordered_coffees(self):
        my_coffees = [ order.coffee for order in Order.all_orders if order.customer == self ]
        return list( set(my_coffees) )

    # AGGREGATE METHODS #
    def check_total_money_spent(self, coffee_name=None):
        # return the sum of the prices of the orders for self

        if coffee_name is not None:
            coffee_name_prices_list = [ order.price for order in Order.all_orders if order.customer == self and order.coffee.name == coffee_name ]

            return sum(coffee_name_prices_list)
        else:
            all_prices_list = [ order.price for order in Order.all_orders if order.customer == self ]

            return sum(all_prices_list)


class Order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        # IF it has not already been created
        # AND it is between 1 and 10
        if not hasattr(self, "price") and 1 <= new_price <= 10:
            # set the price to the new price
            self._price = new_price
        else:
            # raise a good ol fashioned exception
            raise Exception("The price is not right")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise Exception("Customer must be a Customer")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else:
            raise Exception("Coffee must be a Coffee")