import customtkinter as ctk
from tkinter import *
import math

def mmc():
    a = int(entrada_numero1.get())
    b = int(entrada_numero2.get())

    while b > 0:
        r = a % b
        a = b
        b = r

    label_result.configure(text=f"MMC : {a }")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
janela.geometry("200x300")

janela.title("ver o mmc")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite o Numero :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero 1:")
entrada_numero1.grid(row=1,column=0, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Numero 2 :")
entrada_numero2.grid(row=2,column=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=mmc,hover_color="green")
botao_calcular.grid(row=3,column=0, columnspan=2, pady=10)

label_result= ctk.CTkLabel(janela, text="Checagem:")
label_result.grid(row=4,column=0,columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
