#coding = <utf-8>
from menuFrame import MenuFrame
from textFrame import TextFrame
import tkinter

win = tkinter.Tk()
win.title('text')
listR=['撤销','复制','粘贴','全选']
text1 = TextFrame(win,listR)
menu = MenuFrame(win,text1)
dict1 = {'文件(F)':['新建(N)','打开(O)','保存(s)','另存为(A)','页面设置'],'编辑(E)':['撤销','剪切','复制','粘贴'],'格式(O)':['自动换行(W)','字体(F)'],'查看(V)':['状态栏'],'帮助(H)':['查看帮助','关于记事本']}

menu.addCascade('文件(F)',dict1['文件(F)'])
menu.addCascade('编辑(E)',dict1['编辑(E)'])
menu.addCascade('格式(O)',dict1['格式(O)'])
menu.addCascade('查看(V)',dict1['查看(V)'])
menu.addCascade('帮助(H)',dict1['帮助(H)'])

#text.rightClick([1,2,3,4,5])
win.mainloop()