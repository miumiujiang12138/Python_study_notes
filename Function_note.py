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

# 给形参指定默认值，在调用函数中给形参提供了实参时，Python将使用指定的实参值，否则，将使用形参的默认值

def describe_pet(pet_name,animal_type='dog'): #给animal_type指定为dog
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='wille')
describe_pet('wille')  #如果直接传实参，调用函数时会默认为位置实参
describe_pet(pet_name='harry',animal_type='hamster') #在函数有默认形参的情况下，可以用关键字实参来描述你想要的内容

def get_formatted_name(first_name,last_name):
    """"返回整洁的姓名"""
    full_name = first_name+''+last_name
    return full_name.title()
musician = get_formatted_name('jimi','kui')  #将结果返回到调用行
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''): #让middle_name的实参变成可选的
    if middle_name:
        full_name = first_name+''+middle_name+''+last_name
    else:
        full_name = first_name+''+last_name
    return full_name.title()

musician = get_formatted_name('jimi','kui')
musician = get_formatted_name('jimi','kui','john')

def build_person(first_name,last_name):
    """"返回字典，该字典包含一个人的信息"""
    person ={'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

def build_person(first_name,last_name,age=''):
    """"返回字典，该字典包含一个人的信息"""
    person ={'first':first_name,'last':last_name}
    if age:
        person['age'] = age
   
    return person
musician = build_person('jimi','kui','27')
print(musician)

# 编写函数的理念是，每个函数只负责一项具体的工作；如果你发现你编写的函数执行的任务过多，请试着把它分解为两个
#函数，另外，一个函数总是可以调用另外一个函数，有助于将复杂的任务分解为一系列的步骤
magicians=['john','mike','jacky']
def show_magicians(magicians):
    for people in magicians:
        print(people.title())
show_magicians(magicians)
def make_great(magicians,complete_magicians):
    while magicians:
        current_magician = 'The Great '+magicians.pop()
        complete_magicians.append(current_magician)
def show_magicians(comlete_magicians):
    for magician in comlete_magicians:
     print(magician)
completed_magicians=[]
"""make_great(magicians,completed_magicians)   
show_magicians(completed_magicians)
print(magicians)"""

make_great(magicians[:],completed_magicians) # 切片[:]表示创建列表的副本，不会影响本身的表,一般情况下不适用，只在某些特定场景下用，因为会占用计算机资源
show_magicians(completed_magicians)
print(magicians)

# 传递任意数量的实参
def make_pizza(*toppings):  #形参名*toppings中的星号让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# 结合使用位置实参和任意数量的实参  python会先匹配位置实参和关键字实参，再将余下的实参收集到最后一个形参中
def make_pizza(size,*toppings):
    print('\nMaking a '+str(size)+'-inch pizza with the following toppings:')
    for topping in toppings:
        print('-'+topping)
make_pizza(12,'pepperoni')
make_pizza(16,'mushrooms','green peppers','extra cheese')

# 使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile = build_profile('huang','qian',age=12,location='guangzhou')
print(user_profile)
    

    
