# Este Proyecto fue logrado gracias a APIs & Paqutes hechos por Programadores Expertos, sin embargo.
# El Credito se lo lleva Netting por haber hecho funcionar de tal modo tales Paquetes & APIs.
# © Prod Ryan 2021 - Coded by Prod Ryan [ Netting ]

# ----- [ Importacion de Paquetes & APIs ] ----- #
import os
import sys
from time import sleep
import time
import random
from sty import register as sty
from colorama import *

# ----- [ Variables ] ----- #
bg = sty.bg
fg = sty.fg
rojo = fg(255,17,0)+""
naranja = fg(255,153,0)+""
amarillo = fg(255,217,0)+""
lima = fg(191,255,0)+""
verde = fg(85,255,0)+""
celeste = fg(0,255,115)+""
cian = fg(0,255,195)+""
gris = fg(207,207,207)+""
azul = fg(0,149,255)+""
morado = fg(162,0,255)+""
violeta = fg(255,0,242)+""
rosa = fg(255,140,215)+""
blanco = fg(255,255,255)+""

def rainbow(message):
	scale = [(255,0,0),(255,50,0),(255,100,0),(255,150,0),(255,200,0),(255,255,0),(200,255,0),(150,255,0),(100,255,0),(50,255,0),(0,255,0),(0,255,50),(0,255,100),(0,255,150),(0,255,200),(0,255,255),(0,200,255),(0,150,255),(0,100,255),(0,50,255),(0,0,255),(50,0,255),(100,0,255),(150,0,255),(200,0,255),(255,0,255),(255,0,200),(255,0,150),(255,0,100),(255,0,50),(255,0,0)]
	msg = message.replace("","@@@")
	bb = msg.split("@@@")
	a = random.randint(0,30)
	sys.stdout.write ("")
	for sc in bb:
		if a == 31: a = 0
		ls = list(scale[int(a)])
		a = a + 1
		sc = sc.replace(sc,fg(str(ls[0]),str(ls[1]),str(ls[2]))+sc+fg.rs)
		sys.stdout.write(sc)

def tptFlash(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)

def tpt(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.08)

def tptInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.04)
  valor = input()  
  return valor

def banner():
    rainbow(f'''
    Banner                  
        ''')

    tptFlash(f'''

    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ]{Fore.WHITE} {Fore.LIGHTGREEN_EX}Tool {Fore.WHITE}Desarrollada por {Fore.LIGHTGREEN_EX}© {Fore.LIGHTCYAN_EX}Prod Ryan {Fore.MAGENTA}[ {Fore.LIGHTCYAN_EX}Netting{Fore.MAGENTA} ]{Fore.WHITE}''')

def carga():
    os.system('cls || clear')
    tpt(f'''
    
    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ]{Fore.WHITE} Bienvenid@ a {Fore.RED}XD {Fore.LIGHTGREEN_EX}Tool{Fore.WHITE}... ''')

    time.sleep(2)

    tpt(f'''
    
    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ]{Fore.WHITE} {Fore.LIGHTGREEN_EX}Tool {Fore.WHITE}Desarrollada por {Fore.LIGHTGREEN_EX}© {Fore.LIGHTCYAN_EX}Prod Ryan {Fore.MAGENTA}[ {Fore.LIGHTCYAN_EX}Netting{Fore.MAGENTA} ]{Fore.WHITE}''')

    time.sleep(2)

    tpt(f'''
    
    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ] {Fore.WHITE} Dame dos Segundos mas & Comenzamos... ''')

    time.sleep(2)

    os.system('cls || clear')

def recarga():
    os.system('cls || clear')
    banner()
    mop()

# ----- [ Funciones ] ----- #
def op1():
    print(f'''
        
    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ] {Fore.WHITE} Opcion 1 Elegida...''')
    time.sleep(1)
    recarga()

def op2():
    print(f'''
        
    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ] {Fore.WHITE} Opcion 2 Elegida...''')
    time.sleep(1)
    recarga()

def op3():
    print(f'''
        
    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ] {Fore.WHITE} Opcion 3 Elegida...''')
    time.sleep(1)
    recarga()

def op4():
    print(f'''
        
    {Fore.MAGENTA}[ {Fore.WHITE}!{Fore.MAGENTA} ] {Fore.WHITE} Opcion 4 Elegida...''')
    time.sleep(1)
    recarga()

def mop():
    rainbow(f'''
    
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │                                                     │
    │   Seleccion una accion que quiera hacer             │                      
    │                                                     │
    │        1 - Opcion 1                                 │
    │                                                     │
    │        2 - Opcion 2                                 │                     
    │                                                     │
    │        3 - Opcion 3                                 │
    │                                                     │
    │        4 - Opcion 4                                 │
    │                                                     │
    │        5 - Salir                                    │
    │                                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
    ''')

    opciones = tptInput(f'''
    
    {Fore.LIGHTYELLOW_EX}[ {Fore.WHITE}?{Fore.LIGHTYELLOW_EX} ]{Fore.WHITE} ''')

    if opciones == '1':
        op1()
    elif opciones == '2':
        op2()
    elif opciones == '3':
        op3()
    elif opciones == '4':
        op4()
    elif opciones == '5':
        sys.exit()
    else:
        os.system('cls || clear')
        banner()
        mop()

# ----- [ Ejecutor ] ----- #
def menu():
    carga()
    banner()
    mop()

# ----- [ Inicializacion ] ----- #
menu()
