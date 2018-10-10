import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from textFrame import TextFrame
class MenuFrame(tkinter.Frame):
    def __init__(self,master,otherWin):
        self.otherWin = otherWin
        self.frame = tkinter.Frame(master)
        self.frame.pack(side=tkinter.TOP)
        self.menubar = tkinter.Menu()
        master.config(menu=self.menubar)
        #添加control+n的快捷方式
        master.bind('<Control-n>',self.createFile)
        #添加control+o的快捷方式
        master.bind('<Control-o>',self.openFile)

        master.bind('<Control-s>',self.saveFile)

        master.bind('<Control-a>',self.saveAsFile)
    def saveAsFile(self,event):
        print('文件另存为')
    def saveFile(self,event):
        path = askopenfilename()
        with open(path,'w',encoding='gbk') as f:
            t2 = self.otherWin.txt.get(0.0, tkinter.END)
            f.write(t2)


        print('文件已保存')
    def createFile(self,event):
        print('新建了一个新的文件')

    def openFile(self, event):
        path = askopenfilename()
        with open(path,'r',encoding='gbk') as f:
            str1 = f.read()
            self.otherWin.txt.insert(tkinter.INSERT,str1)

        #print('打开了一个新的文件')
        #cascade = {'cascade1':[cammand1,command2,command3,command4],'cascade2':[cammand1,command2,command3,command4].....}
    # def addCascade(self,cascade):
    #     menu0 = tkinter.Menu(self.menubar, tearoff=False)
    #     key0 = list(cascade.keys())[0]
    #     for va in cascade[key0]:
    #         menu0.add_command(label=va)
    #     self.menubar.add_cascade(label=key0,menu=menu0)

    def addCascade(self,menuName,cascade):
        _menu = tkinter.Menu(self.menubar,tearoff=False)
        for va in cascade:
            _menu.add_command(label=va)
        self.menubar.add_cascade(label=menuName,menu=_menu)






        # for key in cascade.keys():
        #     self.menubar.add_cascade(label=key,menu=menu0)
        #     for va in cascade[key]:
        #         menu0.add_command(label=va)

