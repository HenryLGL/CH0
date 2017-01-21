from tkinter import *


class App:

    def __init__(self):
        self.v = StringVar()
        self.dict = {}
        self.History = [] 
        
        self.frame = Frame(root, width=300, heigh=250)
        self.frame.grid()
        self.label = Label(root, textvariable=self.v, anchor=NW, justify=LEFT)
        self.label.grid(row=0,sticky = W)
        self.buttonHelp = Button(root, text = "Help", fg= "red", command = self.help)
        self.buttonHelp.grid(row=10,column=1)
        self.buttonHistory = Button(root, text = "History", fg = "red", command = self.sethistory)
        self.buttonHistory.grid(row=10, column=2)
        self.buttonQuit = Button(root, text='Quit', fg="red",command=self.frame.quit)
        self.buttonQuit.grid(row=10, column=3)
        self.entry = Entry(root)
        self.entry.grid(row=10, sticky=W)
        self.entry.bind('<Return>', self.Cityweather)
        
        with open('weather1.txt','r+',encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split(',')
                self.dict[key] = value
            
        
        
    def Cityweather(self,event):
        i = self.entry.get()
        if i in self.dict:
            self.v.set("%s的天气是%s" %(i, self.dict[i]))
            self.History.append(tuple((i,self.dict[i])))
        else:
            self.v.set("无查询数据，可按help查看帮助信息")
    
        self.entry.delete(0, END)
    
    def help(self):
        self.v.set( """
    输入城市名并按回车键，即可查询该城市天气
    *仅限县级市以上城市*
    点击help，查看帮助文档
    点击history，查看历史查询记录
    点击quit，退出此应用
    """)
    
    def sethistory(self):
        if len(self.History) == 0:
            self.v.set("无历史查询信息")
        else:
            f = open("history.txt","w+",encoding = "UTF8")
            f.truncate()
            f.write("查询历史：\n\n")
            for h in self.History:
                f.write("%s %s \n" % (h[0],h[1]))
            f.seek(0)
            self.v.set(f.read())
            f.close()
    
   
    
                
root = Tk()
root.title("Weather! Weather!")
weather = App()
root.mainloop()
                



        
        
        
        
        