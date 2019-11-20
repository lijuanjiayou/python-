#绝对路径
# f=open("D:\python 9th\练习\诗歌.txt",mode="r",encoding="GB2312")
# content=f.read()
# print(content)
# f.close()

#相对路径
# f=open("恋爱课堂",mode="r",encoding="utf-8")
# content=f.read()
# print(content)
# f.close()

# f=open("恋爱课堂",mode="rb")
# content=f.read()
# print(content)
# f.close()

# 只写
# f=open("log",mode="wb")
# f.write("诗歌散文戏曲".encode("utf-8"))
# f.close()

# 追加
# f=open("log",mode="a",encoding="utf-8")
# f.write("这是诗歌")
# f.close()

# f=open("log",mode="ab")
# f.write("  这不是诗歌吧".encode("utf-8"))
# f.close()

# 读写
# f=open("log",mode="r+",encoding="utf-8")
# print(f.read())
# f.write("这样学习有效果吗")
# f.close()

# 写读(看光标，写覆盖写入，剩余的读出来）
# f=open("log",mode="r+",encoding="utf-8")
# f.write("abc")
# print(f.read())
# f.close()

# f=open("log",mode="r+b")
# f.write("abc".encode("utf-8"))
# print(f.read())
# f.close()

# w+需要调光标f.seek(0）
# f=open("log",mode="w+",encoding="utf-8")
# f.write("mmmm")
# f.seek(0)
# print(f.read())
# f.close()

# f=open("log",mode="r+",encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

with open("log",mode="r+",encoding="utf-8") as f1,open("log",mode="r+",encoding="utf-8") as f2:
    print(obj.read())