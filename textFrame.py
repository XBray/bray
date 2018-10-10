import tkinter
import win32com.client
import re

class TextFrame(tkinter.Frame):
    def __init__(self,master,funcList):
        self.frameDown = tkinter.Frame(master)
        self.frameDown.pack(side=tkinter.TOP)

        self.button = tkinter.Button(self.frameDown, text='为我朗读', command=self.readText)
        self.button.pack()

        self.txt = tkinter.Text(self.frameDown)
        self.txt.pack(side=tkinter.LEFT)
        self.scoll = tkinter.Scrollbar(self.frameDown)
        self.scoll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.scoll.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=self.scoll.set)



        self.menuR = tkinter.Menu(tearoff=False)
        for func in funcList:
            self.menuR.add_command(label=func)
            #不能用self.frameDown.bind
        master.bind('<Button-3>', self.showMenu)
    def readText(self):
        t1 = self.txt.get(0.0,tkinter.END)
        #正则取消标点符号的朗读并停顿
        ret = re.compile(r'''[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'！@#￥……&*（）《》【】]+''')
        t1list = ret.split(t1)
        speaker = win32com.client.Dispatch('SAPI.SpVoice')
        for i in t1list:
            speaker.speak(i)

    # def rightClick(self,funcList):
    #     self.menuR = tkinter.Menu(self.frameDown)
    #     for func in funcList:
    #         self.menuR.add_command(label=func)
    #     self.frameDown.bind('<Button-3>',self.showMenu)
    def showMenu(self,event):
        self.menuR.post(event.x_root,event.y_root)
