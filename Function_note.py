# 函数是带名字的代码块，用于完成具体的工作
# 如果需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，而只需调用执行该任务的函数
# 这个脚本中你将会看到如何向函数传递信息、如何编写主要任务是显示信息的函数、还有用于处理数据并返回一组值的函数
# 最后将会展示如何将函数存储在被称之为模块的独立文件中，让主程序文件的组织更为有序。

# 实参和形参
# 调用函数时，将要让函数使用的信息放在括号内。如：
def greet_user(username):
    """显示简单的问候语"""
    print("Hello,"+username.title()+"!")
greet_user('jesse')  #在greet_user('jesse')中，将实参'jesse'放在括号中传递给函数，这个值被存储在形参username中

# 传递实参之位置实参
# 即实参调用顺序与形参顺序相同
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('dog','judy')  #'dog'对应animal_type,'judy'对应pet_name

# 传递实参之关键字实参
# 关键字实参是传递给函数的名称——值对，直接在实参中将形参名和实参值关联起来，关键字实参让你无需考虑函数调用中的实参顺序
describe_pet(animal_type='cat',pet_name='momo')
describe_pet(pet_name='feng',animal_type='dog')
