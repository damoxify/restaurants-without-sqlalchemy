# Customer, Restaurant, and Review Management System

For this project, we are working with a Yelp-style domain, managing three models: `Restaurant`, `Customer`, and `Review`. In this system, a `Restaurant` has many `Reviews`, a `Customer` has many `Reviews`, and a `Review` belongs to both a `Customer` and a `Restaurant`. The `Restaurant`-`Customer` relationship is a many-to-many relationship.

Please note that you should create your own test sample instances to ensure that your code works correctly in the console before submitting it.

## Classes and Instances

### Customer Class
The `Customer` class represents a customer and includes the following attributes and methods:

#### Attributes
- `given_name` (str): The given name of the customer.
- `family_name` (str): The family name of the customer.
- `reviews` (list): A list of reviews made by the customer.
- `all_customers` (class variable): A list of all customer instances.

#### Methods
- `__init__(self, given_name, family_name)`: Initializes a customer with a given name and family name.
- `given_name(self)`: Returns the given name of the customer.
- `family_name(self)`: Returns the family name of the customer.
- `full_name(self)`: Returns the full name of the customer.
- `all(cls)`: Returns a list of all customer instances.

### Restaurant Class
The `Restaurant` class represents a restaurant and includes the following attributes and methods:

#### Attributes
- `name` (str): The name of the restaurant.
- `all_restaurants` (class variable): A list of all restaurant instances.

#### Methods
- `__init__(self, name)`: Initializes a restaurant with a name.
- `name(self)`: Returns the name of the restaurant.
- `reviews(self)`: Returns a list of reviews for the restaurant.
- `customers(self)`: Returns a unique list of customers who have reviewed the restaurant.

### Review Class
The `Review` class represents a review and includes the following attributes and methods:

#### Attributes
- `customer` (Customer): The customer who wrote the review.
- `restaurant` (Restaurant): The restaurant being reviewed.
- `rating` (int): The rating given in the review.
- `all_reviews` (class variable): A list of all review instances.

#### Methods
- `__init__(self, customer, restaurant, rating)`: Initializes a review with a customer, restaurant, and rating.
- `rating(self)`: Returns the rating given in the review.
- `customer(self)`: Returns the customer who wrote the review.
- `restaurant(self)`: Returns the restaurant being reviewed.
- `all(cls)`: Returns a list of all review instances.

## Object Relationship Methods

### Review Class
- `customer(self)`: Returns the customer object for that review.
- `restaurant(self)`: Returns the restaurant object for that review.

### Restaurant Class
- `reviews(self)`: Returns a list of all reviews for that restaurant.
- `customers(self)`: Returns a unique list of customers who have reviewed the restaurant.

### Customer Class
- `restaurants(self)`: Returns a unique list of all restaurants the customer has reviewed.
- `add_review(self, restaurant, rating)`: Creates a new review and associates it with the customer and restaurant.

## Aggregate and Association Methods

### Customer Class
- `num_reviews(self)`: Returns the total number of reviews authored by the customer.
- `find_by_name(cls, name)`: Given a full name, returns the first customer whose full name matches.
- `find_all_by_given_name(cls, name)`: Given a given name, returns a list containing all customers with that given name.

### Restaurant Class
- `average_star_rating(self)`: Returns the average star rating for the restaurant based on its reviews. The average is calculated by adding up all the ratings and dividing by the number of ratings.

## Sample Usage
The provided code includes sample instances of customers, restaurants, and reviews, as well as testing of various methods. You can use this code as a reference to understand how to interact with these classes and their methods.

Before submitting your code, make sure to create and test your own sample instances to verify that your methods work as expected. Prioritize writing methods that work over writing more methods that don't work. You can refactor your code to adhere to best practices if there is time at the end.