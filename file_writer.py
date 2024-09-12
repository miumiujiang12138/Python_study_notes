# 写文件：保存数据最好的方式就是将其写入到文件中
filename = 'file/programming.txt'
with open(filename,'w') as file_object:         #打开文件时，可指定读取模式'r',写入模式'w',附加模式'a'或者能够读写
    file_object.write("I love programming.\n")    #模式'r+',如果省略了模式实参，python将以默认的只读模式打开文件
    file_object.write("I love creating games.\n")                                            #注意：python只能将字符串写入到文件中，要将数值数据存储在文本中，
                                                #必须先str()转成字符串
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")