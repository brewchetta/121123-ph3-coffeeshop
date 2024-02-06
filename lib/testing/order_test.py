import pytest

from classes.starter import Coffee, Customer, Order

# from solutions.coffee import Coffee
# from solutions.customer import Customer
# from solutions.order import Order

class TestOrders:
    """ [TESTING SUITE: <Order>] """

    def test_has_price(self):
        """ (INITIALIZERS AND PROPERTIES) An order's price must be set upon initialization. """
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (order_1.price == 2)
        assert (order_2.price == 5)

    def test_cannot_change_price(self):
        """ (INITIALIZERS AND PROPERTIES) An order's price must be immutable after instantiation. """
        coffee = Coffee("Hazelnut Latte")
        customer = Customer('Steve')
        order = Order(customer, coffee, 3)
        
        with pytest.raises(Exception):
            order.price = 4

    def test_order_price_is_int(self):
        """ (INITIALIZERS AND PROPERTIES) An order's price must be of type `int`. """
        coffee = Coffee("Cappuccino")
        customer = Customer('Steve')
        
        with pytest.raises(Exception):
            order = Order(customer, coffee, "free")

    def test_order_quantity(self):
        """ (INITIALIZERS AND PROPERTIES) An order's price must be inclusively between 1 and 10 in magnitude. """
        coffee = Coffee("Espresso")
        customer = Customer('Steve')

        with pytest.raises(Exception):
            order_1 = Order(customer, coffee, -2)

        with pytest.raises(Exception):
            order_2 = Order(customer, coffee, 72)

    def test_has_a_customer(self):
        """ (OBJECT RELATIONAL METHODS) An order is linked to a single customer instance. """
        coffee = Coffee("Mocha")
        customer_1 = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer_1, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (order_1.customer == customer_1)
        assert (order_2.customer == customer_2)

    def test_customer_of_type_customer(self):
        """ (OBJECT RELATIONAL METHODS) An ordering customer is of type `<Customer>`. """
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(order_1.customer, Customer))
        assert (isinstance(order_2.customer, Customer))

    def test_has_a_coffee(self):
        """ (OBJECT RELATIONAL METHODS) An order is linked to a single coffee instance. """
        coffee_1 = Coffee("Mocha")
        coffee_2 = Coffee("Peppermint Mocha")
        customer = Customer('Wayne')
        order_1 = Order(customer, coffee_1, 2)
        order_2 = Order(customer, coffee_2, 5)

        assert (order_1.coffee == coffee_1)
        assert (order_2.coffee == coffee_2)

    def test_coffee_of_type_coffee(self):
        """ (OBJECT RELATIONAL METHODS) An ordered coffee is of type `<Coffee>`. """
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(order_1.coffee, Coffee))
        assert (isinstance(order_2.coffee, Coffee))

    def test_get_all_orders(self):
        """ (OBJECT RELATIONAL METHODS) The `<Order>` class schematic tracks created instances of itself. """
        Order.all_orders = []
        coffee = Coffee("Mocha")
        customer = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer_2, coffee, 5)

        assert (len(Order.all_orders) == 2)
        assert (order_1 in Order.all_orders)
        assert (order_2 in Order.all_orders)
