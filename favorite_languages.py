# 从Python标准库里导入模块中的类并且使用
# 模块collections中OrderedDict类的用法，OrderedDict可以创建一个有序字典，
# 传统的字典只能够将信息关联起来但是不能记录其中的键值对添加的顺序

from collections import OrderedDict
favorite_languages = OrderedDict()  # OrderedDict可以创建一个空的有序字典，以后会经常用到
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
for name,languages in favorite_languages.items():
    print(name.title()+"`s favorite language is "+languages.title()+".")