import pytest

from classes.starter import Coffee, Customer, Order

# from solutions.coffee import Coffee
# from solutions.customer import Customer
# from solutions.order import Order

class TestCustomer:
    """ [TESTING SUITE: <Customer>] """

    def test_has_name(self):
        """ (INITIALIZERS AND PROPERTIES) A customer's name must be set upon initialization. """
        customer = Customer('Steve')
        assert (customer.name == "Steve")

    def test_can_change_name(self):
        """ (INITIALIZERS AND PROPERTIES) A customer's name must be mutable after instantiation. """
        customer = Customer('Steve')
        customer.name = "Stove"
        assert (customer.name == "Stove")

    def test_customer_name_is_str(self):
        """ (INITIALIZERS AND PROPERTIES) A customer's name must be of type `str`. """
        customer = Customer('Steve')
        assert (isinstance(customer.name, str))

        with pytest.raises(Exception):
            customer.name = 1

    def test_customer_name_length(self):
        """ (INITIALIZERS AND PROPERTIES) A customer's name must be inclusively between 1 and 15 characters in length. """
        customer = Customer('Steve')
        assert (len(customer.name) == 5)

        with pytest.raises(Exception):
            customer.name = "NameLongerThan15Characters"

        with pytest.raises(Exception):
            customer.name = ""

    def test_has_many_orders(self):
        """ (OBJECT RELATIONAL METHODS) A customer must be able to associate to many orders. """
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)
        order_3 = Order(customer_2, coffee, 5)

        assert (len(customer.access_current_orders()) == 2)
        assert (not order_3 in customer.access_current_orders())
        assert (order_1 in customer.access_current_orders())
        assert (order_2 in customer.access_current_orders())

    def test_orders_of_type_order(self):
        """ (OBJECT RELATIONAL METHODS) A customer's orders must each be of type `<Order>`. """
        coffee = Coffee("Vanilla Latte")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 5)

        assert (isinstance(customer.access_current_orders()[0], Order))
        assert (isinstance(customer.access_current_orders()[1], Order))

    def test_has_many_coffees(self):
        """ (OBJECT RELATIONAL METHODS) A customer must be able to associate to many coffees. """
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")

        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee_2, 5)

        assert (coffee in customer.access_ordered_coffees())
        assert (coffee_2 in customer.access_ordered_coffees())

    def test_has_unique_coffees(self):
        """ (OBJECT RELATIONAL METHODS) A customer's coffees must each be unique. """
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")

        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2)
        order_2 = Order(customer, coffee, 2)
        order_3 = Order(customer, coffee_2, 5)

        assert (len(set(customer.access_ordered_coffees())) == len(customer.access_ordered_coffees()))
        assert (len(customer.access_ordered_coffees()) == 2)

    def test_coffees_of_type_coffee(self):
        """ (OBJECT RELATIONAL METHODS) A customer's coffees must each be of type `<Coffee>`. """
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Caramel Frappuccino")
        customer = Customer('Dima')
        order_1 = Order(customer, coffee, 3)
        order_2 = Order(customer, coffee_2, 5)

        assert (isinstance(customer.access_ordered_coffees()[0], Coffee))
        assert (isinstance(customer.access_ordered_coffees()[1], Coffee))

    def test_total_overall_spending(self):
        """ (AGGREGATE METHODS) From the context of a customer, one must be able to calculate the total money a customer spent on all coffees. """
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Caramel Frappuccino")
        coffee_3 = Coffee("Espresso")
        customer = Customer("Dima")
        order_1 = Order(customer, coffee, 5)
        order_2 = Order(customer, coffee_2, 3)
        order_3 = Order(customer, coffee_2, 4)
        order_4 = Order(customer, coffee_3, 2)
        order_5 = Order(customer, coffee_3, 2)

        assert (customer.check_total_money_spent() == 16)

    def test_total_spent_on_given_coffee(self):
        """ (AGGREGATE METHODS) From the context of a customer, one must be able to calculate the total money a customer spent on a specific coffee. """
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Caramel Frappuccino")
        coffee_3 = Coffee("Espresso")
        customer = Customer("Dima")
        order_1 = Order(customer, coffee, 5)
        order_2 = Order(customer, coffee_2, 3)
        order_3 = Order(customer, coffee_2, 4)
        order_4 = Order(customer, coffee_3, 2)
        order_5 = Order(customer, coffee_3, 2)

        assert (customer.check_total_money_spent("Vanilla Latte") == 5)
        assert (customer.check_total_money_spent("Caramel Frappuccino") == 7)
        assert (customer.check_total_money_spent("Espresso") == 4)
        assert (customer.check_total_money_spent("Apple Juice") == 0)
