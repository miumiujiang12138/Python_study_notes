# 需要将一系列字典存储在列表中，或者将列表作为值存储在字典中，这称之为“嵌套”
 
## 字典列表
aliens = []
for alien_num in range(30):  #range()返回一系列数字，其中唯一的用途是告诉python我们要重复循环多少次
    new_alien = {'color':'green','points':5,'speed':'slow'} 
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

#显示创建了多少个外星人
print("Total number of aliens:"+str(len(aliens)))

#在字典中存储列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],    # 每当需要将字典中的一个键关联到多个值时，都可以在字典中嵌套一个列表
}

print("You ordered a "+pizza['crust']+"-crust pizza"+
      " with the fellowing toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)

#在字典中存储字典
# 如果有多个网站用户，每个用户都有独特的用户名，可在字典中将用户名作为键，然后将用户的信息存储在一个字典中
# 并将该字典作为与用户名相关联的值
users ={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    },
}

for username,user_info in users.items():   # 使用item()来访问字典中的键和值
    print("\nUsername:"+username)
    full_name = user_info['first']+user_info['last']
    location = user_info['location']
    print('\nFull name:'+full_name.title())
    print('\nLocation:'+location.title())

favorite_languages = {
    'jen':'python',
    'sara':'c',
    'edward':'ruby',
    'phli':'python'
}
survey_list =['jen','edward','amy','aber']

for people in survey_list:
    if people in favorite_languages.keys():      #用.keys()访问字典里的键
        print("\n"+people.title()+" ,Thanks for your participation!")
    else:
        print("\n"+people.title()+" ,Please take your poll!")
