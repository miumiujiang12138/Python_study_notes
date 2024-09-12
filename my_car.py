from car import Car  #将类迁移到模块中并且导入该模块，使主程序文件变得更易读
from car import ElectricCar
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer = 23
my_new_car.read_odeometer()
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()

