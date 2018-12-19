import random
from tkinter import Frame, Label, Button
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
            self.hellolabel=Label(self, text='Waiting',font=(20),width=20,height=2)
            self.hellolabel.grid()
            self.rollbutton = Button(self, text='Roll!', width=10, height=1, command=lambda:self.hellolabel.config(text=self.randomselect()))
            self.rollbutton.grid(sticky='s')

    def randomselect(self):
        a = random.randint(0, 99)
        b = a % 5
        if b == 0:
            return '李杨'
        elif b == 1:
            return '李洋'
        elif b == 2:
            return '黄磊'
        elif b == 3:
            return '文波'
        elif b == 4:
            return '陈思'


if __name__ == "__main__":
    nameselect=Application()
    nameselect.master.title('Roll a Dice!')
    nameselect
    nameselect.mainloop()

