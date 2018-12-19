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
            self.nameInput = Entry(self, width=20)
            self.nameInput.grid()

    def roll(self):
            self.rollbutton = Button(self, text='Roll!', width=10, height=1,activeforeground='red',
                                     activebackground='blue',
                                     command=self.hello)
            self.rollbutton.grid(sticky='s')

    def hello(self):
        names = self.nameInput.get()
        listed = list(x for x in names.split(sep= '，'))
        self.choosed = self.randomselect(listed)
        name = self.choosed or 'You input nothing!'
        messagebox.showinfo(message=name)

    def randomselect(self, nlist):
        a = random.randint(0, len(nlist)-1)
        b = nlist[a]
        return b

if __name__ == "__main__":
    nameselect=Application()
    nameselect.master.title('Roll a Dice!')
    nameselect.mainloop()

