class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)

class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def reviews(self):
        return [review for review in Review.all_reviews if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))

class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews

# Create instances and add sample data
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

restaurant1 = Restaurant("Good Eats")
restaurant2 = Restaurant("Tasty Bites")

customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 5)
customer2.add_review(restaurant1, 3)

# Testing methods
print("All Customers:", Customer.all())  # Should print a list of all customers
print("All Reviews:", Review.all())  # Should print a list of all reviews

# Additional methods for Customer and Restaurant
print("Number of Reviews by Customer 1:", len(customer1.reviews))  # Should print 2
print("Customer by Full Name 'John Doe':", Customer.find_by_name("John Doe").full_name())  # Should print "John Doe"
print("Customers with Given Name 'John':", [c.full_name() for c in Customer.find_all_by_given_name("John")])  # Should print a list of customers

print("Average Star Rating for Restaurant 1:", restaurant1.average_star_rating())  # Should print the average star rating for restaurant1
