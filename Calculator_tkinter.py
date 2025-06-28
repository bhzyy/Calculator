import tkinter

class Program(tkinter.Tk):
    operation=['/','*','-','+']
    counter_dot=0
    def add_char(self,text):
        result_box=self.textbox_show.get()
        if text in self.operation and len(result_box)==0:
            print("You cant put operation.")
            return
        if text!='.':
            if text in self.operation and result_box[len(result_box)-1] not in self.operation:
                self.textbox_show.insert(tkinter.END,text)
                self.textbox_show.icursor(tkinter.END)
                self.textbox_show.xview(tkinter.END)
                self.counter_dot=0
                return
            if text not in self.operation:
                self.textbox_show.insert(tkinter.END,text)
                self.textbox_show.icursor(tkinter.END)
                self.textbox_show.xview(tkinter.END)
                
        elif text=='.' and self.counter_dot==0 and result_box[len(result_box)-1] not in self.operation:
            self.textbox_show.insert(tkinter.END,text)
            self.textbox_show.icursor(tkinter.END)
            self.textbox_show.xview(tkinter.END)
            self.counter_dot+=1
            return

    def clear_content(self):
        self.textbox_show.delete(0,tkinter.END)
        self.textbox_show.focus_set()

    def calculate(self):
        exp=self.textbox_show.get()
        if  exp:
            result=eval(exp)
            self.clear_content()
            self.textbox_show.insert(0,result)
        else:
            print("There isn't anything to calculate.")

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Calculator")
        self.iconbitmap('Calculator_41154.ico')
        self.geometry("326x382-100+100")
        self.resizable(False,False)
        self.config(bg="black")

    def create_widgets(self):
        self.textbox_show=tkinter.Entry(self,border=0,relief="solid",width=10,bg="#000000",font=("san-serif",40),fg="#fff")
        self.button_C=tkinter.Button(self,text="C",width="32",bg="#555",activebackground="#444",activeforeground="#fff",fg="#fff",border=0,font=("san-serif",12,"bold"),height=2,command=self.clear_content)
        self.button_1=tkinter.Button(self,text='1',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('1'))
        self.button_2=tkinter.Button(self,text='2',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('2'))
        self.button_3=tkinter.Button(self,text='3',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('3'))
        self.button_plus=tkinter.Button(self,text='+',width='1',bg="#fc9403",activebackground="#935806",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('+'))
        self.button_4=tkinter.Button(self,text='4',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('4'))
        self.button_5=tkinter.Button(self,text='5',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('5'))
        self.button_6=tkinter.Button(self,text='6',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('6'))
        self.button_dif=tkinter.Button(self,text='-',width='1',bg="#fc9403",activebackground="#935806",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('-'))
        self.button_7=tkinter.Button(self,text='7',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('7'))
        self.button_8=tkinter.Button(self,text='8',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('8'))
        self.button_9=tkinter.Button(self,text='9',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('9'))
        self.button_mul=tkinter.Button(self,text='*',width='1',bg="#fc9403",activebackground="#935806",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('*'))        
        self.button_0=tkinter.Button(self,text='0',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('0'))
        self.button_dot=tkinter.Button(self,text='.',width='1',bg="#333",activebackground="#222",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('.'))
        self.button_equal=tkinter.Button(self,text='=',width='1',bg="#fc9403",activebackground="#935806",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.calculate())        
        self.button_tagh=tkinter.Button(self,text='/',width='1',bg="#fc9403",activebackground="#935806",activeforeground="#fff",fg="#fff",font=("san-serif",12,"bold"),border=0,height=3,command=lambda:self.add_char('/'))        

    def geo_widgets(self):
        self.textbox_show.grid(row=0, column=0, columnspan=4, sticky="ew")
        self.button_C.grid(row=1, column=0, columnspan=4, sticky="ew")
        self.button_1.grid(row=2,column=0,sticky="ew",padx=(1,0))
        self.button_2.grid(row=2,column=1,sticky="ew",padx=(1,0))
        self.button_3.grid(row=2,column=2,sticky="ew",padx=(1,0))
        self.button_plus.grid(row=2,column=3,sticky="ew",pady=(1,1),padx=(1,0))
        self.button_4.grid(row=3,column=0,sticky="ew",padx=(1,0))
        self.button_5.grid(row=3,column=1,sticky="ew",padx=(1,0))
        self.button_6.grid(row=3,column=2,sticky="ew",padx=(1,0))
        self.button_dif.grid(row=3,column=3,sticky="ew",pady=(0,1),padx=(1,0))
        self.button_7.grid(row=4,column=0,sticky="ew",padx=(1,0))
        self.button_8.grid(row=4,column=1,sticky="ew",padx=(1,0))
        self.button_9.grid(row=4,column=2,sticky="ew",padx=(1,0),pady=(0,1))
        self.button_mul.grid(row=4,column=3,sticky="ew",pady=(0,1),padx=(1,0))
        self.button_0.grid(row=5,column=0,sticky="ew",padx=(1,0))
        self.button_dot.grid(row=5,column=1,sticky="ew",padx=(1,0))
        self.button_equal.grid(row=5,column=2,sticky="ew",padx=(1,0))
        self.button_tagh.grid(row=5,column=3,sticky="ew",padx=(1,0))

    def show_program(self):
        self.mainloop()

Window=Program()
Window.create_widgets()
Window.geo_widgets()
Window.show_program()
