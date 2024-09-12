# 读取文件,注意如果是在Linux/macOS系统中用斜杠'\',如果是在windowS系统中用r+反斜杠'\'，即r'C:\...'
with open('file\pi_digits.txt') as file_object: # 你只管打开文件，并在需要的时候使用它，
                                                # python会在适当的时候自动关闭
    contents = file_object.read()
    print(contents.rstrip()) #rstrip()删除字符串末尾空白

file_path = 'file\pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

# 使用关键字with时，open()返回的文件对象只在with代码块内可使用，
# 如果你需要在with代码块以外使用你可以将文件的各行存储在一个列表中，并在with代码块外使用该列表

with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip()) #rstrip()可以用来消除换行符、制表符

with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
pi_string = ''
for line in lines:
    pi_string += line.strip()  #strip()可以用来消除空格
print(pi_string)
print(len(pi_string))



