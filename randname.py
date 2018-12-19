import random
from tkinter import Frame, Label, Button, messagebox, Entry
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.roll()

    def createWidgets(self):
            self.hellolabel=Label(self, text='Enter names',font=(20),width=20,height=2)
            self.hellolabel.grid()
            self.nameInput = Entry(self, width=20)#创建文本输入框
            self.nameInput.grid()

    def roll(self):
            self.rollbutton = Button(self, text='Roll!', width=10, height=1,activeforeground='red',
                                     activebackground='blue',
                                     command=self.hello)#创建按钮，设定大小和前景色背景色，点击运行hello函数
            self.rollbutton.grid(sticky='s')

    def hello(self):
        """随机选取一个文本框中输入的值，显示在消息框中"""
        names = self.nameInput.get()#获取文本框输入内容
        listed = list(x for x in names.split(sep=' '))#将输入的字符串以空格分割, 如果以空格分割会报错, 需要修改
        self.choosed = self.randomselect(listed)
        name = self.choosed or 'You input nothing!'
        messagebox.showinfo(message=name)

    def randomselect(self, nlist):
        """输入一个列表，返回列表中的一个随机元素"""
        a = random.randint(0, len(nlist)-1)
        b = nlist[a]
        return b

if __name__ == "__main__":
    nameselect=Application()
    nameselect.master.title('Roll a Dice!')
    nameselect.master.geometry('200x200')
    nameselect.master.resizable(width=False,height=False)
    nameselect.mainloop()