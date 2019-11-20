'''
1.让用户输入需要注册的用户名和密码,恭喜登录成功；
2.用只写的方式将用户名和密码写入到一个文件中format;
3.建立一个列表，进行while循环，输入用户名和密码
4.将文件中的用户名和密码放到一个列表中for line in f,append；
5.将列表中的元素和输入的用户名密码进行比较strip,==；
6.如果正确就break
'''
username=input("请输入你要注册的用户名：")
password=input("请输入你要注册的密码：")
print("恭喜你注册成功！")

with open("list_infoo",mode="w",encoding="utf-8") as f:
    f.write("{}\n{}".format(username,password))

lis=[]
i=0
while i<3:
    usn=input("请输入用户名：")
    pwd=input("请输入密码：")
    with open("list_infoo",mode="r+",encoding="utf-8") as f1:
        for line in f1:
            lis.append(line)
    if usn==lis[0].strip() and pwd==lis[1].strip():
        print("登录成功！")
        break
    else:print("登录失败！")
    i+=1