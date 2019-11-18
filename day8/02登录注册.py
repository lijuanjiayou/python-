# 输入用户名和密码
username=input("请输入用户名:")
password=input("请输入密码:")

# 将用户名和密码放到一个文件中
with open("info",mode="w",encoding="utf-8") as f:
    f.write("{}\n{}".format(username,password))
print("恭喜您，注册成功！")
# 用户名和密码验证
list=[]
i=0
while i < 3:
    usn=input("请输入你需要验证的用户名:")
    pwd=input("请输入你需要验证的密码:")
    # 打开文件列表进行比较
    with open("info",mode="r+",encoding="utf-8") as f1:
        for line in f1:
            list.append(line)
    if usn==list[0].strip() and pwd==list[1].strip():
        print("登陆成功！")
        break
    else:print("登录失败！")
    i+=1
