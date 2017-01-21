#coding:utf-8
dict = {}
with open('weather1.txt','r+',encoding='utf-8') as f:
    for line in f:
        key, value = line.strip().split(',')
        dict[key] = value


big_menu = """
\t* 欢迎来到L_L天文台
\t* 查询天气情况，请输入相应城市名称；
\t* 获取帮助信息，请输入help
\t* 获取历史查询信息，请输入history
\t* 退出程序，请输入quit
"""

print(big_menu)    
    
history = []
while True:
    i = input("请输入城市的名称或其他指令:")
    if i == "help":
        print("""
		请输入城市名，查询当前天气状况；
		如您需要帮助，请输入help获取帮助文档；
		如您需要浏览历史纪录，请输入history获取相应信息；
		如您需要关闭程序，请输入quit。
		""")
    elif i == "quit":
        print ("欢迎下次使用")
        break
    elif i == "history":
        if len(history) == 0: 
            print ("没有历史查询信息") 
        for h in history:
            print (h[0],h[1])
    elif i in dict:
        history.append(tuple((i,dict[i])))
        print ("%s的天气状况是: %s" %(i ,dict[i]))
    else:
        print("未找到相关信息，可输入help获得帮助")