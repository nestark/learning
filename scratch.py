import wmi
import sys
import os
from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self,*info):
        for i in info:
            self.helloLabel = Label(self,text=i)
            self.helloLabel.grid()

    def creatButton(self):
        self.okButton = Button(self, text='OK', command=self.quit)
        self.okButton.grid()
def sys_version(option):
    c = wmi.WMI ()
    #获取操作系统版本
    for sys in c.Win32_OperatingSystem():
        sysver="Version:%s" %sys.Caption+"Vernum:%s" %sys.Version
        compname=sys.CSname#计算机名
    for cs in c.Win32_ComputerSystem():
        username=cs.Username
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        mac=interface.MACAddress
    for ip_address in interface.IPAddress:
        ip=ip_address
        print(ip)
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
app.createWidgets(version,hostname,usern,ipad)
app.master.title('Help Info')
app.creatButton()
# 主消息循环:
app.mainloop()

