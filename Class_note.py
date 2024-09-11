# 在面向对象编程中，你编写表示现实世界中的事务和情景的类，并且基于这些类创建对象
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print('The restaurant name is '+self.restaurant_name+
              '\nThe restaurant cuisine_type is '+self.cuisine_type)
    def restaurant_status(self):
        print(self.restaurant_name+' status is on door!')
restaurant = Restaurant('manji','dessert')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.restaurant_status()

class User():
    def __init__(self,first_name,last_name,**user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
    def describe_user(self):
        profile = {}
        profile['first_name'] = self.first_name
        profile['last_name'] = self.last_name
        for key,value in self.user_info.items():
            profile[key] = value
        print(profile)
    def greet_user(self):
        print('\nHello, '+self.first_name+''+self.last_name+'!')
user1=User('jennie','king',location='Korean',age=27)
user1.describe_user()
user1.greet_user()

        
        
