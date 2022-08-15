
space =[]
for i in range(8):
    row =[]
    for j in range(8):
        row.append(0)
    space.append(row)


def edit(name,data):
    file1 = open(name,"a")
    file1.write(data)
    file1.close

def analyse(name):
    content =[]
    for line in open(name,"r").readlines():# reads the lines
        dat = line
        content.append(dat)
    return content

def clear(name):
    file = open(name,"r+")
    file.truncate(0)
    file.close()

clear("playerMove.txt")
edit("playerMove.txt","0")

print(space)
m =0
def place(space,location,player):
    if player ==1:
        value ="R"
    else:
        value ="Y"

    found =False
    row =0
    error =False
    while found ==False:
        try:
            slot =space[row][location]
        except:
            pass
        if row ==8:
            found =True
            error =True
        elif slot ==0:
            space[row][location] =value
            val =[row,location]
            found =True
        else:
            row =row+1
    if error ==True:
        return "N","N"
    else:
        #print(val,"<----")
        return space,val
        
def check(space):
    #rows
    for i in range(8):
        complete =0
        previous ="N"
        for j in range(8):
            if space[j][i] ==previous and space[j][i] !=0:
                complete =complete+1
            else:
                complete =1
            
            if complete >3:
                return space[j][i]
            previous =space[j][i]
    #columns
    j=0
    i=0    
    for j in range(0,8):
        #print(j)
        complete =0
        previous ="N"
        for i in range(0,8):
            #print(space[j][i],previous)
            if space[j][i] ==previous and space[j][i] !=0:
                complete =complete+1
            else:
                complete =1
            previous =space[j][i]
            if complete >3:
                return space[j][i]
    #diagonals
    for c in range(-7,7):
        previous ="N"
        complete =0
        #print("@@@@@")
        struc =[]
        for x in range(8):
            try:
                y =x+c
                struc.append(space[x][y])
                #print("done")
                if previous ==space[x][y]and space[x][y] !=0:
                    complete=complete+1
                else:
                    complete =0
                previous =space[x][y]
                if complete >2:
                    #print("success")
                    return space[x][y]
            except:
                pass
        #print(struc)
            
    for c in range(-7,7):
        previous ="N"
        complete =0
        #print("@@@@@")
        struc =[]
        for x in range(8):
            try:
                y =-1*x+c
                struc.append(space[x][y])
                #print("done")
                if previous ==space[x][y]and space[x][y] !=0:
                    complete=complete+1
                else:
                    complete =0
                previous =space[x][y]
                if complete >2:
                    #print("success")
                    return space[x][y]
            except:
                pass
        #print(struc)  
    return "N"

a=""
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
root =Tk()
for i in range(8):
    for j in range(8):
        Label(root,text="",width=3,background="white").grid(row=i,column=j)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    

def move(line,space,m):
    m =(analyse("playerMove.txt"))
    m=int(m[0])
    print(m)
    clear("playerMove.txt")
    if m%2 ==0:
        play =1
    else:
        play =2
        
    m=m+1
    edit("playerMove.txt",str(m))
    print(m*10)
    grid2 = place(space,line-1,play)
    if grid2[0] =="N":
        print("column is full")
    else:
        space =grid2[0]
        for i in space:
            print(i)
    print(grid2[1])
    try:
        if m%2 !=0:
            Label(root,text="",width=3,background="red").grid(row=(7-grid2[1][0]),column=grid2[1][1])
        else:
            Label(root,text="",width=3,background="yellow").grid(row=(7-grid2[1][0]),column=grid2[1][1])

    except:
        print("line is full")
    a =check(space)
    if a !="N":
        if a =="Y":
            message = ("Yellow is the winner")
        else:
            message = ("Red is the winner")

        popupmsg(message)


b1 =Button(text="1",width=3,command =lambda: move(1,space,m)).grid(row=8,column=0)
b2 =Button(text="2",width=3,command =lambda: move(2,space,m)).grid(row=8,column=1)
b3 =Button(text="3",width=3,command =lambda: move(3,space,m)).grid(row=8,column=2)
b4 =Button(text="4",width=3,command =lambda: move(4,space,m)).grid(row=8,column=3)
b5 =Button(text="5",width=3,command =lambda: move(5,space,m)).grid(row=8,column=4)
b6 =Button(text="6",width=3,command =lambda: move(6,space,m)).grid(row=8,column=5)
b7 =Button(text="7",width=3,command =lambda: move(7,space,m)).grid(row=8,column=6)
b8 =Button(text="8",width=3,command =lambda: move(8,space,m)).grid(row=8,column=7)
root.mainloop()

    

