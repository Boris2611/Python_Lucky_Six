from tkinter import *  
import tkinter as tk
import random
root = Tk()
root.geometry('900x400')
root.title("Lucky Six")

tk.Label(root, text="Broj 1: ").grid(row=0)
tk.Label(root, text="Broj 2: ").grid(row=1)
tk.Label(root, text="Broj 3: ").grid(row=2)
tk.Label(root, text="Broj 4: ").grid(row=3)
tk.Label(root, text="Broj 5: ").grid(row=4)
tk.Label(root, text="Broj 6: ").grid(row=5)
tk.Label(root, text="Ulog: ").grid(row=6)

br1 = tk.Entry(root)
br2 = tk.Entry(root)
br3 = tk.Entry(root)
br4 = tk.Entry(root)
br5 = tk.Entry(root)
br6 = tk.Entry(root)
ulog = tk.Entry(root)

br1.grid(row=0, column=1, padx = 20, pady = 0)
br2.grid(row=1, column=1, padx = 20, pady = 0)
br3.grid(row=2, column=1, padx = 20, pady = 0)
br4.grid(row=3, column=1, padx = 20, pady = 0)
br5.grid(row=4, column=1, padx = 20, pady = 0)
br6.grid(row=5, column=1, padx = 20, pady = 0)
ulog.grid(row=6, column=1, padx = 20, pady = 0)

novac = 1000
dobitak = 0

def funkcija():
    global novac, dobitak
    novac = novac - int(ulog.get())
    novac = novac + dobitak
    tk.Label(root, text = "Novac: " + str(novac), width=30, bg= 'yellow').grid(row=13, column=1)
    print("Racunajne")
    #Kvota
    kvota = ["None", "None", "None", "None", "None",
             10000, 7500, 5000, 2500, 1000, 500,
             300, 200, 150, 100, 90, 80, 70, 60,
             50, 40, 30,25, 20, 15, 10, 9, 8, 7,
             6, 5, 4, 3, 2, 1]
    # Random Brojevi
    izlaze = random.sample(range(1, 49), 35)
    # Provera ########
    for broj in range(35):
        if int(br1.get()) == izlaze[broj]:
            izlaze[broj] =  str(izlaze[broj]) + "$"
        elif int(br2.get()) == izlaze[broj]:
            izlaze[broj] =  str(izlaze[broj]) + "$"
        elif int(br3.get()) == izlaze[broj]:
            izlaze[broj] =  str(izlaze[broj]) + "$"
        elif int(br4.get()) == izlaze[broj]:
            izlaze[broj] =  str(izlaze[broj]) + "$"
        elif int(br5.get()) == izlaze[broj]:
            izlaze[broj] =  str(izlaze[broj])  + "$"
        elif int(br6.get()) == izlaze[broj]:
            izlaze[broj] = str(izlaze[broj])  + "$"

    dobitni = []
    dobitnaKvota = []
    for i in range(35):
        if "$" in str(izlaze[i]):
            dobitni.append(izlaze[i])
            dobitnaKvota.append(kvota[i])
    tk.Label(root, text=dobitni, bg='yellow', width=30).grid(row=18, column=1)     
    if len(dobitni) == 6:
        print("WIN")
        tk.Label(root, text="Brojevi su dobitni !", bg='green', width=30).grid(row=15, column=1)
        dobitak = int(ulog.get()) * dobitnaKvota[-1]
        tk.Label(root, text="Dobitak: " + str(dobitak), bg='green', width=30).grid(row=16, column=1)
    else:
        dobitak = 0
        tk.Label(root, text="Brojevi nisu dobitni !", bg='red', width=30).grid(row=15, column=1)
        tk.Label(root, text="Dobitak: 0", bg='red', width=30).grid(row=16, column=1)
                   
    # Printovanje

    for i in range(10):
        if "$" in str(izlaze[i]):
            tk.Label(root, text=str(i+1) + " )", bg='#666600', width=4).grid(row=i, column=2)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#b3b300', width=6).grid(row=i, column=3)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='yellow', width=6).grid(row=i, column=4)
        else:
            tk.Label(root, text=str(i+1) + " )", bg='#777', width=4).grid(row=i, column=2)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#888', width=6).grid(row=i, column=3)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='#999', width=6).grid(row=i, column=4)
            
    for i in range(10,20):
        if "$" in str(izlaze[i]):
            tk.Label(root, text=str(i+1) + " )", bg='#666600', width=4).grid(row=i - 10, column=5)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#b3b300', width=6).grid(row=i - 10, column=6)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='yellow', width=6).grid(row=i - 10, column=7)
        else:
            tk.Label(root, text=str(i+1) + " )", bg='#777', width=4).grid(row=i - 10, column=5)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#888', width=6).grid(row=i - 10, column=6)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='#999', width=6).grid(row=i - 10, column=7)
    for i in range(20,30):
        if "$" in str(izlaze[i]):
            tk.Label(root, text=str(i+1) + " )", bg='#666600', width=4).grid(row=i - 20, column=8)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#b3b300', width=6).grid(row=i - 20, column=9)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='yellow', width=6).grid(row=i - 20, column = 10)
        else:
            tk.Label(root, text=str(i+1) + " )", bg='#777', width=4).grid(row=i - 20, column=8)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#888', width=6).grid(row=i - 20, column=9)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='#999', width=6).grid(row=i - 20, column = 10)
    for i in range(30,35):
        if "$" in str(izlaze[i]):
            tk.Label(root, text=str(i+1) + " )", bg='#666600', width=4).grid(row=i - 30, column=11)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#b3b300', width=6).grid(row=i - 30, column=12)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='yellow', width=6).grid(row=i - 30, column=13)
        else:
            tk.Label(root, text=str(i+1) + " )", bg='#777', width=4).grid(row=i - 30, column=11)
            tk.Label(root, text=str(kvota[i]) + " x", bg='#888', width=6).grid(row=i - 30, column=12)
            tk.Label(root, text=str(izlaze[i]) + "       ", bg='#999', width=6).grid(row=i - 30, column=13)
    if novac < 0:
        exit()
Button(root, text="Igraj",padx=50,pady = 10,  command=funkcija).grid(column=1, row = 10)
 
root.mainloop()
