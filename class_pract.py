class Restaurant():
    def __init__(self, restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print('Welcome to '+self.name.title())
        print('Have a taste of '+self.type.title()+' food')

    def open_restaurant(self):
        print('Opening now!')

    def set_number_served(self, number):
        self.number_served=number

    def increment_number_served(self, increment):
        while self.number_served < increment:
            self.number_served += 1

names=['vipkid','sayABC','lingualBus']
type='chinese'
for name in names:
    my_restaurant=Restaurant(name,type)
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

my_restaurant.number_served=20
print(my_restaurant.number_served)
my_restaurant.set_number_served(50)
print(my_restaurant.number_served)
my_restaurant.increment_number_served(100)
print(my_restaurant.number_served)

