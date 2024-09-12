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