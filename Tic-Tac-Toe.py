import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
import datetime
import os
tr1=['']
tr2=['']
win=None

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        self.player1_name=""
        self.player2_name=""      

        for F in (StartPage,InputPage,HistoryPage,GamePage):
            frame = F(container,self)
            self.frames[F] =frame
            frame.grid(row=0,column=0,sticky="nsew")
        
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        if cont==HistoryPage:
            frame.load_history()
        if cont == GamePage:
            frame.update_label()
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller

        self.bg_path=PhotoImage(file="MBG.png")
        label_bg=Label(self,image=self.bg_path)
        label_bg.place(relheight=1,relwidth=1)

        label1=Label(self,text="Developed By Team_15 \u00A9 2024",font=("Verdanta",13),bg="#88cffa")
        label1.pack(side=BOTTOM)
        
        button1=Button(self,text="NEW GAME",command=lambda:controller.show_frame(InputPage),font=("Helvetica",27),bg="green",fg="white",relief="solid")
        button1.place(x=675,y=675)
        
        button2=Button(self,text="HISTORY",command=lambda:controller.show_frame(HistoryPage),font=("Helvetica",27),bg="gray",fg="white",relief="solid")
        button2.place(x=1000,y=675)

        button3=Button(self,text="EXIT",command=exit,font=("Helvetica",27),bg="red",fg="white",relief="solid")
        button3.place(x=480,y=675)

class InputPage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller

        self.bg_path=PhotoImage(file="MBG.png")
        label_bg=Label(self,image=self.bg_path)
        label_bg.place(relheight=1,relwidth=1)

        label=Label(self,text="Players Names",font=("Helvitica",30),bg="#88cffa")
        label.pack(pady=10)

        label1=Label(self,text="Player-1(X)",font=("Helvitica",20),bg="black",fg="white")
        label1.pack(pady=(10,0))
        self.entry1=Entry(self,font=("Helvetica",15))
        self.entry1.pack()
        label2=Label(self,text="Player-2(O)",font=("Helvitica",20),bg="black",fg="white")
        label2.pack(pady=(90,0))
        self.entry2=Entry(self,font=("Helvetica",15))
        self.entry2.pack(pady=(0,70))

        button1=Button(self, text="Next", command=self.save_and_next,font=("Helvetica",25),bg="green",fg="white",relief="solid")
        button1.place(x=1000,y=675)

        button2=Button(self, text="Back", command=lambda: controller.show_frame(StartPage),font=("Helvetica",25),bg="red",fg="white",relief="solid")
        button2.place(x=480,y=675)

    def save_and_next(self):
        tr1[0]=self.entry1.get()
        tr2[0]=self.entry2.get()
        self.controller.show_frame(GamePage)

class HistoryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller=controller

        bg=Label(self,text="",bg="#88cffa")
        bg.place(relheight=1,relwidth=1)

        label=Label(self,text="History",font=("Helvetica",20),bg="#88cffa")
        label.pack(pady=10)

        self.history_manager=HistoryManager()
        self.history_listbox=Listbox(self,font=("Helvetica",15),width=90,height=30)
        self.history_listbox.pack(pady=10)

        self.load_history()
        
        button=Button(self,text="Back",command=lambda:controller.show_frame(StartPage),font=("Helvetica",17),bg="red",fg="white",relief="solid")
        button.pack()

    def load_history(self):
        self.history_listbox.delete(0,tk.END)
        self.history_manager.load_history()
        history=self.history_manager.get_history()
        for entry in history:
            self.history_listbox.insert(tk.END, f"{entry[0]}    {entry[1]}    {entry[2]}")
        

