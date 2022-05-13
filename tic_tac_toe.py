from tkinter import *
from tkinter import messagebox
import random as r
import pyglet
pyglet.font.add_file('Fonts/WhaleITriedRegular-xWq0.ttf')
pyglet.font.add_file('Fonts/Amilya.ttf')
#########################################################################
############################ MiniMax Section ############################
#########################################################################
# user = 'O'
# me = 'X'
board = [[' ' for i in range(3)], [' ' for i in range(3)], [' ' for i in range(3)]]

def minimax(board, is_max, me, user):
    # check the board
    state = is_end(board)
    if state == 1:
        # print('1')
        return state
    elif state == -1:
        # print(-1)
        return state
    
    if is_draw(board):
        return 0
    
    if is_max:
        # print('here')
        # set best to infinite
        top = -1000
        # walk through in every empty cell
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = me
                    top = max(top, minimax(board, not is_max, me, user))
                    # undo the change
                    board[i][j] = " "
        return top
        
    else:
        # set best to infinite
        # print('there')
        top = 1000
        # walk through in every empty cell
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = user
                    top = min(top, minimax(board, not is_max, me, user))
                    # undo the change
                    board[i][j] = " "
        return top


def is_end(board):
    for r in range(3) :    
        if (board[r][0] == board[r][1] and board[r][1] == board[r][2]) and board[r][0] == " ":       
            if (board[r][0] == me):
                return 1
            elif (board[r][0] == user):
                return -1
 
    for col in range(3) :
      
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) and board[0][col] == " ":
         
            if (board[0][col] == me):
                return 1
            elif (board[0][col] == user):
                return -1
 
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[2][2] == " ":
     
        if (board[0][0] == me):
            return 1
        elif (board[0][0] == user):
            return -1
 
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[0][2] == " ":
     
        if (board[0][2] == me):
            return 1
        elif (board[0][2] == user):
            return -1
        
#########################################################################

def is_draw(board):
    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == ' ') :
                return False
    return True

def best_move(board):
    # just define these values, do use them later
    best_move_score = -1000
    # theres no cell like that, we set it just to define it
    best_move_cell = (-100, -100)
    
    # now we are gonna see if we fill a empty cell, what value minimax gives us
    # we try minimax for every empty cell and fill the one with the best minimax score
    for i in range(3):
        for k in range(3):
            if board[i][k] == " ":
                board[i][k] = me
                score = minimax(board, False, me, user)
                print(score, f'for {i} {k}')
                # undo the change
                board[i][k] = " "
                # print('here is the board', board)
                
                if score > best_move_score:
                    best_move_cell = (i, k)
                    print(best_move_cell)
                    best_move_score = score
                    
    print(best_move_cell)
    return best_move_cell, best_move_score



def button(frame):
    b=Button(frame,padx=1,bg="#560bad",width=3,text="   ",font=('Whale I Tried',60,'bold'),relief="sunken",bd=10)
    return b
def change_turn():
    global a
    for i in ['O','X']:
        if i!=a:
            a=i
            break
    if a == me:
        cell, score = best_move(board)
        click(cell[0], cell[1])
def reset():
    global a, board, me, user
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
    user = a
    me = 'X' if a != 'X' else 'O'
    board = [[' ' for i in range(3)], [' ' for i in range(3)], [' ' for i in range(3)]]
def check():
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
                    return False
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset() 
        return False
        
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
        return False
        
def click(row,col):
        print(row, col)
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        board[row][col] = a
        state = check()
        if state == None:
            change_turn()
            label.config(text=a+"'s Chance")
###############   Main Program #################
root=Tk()
root.resizable(0,0)
root.config(bg='#f72585')
root.title("Tic-Tac-Toe")
a=r.choice(['O','X']) 
user = a
me = 'X' if a != 'X' else 'O'
colour={'O':"#FF6700",'X':"#4cc9f0"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text="Your Chance",font=('Amilya',20,'bold'),fg='#06d6a0',bg='#f72585')
label.grid(row=3,column=0,columnspan=3)

root.mainloop()