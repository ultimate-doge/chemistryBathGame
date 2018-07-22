from tkinter import *
import webbrowser
class lvl1:
    def __init__(self):
        self.lvl_cnt=1
        self.main = Tk()
        self.main.title('化学澡堂')
        self.main.geometry('700x600')
        self.main.resizable(0, 0)
        self.menu=Menu(self.main)
        self.main.config(menu=self.menu)
        self.fileMenu = Menu(self.menu)
        self.menu.add_cascade(menu=self.fileMenu,label='方程式')
        self.title = Button(self.main, text='化学澡堂', font='Times 40 bold',command=self.sponsor)
        self.title.pack()
        self.kohler=False
        self.equation=[True,True,True,True,True,True,True]
        self.pac7 = PhotoImage(file="thumb.gif").subsample(2, 2)
        self.start = Button(self.main, image=self.pac7, command=self.tart)
        self.start.pack()
        self.main.mainloop()
    def sponsor(self):
        if self.kohler:
            webbrowser.open('https://www.hackshanghai.com/')
        self.start.destroy()
        self.kohler=True
        self.title['text']='Kohler+Hack='
        self.pac7 = PhotoImage(file="kohler.gif").subsample(2, 2)
        self.start = Button(self.main, image=self.pac7, command=self.tart)
        self.start.pack()
        webbrowser.open('')
    def tart(self):
        self.title.pack_forget()
        self.start.pack_forget()
        self.stuff = Frame(self.main,bg="white")
        self.stuff.propagate(0)
        self.stuff.pack(fill=BOTH,expand=1)
        self.level=Label(self.stuff,text="Level 1",font="MS 20",bg="white")
        self.level.pack(side=TOP)
        self.state="Ba(OH)2"
        self.pac = PhotoImage(file=self.state+'.gif')
        self.pac = self.pac.subsample(2, 2)
        self.pic = Label(self.stuff, image=self.pac)
        self.pic.pack()
        self.desc = Label(self.stuff, text="这是氢氧化钡，你要让它泡完澡后不会消失哦",font="MS 18",bg='white')
        self.desc.pack(side=BOTTOM)
        self.pac2=PhotoImage(file="H2CO3.gif")
        self.pac2=self.pac2.subsample(3,3)
        self.choice1=Button(self.stuff,text='碳酸',image=self.pac2,command=self.ch1,bg="white")
        self.choice1.pack(side=LEFT)
        self.pac3 = PhotoImage(file="H2SO4.gif")
        self.pac3 = self.pac3.subsample(3, 3)
        self.choice2 = Button(self.stuff, text='硫酸', image=self.pac3, command=self.ch2, bg="white")
        self.choice2.pack(side=RIGHT)
    def ch1(self):
        self.choice1.pack_forget()
        self.desc['text'] = "现在他是碳酸钡，你还是要保证它泡完澡后不会消失哦"
        if self.equation[0]:
            self.equation[0]=False
            self.fileMenu.add_command(label='Ba(OH)2+H2CO3→BaCO3↓+2H2O')
            self.desc['text'] = "现在他是碳酸钡，你还是要保证它泡完澡后不会消失哦\n你获得了一个新的方程式：Ba(OH)2+H2CO3→BaCO3↓+2H2O"
        self.state = "BaCO3"
        self.pic.destroy()
        self.pac4 = PhotoImage(file=self.state + '.gif')
        self.pac4 = self.pac4.subsample(1, 1)
        self.pic = Label(self.stuff, image=self.pac4)
        self.pic.pack(side=LEFT)
        self.pac5 = PhotoImage(file='HCL.gif')
        self.pac5 = self.pac5.subsample(3, 3)
        self.choice3 = Button(self.stuff, image=self.pac5, command=self.ch3)
        self.choice3.pack(side=BOTTOM)
        self.choice2.pack_forget()
    def ch2(self):
        self.desc['text'] = "现在他是硫酸钡，你还是要保证它泡完澡后不会消失哦"
        self.choice1.pack_forget()
        if self.equation[1]:
            self.equation[1]=False
            self.fileMenu.add_command(label='Ba(OH)2+H2SO4→+2H2)')
            self.desc['text'] = "现在他是硫酸钡，你还是要保证它泡完澡后不会消失哦\n你获得了一个新的方程式：Ba(OH)2+H2SO4→+2H2)"
        self.state = "BaSO4"
        self.pic.destroy()
        self.pac4=PhotoImage(file=self.state+'.gif')
        self.pac4=self.pac4.subsample(1,1)
        self.pic=Label(self.stuff,image=self.pac4,bg='white')
        self.pic.pack(side=LEFT)
        self.pac5=PhotoImage(file='HCL.gif')
        self.pac5=self.pac5.subsample(3,3)
        self.choice3 = Button(self.stuff, image=self.pac5, command=self.ch3,bg='white')
        self.choice3.pack(side=BOTTOM)
        self.choice2.pack_forget()
    def ch3(self):
        if self.state=="BaCO3":
            self.choice3.pack_forget()
            self.desc.pack_forget()
            self.pic.destroy()
            self.status="level1lose"
        else:
            self.choice3.pack_forget()
            self.desc.pack_forget()
            self.pic.destroy()
            self.status = "level1win"
        self.pac6 = PhotoImage(file=self.status + '.gif')
        self.pac6 = self.pac6.subsample(2, 2)
        self.pic = Label(self.stuff, image=self.pac6)
        self.pic.pack()
        self.choice4=Button(self.stuff,text="下一关",command=self.next,font="MS 20")
        if self.state=='BaSO4':
            self.temp=Label(text='',font='MS 18')
            self.temp.pack()
        elif self.state=='BaCO3':
            self.choice4['text']='重新开始'
            if self.equation[1]:
                self.equation[1] = False
                self.fileMenu.add_command(label='Ba(OH)2+H2SO4→+2H2)')
                self.temp = Label(text="你获得了一个新的方程式：Ba(OH)2+H2SO4→+2H2)",font='MS 18')
                self.temp.pack()
        self.choice4.pack(side=BOTTOM)
    def next(self):
        self.choice4.pack_forget()
        self.pic.destroy()
        if self.state=='BaCO3':
            self.level.pack_forget()
            self.choice4.pack_forget()
            self.level = Label(self.stuff, text="Level 1", font="MS 20", bg="white")
            self.level.pack(side=TOP)
            self.state = "Ba(OH)2"
            self.pac = PhotoImage(file=self.state + '.gif')
            self.pac = self.pac.subsample(4, 4)
            self.pic = Label(self.stuff, image=self.pac)
            self.pic.pack()
            self.desc = Label(self.stuff, text="这是氢氧化钡，你要让它泡完澡后不会消失哦", font="MS 18", bg='white')
            self.desc.pack(side=BOTTOM)
            self.pac2 = PhotoImage(file="H2CO3.gif")
            self.pac2 = self.pac2.subsample(3, 3)
            self.choice1 = Button(self.stuff, text='碳酸', image=self.pac2, command=self.ch1, bg="white")
            self.choice1.pack(side=LEFT)
            self.pac3 = PhotoImage(file="H2SO4.gif")
            self.pac3 = self.pac3.subsample(3, 3)
            self.choice2 = Button(self.stuff, text='硫酸', image=self.pac3, command=self.ch2, bg="white")
            self.choice2.pack(side=RIGHT)
        else:
            self.level['text'] = "Level 2"
            self.state = "Fe"
            self.choice2.destroy()
            self.pic.destroy()
            self.desc.pack_forget()
            self.pac = PhotoImage(file=self.state + '.gif').subsample(2,2)
            self.pic = Label(self.stuff, image=self.pac)
            self.pic.pack()
            self.choice1 = Button(self.stuff, image=self.pac5, command=self.ch21)
            self.choice1.pack(side=LEFT)
            self.pac7=PhotoImage('CuSO4.gif').subsample(3,3)
            self.choice2=Button(self.stuff,image=self.pac7,command=self.ch22)
            self.choice2.pack(side=RIGHT)
            self.desc = Label(text="这是铁，你要让它泡完澡后不会溶解哦", font="MS 18")
            self.desc.pack()
    def bath(self):
        pass
    def ch22(self):
        self.pic.pack_forget()
        self.choice2.destroy()
        self.state = "FeSO4"
        self.pac7 = PhotoImage(file=self.state + '.gif').subsample(2, 2)
        self.pic = Label(self.stuff, image=self.pac2)
        self.pic.pack()
        self.pac8 = PhotoImage(file="C2H5OH.gif").subsample(3, 3)
        self.choice2 = Button(self.stuff, text='下一关', command=self.ch22b)
        self.pac9 = PhotoImage(file='level2win.gif')
        self.pic = Label(self.stuff, image=self.pac9)
        self.pic.pack()
        self.choice2.pack()
        if self.equation[4]:
            self.fileMenu.add_command(label='Fe + CuSO4 →FeSO4 + Cu')
            self.temp = Label(text="你获得了一个新的方程式：Fe + CuSO4 →FeSO4 + Cu", font='MS 18')
            self.temp.pack()
            self.equation[4] = False
    def ch21(self):
        self.pic.pack_forget()
        self.choice1.pack_forget()
        self.state="FeCl2"
        self.pac2=PhotoImage(file=self.state+'.gif').subsample(2,2)
        self.pic=Label(self.stuff,image=self.pac2)
        self.pic.pack()
        self.pac3=PhotoImage(file="C2H5OH.gif").subsample(3,3)
        self.choice1=Button(self.stuff,image=self.pac3,command=self.ch21b)
        self.choice1.pack(side=RIGHT)
        if self.equation[3]:
            self.fileMenu.add_command(label='Fe + 2HCl → FeCl2 + H2↑')
            self.temp = Label(text="你获得了一个新的方程式：Fe + 2HCl → FeCl2 + H2↑", font='MS 18')
            self.desc['text']="现在他是氯化铁，你还是要保证它泡完澡后不会消失哦"
            self.temp.pack()
            self.equation[3]=False
    def ch21b(self):
        self.temp.destroy()
        self.pic.destroy()
        self.choice1.destroy()
        self.pac4=PhotoImage(file='level2lose.gif').subsample(2,2)
        self.pic=Label(self.stuff,image=self.pac4)
        self.choice2=Button(text='重新开始',command=self.ch21bb)
        self.pic.pack()
        self.choice2.pack()
        self.desc['text']=''
    def ch21bb(self):
        self.level['text'] = "Level 2"
        self.state = "Fe"
        self.choice2.destroy()
        self.pic.destroy()
        self.desc.pack_forget()
        self.pac = PhotoImage(file=self.state + '.gif').subsample(2,2)
        self.pic = Label(self.stuff, image=self.pac)
        self.pic.pack()
        self.choice1 = Button(self.stuff, image=self.pac5, command=self.ch21)
        self.choice1.pack(side=LEFT)
        self.pac7 = PhotoImage('CuSO4.gif').subsample(3,3)
        self.choice2 = Button(self.stuff, image=self.pac7, command=self.ch22)
        self.choice2.pack(side=RIGHT)
        self.desc = Label(text="这是铁，你要让它泡完澡后不会溶解哦", font="MS 18")
        self.desc.pack()
    def ch22b(self):
        self.pic.destroy()
        self.choice2.destroy()
        self.temp.destroy()
        self.pac8 = PhotoImage(file='construction.gif')
        self.pic = Label(self.stuff, image=self.pac8)
        self.pic.pack()
lvl1()