class GamePage(tk.Frame):
    def update_label(self):
        self.label.config(text=f"{tr1[0]} vs {tr2[0]}")

    def update_turn_label(self):
            current_player = "Player-1(X)" if turn == "X" else "Player-2(O)"
            self.turn_label.config(text=f"Current Turn: {current_player}")

    def game_logic(self):
        def check(clicked):
            global turn, count, visited, b

            count+=1
            visited[clicked]=turn
            if b[clicked].cget('text')=="":
                b[clicked].configure(text=turn,font=("Helvetica",9),fg="red",state=DISABLED)
                self.update_turn_label()
                turn = "O" if turn == "X" else "X" 
                self.update_turn_label()


            if count>2:
                checkPattern()

        def checkPattern():
            global turn, count
            ans=[[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

            flag=0
            for i in ans:
                temp = i
                a1=temp[0]
                a2=temp[1]
                a3=temp[2]

                if visited[a1]!= "" and visited[a1] == visited[a2] and visited[a2] == visited[a3]:
                    turn="O" if turn=="X" else "X"
                    flag=1
                    break

            global win
            if flag==1:
                if turn=="X":
                        winner=tr1[0]
                        self.history_manager.save_result(f"{tr1[0]} vs {tr2[0]}", winner)
                        messagebox.showinfo(f"{winner}"+" Won", "Game Over")
                elif turn=="O":
                        winner=tr2[0]
                        self.history_manager.save_result(f"{tr1[0]} vs {tr2[0]}",winner)
                        messagebox.showinfo(f"{winner}"+" Won","Game Over")
                win.destroy()
                self.controller.show_frame(InputPage)
            elif count == 9:
                messagebox.showinfo("None Won", "Restart the Game")
                win.destroy()
                game()

        def game():
            global b, turn, count, visited, win

            win=Tk()
            win.title("GAME")
            win.resizable(False, False)
            win.geometry("450x350+480+180")

            b=[None for i in range(9)]
            turn="X"
            count=0
            visited=["" for i in range(9)]

            b[0]=Button(win,text = '',height = 7, width = 20, command = lambda: check(0),bg="black",disabledforeground="white")
            b[1]=Button(win,text = '',height = 7, width = 20, command = lambda: check(1),bg="black",disabledforeground="white")
            b[2]=Button(win,text = '',height = 7, width = 20, command = lambda: check(2),bg="black",disabledforeground="white")
            b[3]=Button(win,text = '',height = 7, width = 20, command = lambda: check(3),bg="black",disabledforeground="white")
            b[4]=Button(win,text = '',height = 7, width = 20, command = lambda: check(4),bg="black",disabledforeground="white")
            b[5]=Button(win,text = '',height = 7, width = 20, command = lambda: check(5),bg="black",disabledforeground="white")
            b[6]=Button(win,text = '',height = 7, width = 20, command = lambda: check(6),bg="black",disabledforeground="white")
            b[7]=Button(win,text = '',height = 7, width = 20, command = lambda: check(7),bg="black",disabledforeground="white")
            b[8]=Button(win,text = '',height = 7, width = 20, command = lambda: check(8),bg="black",disabledforeground="white")

            b[0].grid(row = 0, column = 0)
            b[1].grid(row = 0, column = 1)
            b[2].grid(row = 0, column = 2)
            b[3].grid(row = 1, column = 0)
            b[4].grid(row = 1, column = 1)
            b[5].grid(row = 1, column = 2)
            b[6].grid(row = 2, column = 0)
            b[7].grid(row = 2, column = 1)
            b[8].grid(row = 2, column = 2)

            win.mainloop()    

        game()

    def restart(self):
        self.controller.show_frame(InputPage)
        if win==None:
            pass
        else:
            win.destroy()
        
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        self.history_manager=HistoryManager()
        self.bg_path=PhotoImage(file="MBG.png")
        label_bg=Label(self,image=self.bg_path)
        label_bg.place(relheight=1,relwidth=1)

        self.label=Label(self,text=f"{tr1[0]} vs {tr2[0]}",font=("Helvetica",18),bg="black",fg="white")
        self.label.pack(pady=10)

        button=Button(self,text="Restart (or Back)",command=self.restart,font=("Helvetica",15),bg="red",fg="white",relief="solid")
        button.pack(pady=20)

        button=Button(self,text="START",command=self.game_logic,font=("Helvetica",17),bg="green",fg="white",relief="solid")
        button.pack(pady=(50,0))

        self.turn_label = Label(self, text="Current Turn: Player-1(X)",font=("Verdanta",23),bg="dodgerblue",fg="red")
        self.turn_label.pack(side=BOTTOM,pady=150)

class HistoryManager:
    def __init__(self, filename="History.csv"):
        self.filename = filename
        self.history = []
        self.load_history()

    def save_result(self, player, winner):
        date =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append((player,winner,date))
        with open(self.filename, mode='a', newline='') as file:
            writer=csv.writer(file)
            writer.writerow([player+"       Won by ",winner+"          Date&Time:",date])

    def load_history(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                self.history = list(reader)

    def get_history(self):
        return self.history

app=App()
app.title("TIC-TAC-TOE")
app.state("zoomed")
app.mainloop()


