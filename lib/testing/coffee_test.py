import pytest

from classes.starter import Coffee, Customer, Order

# from solutions.coffee import Coffee
# from solutions.customer import Customer
# from solutions.order import Order

class TestCoffee:
    """ [TESTING SUITE: <Coffee>] """

    def test_has_name(self):
        """ (INITIALIZERS AND PROPERTIES) A coffee's name must be set upon initialization. """
        coffee = Coffee("Mocha")
        assert (coffee.name == "Mocha")

    def test_name_setter(self):
        """ (INITIALIZERS AND PROPERTIES) A coffee's name must be immutable after instantiation. """
        coffee = Coffee("Mocha")

        with pytest.raises(Exception):
            coffee.name = "Peppermint Mocha"

    def test_name_is_string(self):
        """ (INITIALIZERS AND PROPERTIES) A coffee's name must be of type `str`. """
        coffee = Coffee("Mocha")
        assert (isinstance(coffee.name, str))

    def test_has_many_orders(self):
        """ (OBJECT RELATIONAL METHODS) A coffee must be able to associate to many orders. """
        coffee = Coffee("Hazelnut Latte")
        coffee_2 = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)
        order_3 = Order(customer, coffee_2, 5)

        assert (len(coffee.access_current_orders()) == 2)
        assert (order_1 in coffee.access_current_orders())
        assert (order_2 in coffee.access_current_orders())
        assert (not order_3 in coffee.access_current_orders())

    def test_orders_of_type_order(self):
        """ (OBJECT RELATIONAL METHODS) A coffee's orders must each be of type `<Order>`. """
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(coffee.access_current_orders()[0], Order))
        assert (isinstance(coffee.access_current_orders()[1], Order))

    def test_has_many_customers(self):
        """ (OBJECT RELATIONAL METHODS) A coffee must be able to associate to many customers. """
        coffee = Coffee("Flat White")

        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (customer in coffee.access_relevant_customers())
        assert (customer_2 in coffee.access_relevant_customers())

    def test_has_unique_customers(self):
        """ (OBJECT RELATIONAL METHODS) A coffee's customers must each be unique. """
        coffee = Coffee("Vanilla Latte")

        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 2)
        order_3 = Order(customer, coffee, 5)

        assert (len(set(coffee.access_relevant_customers())) == len(coffee.access_relevant_customers()))
        assert (len(coffee.access_relevant_customers()) == 2)

    def test_customers_of_type_customer(self):
        """ (OBJECT RELATIONAL METHODS) A coffee's customers must each be of type `<Customer>`. """
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (isinstance(coffee.access_relevant_customers()[0], Customer))
        assert (isinstance(coffee.access_relevant_customers()[1], Customer))

    def test_get_number_of_orders(self):
        """ (AGGREGATE METHODS) From the context of a coffee, one must be able to determine the current number of orders for that coffee. """
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (coffee.get_current_number_of_orders() == 2)

    def test_average_price(self):
        """ (AGGREGATE METHODS) From the context of a coffee, one must be able to determine the average price across all orders for that coffee. """
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        Order(customer, coffee, 2)
        Order(customer_2, coffee, 5)

        assert (coffee.calculate_average_price_across_all_orders() == 3.5)
