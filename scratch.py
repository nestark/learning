import wmi
import socket
import win32clipboard
from tkinter import *
mess=[]

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self,*info):
        for a in info:
            self.hellolabel = Label(self, text=a)
            self.hellolabel.grid()
            mess.append(a)

    def send_to_clibboard(self):
        sent=''
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        for b in mess:
            sent+=b+'\n'
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, sent)
        win32clipboard.CloseClipboard()

    def creatButton(self):
        self.okButton = Button(self, text='OK', command=self.quit)
        self.okButton.grid()
        self.copybutton= Button(self, text='复制', command=self.send_to_clibboard)
        self.copybutton.grid()


def sys_version(option):
    c = wmi.WMI ()
    #获取操作系统版本
    for sys in c.Win32_OperatingSystem():
        sysver="系统版本:%s" %sys.Caption+' '+"版本号:%s" %sys.Version#系统版本及版本号
        compname="计算机名:%s" %sys.CSname#计算机名
    for cs in c.Win32_ComputerSystem():
        username="用户名:%s" %cs.Username#用户账号名
    '''for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        for ip_address in interface.IPAddress[0]:
            ip=ip_address
            print(ip)'''
    ip="IP地址:%s" %socket.gethostbyname(sys.CSname) #用计算机名获取IP地址
    if option=='sysver':
        return sysver
    elif option=='copname':
        return compname
    elif option=='username':
        return username
    elif option=='ip':
        return ip


version=sys_version('sysver')
hostname=sys_version('copname')
usern=sys_version('username')
ipad=sys_version('ip')
app=Application()
app.createWidgets(version, hostname, usern, ipad)
app.master.title('Help Info')
app.creatButton()
# 主消息循环:
app.mainloop()

