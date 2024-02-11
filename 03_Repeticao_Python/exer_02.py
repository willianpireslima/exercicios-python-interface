import customtkinter as ctk
from tkinter import *
import math

def imprimirLista():
    raio=0
    volume=0
    while raio< 20:

        lb.insert(END, f"Volume : {volume:.2f} Raio : {raio}" )
        volume = (4 / 3) * 3.14 * math.pow(raio,3)
        raio+=0.5

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
janela.geometry("200x300")

janela.title("Calcular Delta")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Imprimir Funcao funcao raio :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)


botao_calcular = ctk.CTkButton(janela, text="Calcular", command=imprimirLista,hover_color="green")
botao_calcular.grid(row=1,column=0, columnspan=2, pady=10)

lb = Listbox(janela, height=5, width=30,bg="#262626", fg="white")
lb.grid(row=3, column=0)

# Iniciar o loop principal da aplicação
janela.mainloop()
