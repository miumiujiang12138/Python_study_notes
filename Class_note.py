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
        profile = {
           # 'first_name' : self.first_name,
           # 'last_name': self.last_name
        }
        profile['first_name'] = self.first_name
        profile['last_name'] = self.last_name
        for key,value in self.user_info.items():
            profile[key] = value
        print(profile)
    def greet_user(self):
        print('\nHello, '+self.first_name.title()+' '+self.last_name.title()+'!')
user1=User('jennie','king',location='Korean',age=27)
user1.describe_user()
user1.greet_user()

# 使用类

class User():
    def __init__(self,first_name,last_name,**user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0
    def describe_user(self):
        profile = {
           # 'first_name' : self.first_name,
           # 'last_name': self.last_name
        }
        profile['first_name'] = self.first_name
        profile['last_name'] = self.last_name
        for key,value in self.user_info.items():
            profile[key] = value
        print(profile)
    def greet_user(self):
        print('\nHello, '+self.first_name.title()+' '+self.last_name.title()+'!')
    def increment_login_attempts(self):
        self.login_attempts+=1
        print('The user`s login times: '+str(self.login_attempts))
    def reset_login_attempts(self):
        self.login_attempts = 0
        print('The rest login time: '+str(self.login_attempts))
user2 = User('jay','zhou',location = 'china',age=36)
user2.describe_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.reset_login_attempts()

# 继承
# 如果你要编写的类是现成类的特殊版本，可以使用继承。
# 一个类继承另一个类时它将自动获得另一个类的所有属性和方法；原有的类称之为父类，而新类称为子类
# 子类继承了父类所有的属性和方法，同时还可以定义自己的属性和方法

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas_tank = 450
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odeometer(self):
        print("This car has "+str(self.odometer)+' mailes on it.')
    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can`t roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer+=miles
    def fill_gas_tank(self):
        print("This car`s gas tank has "+str(self.gas_tank))
class Battery():
    """模拟电动汽车的电瓶"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery.")
    def get_range(self):
        """指出电瓶车的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size ==85:
            range = 270
        message = 'This car can go approximately '+str(range)
        message += ' miles on a full charge'
        print(message)
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """电动汽车子类"""
    def __init__(self,make,model,year):
        super().__init__(make,model,year)  # super()将子类与父类的参数关联起来，让子类实例包含父类的所有属性
        self.battery_size = Battery()      # 创建一个新的Battery实例,并且将该实例存储在属性self.battery_size中
    """    self.battery_size = 70   """             # 给子类定义属性和方法
       
                     
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery.")
    def fill_gas_tank(self):
        # 电动车没有油箱
        print("This car doesn`t need a gas car!") #重写父类中的同名方法，python只会关注子类中重写的部分
    """def fill_gas_tank(self):
        return super().fill_gas_tank()""" # 如果不是重写父类中的方法会用super()关联到父类中的同名方法

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
"""my_tesla.describe_battery() """
my_tesla.fill_gas_tank()
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()
my_tesla.battery_size.upgrade_battery()
my_tesla.battery_size.get_range()



        
