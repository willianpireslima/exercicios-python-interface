import customtkinter as ctk
from tkinter import *
import math

def imprimirLista():
    num1 = int(entrada_numero1.get())

    for i in range(0, num1, 1):
        if num1 % (num1 - i) == 0:
            lb.insert(END,  f"Divisores: {num1 - i}" )

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
janela.geometry("200x300")

janela.title("Calcular Delta")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Mostrar Todos Divisores :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero:")
entrada_numero1.grid(row=1,column=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=imprimirLista,hover_color="green")
botao_calcular.grid(row=2,column=0, columnspan=2, pady=10)

lb = Listbox(janela, height=5, width=30,bg="#262626", fg="white")
lb.grid(row=3, column=0)

# Iniciar o loop principal da aplicação
janela.mainloop()
