# Author: Andrew Kamand
# Date: 1/15/2020
# Description: Code for an online store simulator that is made up of three classes: Product, Customer, and Store.


class Product:
    """A Product object represents a product with an ID code, title, description, price and quantity available."""
    def __init__(self, id_code, title, description, price, quantity_available):
        """Initializes a new Product with the specified id code, title, description, price, and quantity available."""
        self._id_code = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_id_code(self):
        """Returns the Product's id_code."""
        return self._id_code

    def get_title(self):
        """Returns the Product's title."""
        return self._title

    def get_description(self):
        """Returns the Product's description."""
        return self._description

    def get_price(self):
        """Returns the Product's price."""
        return self._price

    def get_quantity_available(self):
        """Returns the Product's quantity_available."""
        return self._quantity_available

    def decrease_quantity(self):
        """Decreases the Product's quantity available by one."""
        self._quantity_available -= 1


class Customer:
    """A Customer object represents a customer with a name, account ID, premium member status, and a cart."""
    def __init__(self, name, account_ID, premium_member):
        """Initializes a new Customer with the specified name, account ID, and premium member status, along with an empty cart."""
        self._name = name
        self._account_ID = account_ID
        self._premium_member = premium_member
        self._cart = []

    def get_cart(self):
        """Returns the Customer's cart."""
        return self._cart

    def get_name(self):
        """Returns the Customer's name."""
        return self._name

    def get_account_ID(self):
        """Returns the Customer's account ID"""
        return self._account_ID

    def is_premium_member(self):
        """Returns whether the Customer is a premium member."""
        return self._premium_member

    def add_product_to_cart(self, product_id):
        """Adds the product ID code to the Customer's cart."""
        self._cart.append(product_id)

    def empty_cart(self):
        """Empties the Customer's cart."""
        self._cart = []


class Store:
    """A Store object represents a store, which contains a list of Product objects as inventory and a list of Customer objects as members."""
    def __init__(self):
        """Initializes a new Store with an empty inventory list and empty member list."""
        self._inventory = []
        self._members = []

    def add_product(self, product):
        """Adds a Product to the inventory."""
        self._inventory.append(product)

    def add_member(self, customer):
        """Adds a Customer to members."""
        self._members.append(customer)

    def get_inventory(self):
        """Returns the store's inventory list."""
        return self._inventory

    def get_members(self):
        """Returns the store's members list."""
        return self._members

    def get_product_from_ID(self, product_id_match):
        """Returns the Product with the matching ID. If no matching ID is found, it returns the special value None."""
        # check inventory for a product id match
        for x in self._inventory:
            if product_id_match == x.get_id_code():
                return x
            else:
                return None

    def get_member_from_ID(self, member_id_match):
        """"Returns the Customer with the matching ID. If no matching ID is found, it returns the special value None."""
        # check members for a member id match
        for x in self._members:
            if member_id_match == x.get_account_ID():
                return x
            else:
                return None

    def product_search(self, search_string):
        """Return a sorted list of ID codes for every product whose title or description contains the search string."""
        # create empty list to hold search matches
        matched_products = []

        # search title and description for the search_string word, and add the product id of any matches to a new list
        for x in self.get_inventory():
            # create new variables that convert search_string, the product title, and the product description to all lowercase
            lower_search_string = search_string.lower()
            temporary_title = x.get_title()
            temporary_description = x.get_description()
            lower_title = temporary_title.lower()
            lower_description = temporary_description.lower()

            # add product id of any matches to newly created matched_products list
            if lower_search_string in lower_title or lower_search_string in lower_description:
                matched_products.append(x.get_id_code())

        # sort and return matched product list
        matched_products.sort()
        return matched_products

    def add_product_to_member_cart(self, product_ID, member_ID):
        """Add product to member's cart if product and member ID found, otherwise return not found statement."""
        # find product in inventory with given product ID
        product_match = self.get_product_from_ID(product_ID)
        # find member in members with given member ID
        member_match = self.get_member_from_ID(member_ID)

        # check if product and member ID's are valid
        if product_match == None:
            return "product ID not found"
        if member_match == None:
            return "member ID not found"
        # if product is still available, add product to member's cart and return notification, else return out of stock notification
        else:
            if product_match.get_quantity_available() > 0:
                member_match.add_product_to_cart(product_ID)
                return "product added to cart"
            else:
                return "product out of stock"

    def check_out_member(self, member_ID):
        """Returns the total charge for a member's cart, provided the member_ID is valid and the products are in stock."""
        # find member in members with given member ID
        member_match = self.get_member_from_ID(member_ID)
        # initialize variable for total cost of cart
        total_cost = 0
        # if member ID is invalid then raise exception error, InvalidCheckoutError
        if member_match == None:
            raise InvalidCheckoutError()
        # tabulate total cost of items in cart
        else:
            for x in member_match.get_cart():
                product_match = self.get_product_from_ID(x)

                # check product quantity, if available, add cost and decrease product quantity
                if product_match.get_quantity_available() > 0:
                    total_cost += product_match.get_price()
                    product_match.decrease_quantity()

                    # check if member is premium status or not, and charge 7% shipping fee if not
                    if member_match.is_premium_member() == False:
                        total_cost = total_cost*1.07

        # empty cart and return total charge
        member_match.empty_cart()
        return total_cost


# exception error class "InvalidCheckoutError", raise when member ID not found
class InvalidCheckoutError(Exception):
    pass


def main():
    # sample code to checkout a member
    p1 = Product("830", "Nintendo Switch", "console and handheld in one video game platform made by nintendo", 300, 9)
    p2 = Product("835", "Playstation", "Sony videogame console", 400, 5)
    p3 = Product("5", "Xbox one", "Microsoft videogame console", 350, 7)
    c1 = Customer("David", "ABC", False)
    myStore = Store()
    myStore.add_product(p1)
    myStore.add_product(p2)
    myStore.add_product(p3)
    myStore.add_member(c1)
    print(myStore.get_members())
    print(myStore.get_inventory())
    print(myStore.get_member_from_ID("ABC"))
    print(myStore.get_product_from_ID("835"))
    myStore.add_product_to_member_cart("830", "ABC")
    myStore.add_product_to_member_cart("835", "ABC")
    myStore.add_product_to_member_cart("5", "ABC")
    print(c1.get_cart())
    try:
        print(myStore.check_out_member("ABC"))
    except InvalidCheckoutError:
        print("Member ID not found.")


if __name__ == '__main__':
    main()
