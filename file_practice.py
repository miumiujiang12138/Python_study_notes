import json
def get_likey_num():
    """输入喜欢的数字"""
    likey_num = input("What is your favorite number?")
    filename = 'likey_num.json'
    with open(filename,'w') as f_obj:
        json.dump(likey_num,f_obj)
        return likey_num

def read_likey_num():
    filename = 'likey_num.json'
    try:
      with open(filename) as f_obj:
        likey_num = json.load(f_obj) #json.load()传参是传文件对象f_obj
    except FileNotFoundError:
       print("You have not add your favorite number!")
       return get_likey_num()
    else:
       print("Is "+likey_num +" your favorite number?")
       return likey_num

def greet_user():
   """问候并验证用户"""
  
   likey_num1 = read_likey_num()
   likey_num = get_likey_num()
   if likey_num1 and likey_num1==likey_num:
      print("Welcome back, "+likey_num1+" !")
   else:
      print("We have remenber your new favorite number is "+likey_num+"!")
      
#get_likey_num()
#read_likey_num()
#read_likey_num()
greet_user()
       