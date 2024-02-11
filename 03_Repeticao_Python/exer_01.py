import customtkinter as ctk
from tkinter import *
import math

#faça um algortimo que ao ser digitado um numero imprima ate esse numero em uma lista

def imprimirLista():
    a = int(entrada_numero1.get())

    i=0
    while i< a:
        lb.insert(END, i)
        i+=1

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
janela.geometry("200x300")

janela.title("Calcular Delta")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Imprimir Numercao :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero :")
entrada_numero1.grid(row=1,column=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=imprimirLista,hover_color="green")
botao_calcular.grid(row=2,column=0, columnspan=2, pady=10)

lb = Listbox(janela, height=3,bg="#262626", fg="white")
lb.grid(row=3, column=0)

# Iniciar o loop principal da aplicação
janela.mainloop()