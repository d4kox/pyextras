import tkinter as tk
import pyautogui as pg
import random as r
import os
import time

numbersList = [0,1,2,3,4,5,6,7,8,9]
operList = ["+","-","*","/"]

def abrir_mc():
    timer = shutdownTimer.get("1.0","end")
    if timer == "-\n":
        with open("shutdowner.bat","w") as shutdownFile:
            shutdownFile.write("")
        shutdownFile.close()
    else:
        timer = int(timer)
        with open("shutdowner.bat","w") as shutdownFile:
            shutdownFile.write("timeout /nobreak "+str(timer))
            shutdownFile.write("\nshutdown /f")
        shutdownFile.close()
                  
    resultado = Resultado.get("1.0","end")
    resultado = int(resultado)
    if Vresultado == resultado:
        os.system('start tlauncher')
        os.system('shutdowner.bat')
    ventana1.destroy()
        
ventana1=tk.Tk()
ventana1.title("Minecraft Launcher")
ventana1.geometry('2500x750')
ventana1.configure(bg="gray")


def charge_window(operacion, resultado):
    a1=tk.Label(ventana1,text="Bienvenido a El lanzador de Minecraft...")

    a2=tk.Label(ventana1,text="Establece el tiempo de apagado (segundos)... Para omitir esto: -.")

    global shutdownTimer
    shutdownTimer=tk.Text(ventana1,height=1)

    a3=tk.Label(ventana1,text="Resuelve esta operacion matematica...")
    a4=tk.Label(ventana1,text=operacion)
    global Resultado
    Resultado=tk.Text(ventana1, height=1)

    global Vresultado
    Vresultado = resultado

    a1.pack(padx=5,pady=5,ipadx=5,ipady=5)
    a2.pack(padx=5,pady=5,ipadx=5,ipady=5)
    shutdownTimer.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
    a3.pack(padx=5,pady=5,ipadx=5,ipady=5)
    a4.pack(padx=5,pady=5,ipadx=5,ipady=5)
    Resultado.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)
    a5=tk.Button(ventana1,text="Continuar",command=abrir_mc)
    a5.pack(side=tk.TOP)
    ventana1.mainloop()

def create_math(numbersList,operList):
    num1 = r.randint(0,9)
    oper = r.randint(0,3)
    num2 = r.randint(0,9)

    num1 = numbersList[num1]
    oper = operList[oper]
    num2 = numbersList[num2]

    if oper == "+":
        resultado = num1+num2
    elif oper == "-":
        resultado = num1-num2
    elif oper == "*":
        resultado = num1*num2
    elif oper == "/":
        if num1 < num2:
            create_math(numbersList, operList)
        else:
            resultado = num1/num2

    operacion = str(num1)+oper+str(num2)
    charge_window(operacion, resultado)


create_math(numbersList, operList)
