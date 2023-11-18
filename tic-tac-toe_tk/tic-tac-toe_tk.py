# Tic Tac Topen
from tkinter import *
import time
import random

def new_game():
    label.config(text = player + " turns", font=("consolas", 20))
    
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col].config(bg="white")

def next_turn(row, col):
    global player
    
    if buttons[row][col]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[row][col]['text'] = player
            winner = check_winner()
            
            if winner is False:
                player = players[1]
                label.config(text=(players[1]+ " turn"))
            elif winner is True:
                label.config(text=(players[0]+ " wins"))
            elif winner == "Tie":
                label.config(text="Tie")  
        else:
            buttons[row][col]['text'] = player
            winner = check_winner()
            
            if winner is False:
                player = players[0]
                label.config(text=(players[0]+ " turn"))
            elif winner is True:
                label.config(text=(players[1]+ " wins"))
            elif winner == "Tie":
                label.config(text="Tie")  

def check_winner():

    color = "green"
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg=color)
            buttons[row][1].config(bg=color)
            buttons[row][2].config(bg=color)
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg=color)
            buttons[1][col].config(bg=color)
            buttons[2][col].config(bg=color)
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg=color)
        buttons[1][1].config(bg=color)
        buttons[2][2].config(bg=color)
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg=color)
        buttons[1][1].config(bg=color)
        buttons[2][0].config(bg=color)
        return True
    elif empty_spaces() is False:

        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
                
        return "Tie"
    else:
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

root = Tk()
root.geometry("420x520")
root.title("Tic-Tac-Toe")

players = ["X", "O"]

player = random.choice(players)

buttons = [[0,0,0],[0,0,0],[0,0,0]]



reset_button = Button(text="New Game", bg="lightblue", font=("consolas", 20), command=new_game)
reset_button.pack(side="top", pady=10)

frame = Frame(root)
frame.pack()
                                            
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", bg="white", font=("consolas", 30), width=5, height=2, command=lambda row=row, column=col: next_turn(row, column))
        buttons[row][col].grid(row=row, column=col)

label = Label(text = player + " turns", font=("consolas", 20))
label.pack()

root.mainloop()