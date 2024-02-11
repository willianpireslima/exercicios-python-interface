import customtkinter as ctk
from tkinter import *
import math

def verificarCapicuas():
    a = int(entrada_numero1.get())
    #converter numero para array
    array = [int(x) for x in str(a)]

    # comparar seu numero com o inverso
    mens = "Sim" if array[0:]==array[::-1] else "Nao"
    label_result.configure(text=f"E um Capicuas ?: {mens}")
# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
janela.geometry("200x300")

janela.title("Verificar Capicuas")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite o Numero :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero :")
entrada_numero1.grid(row=1,column=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=verificarCapicuas,hover_color="green")
botao_calcular.grid(row=2,column=0, columnspan=2, pady=10)

label_result= ctk.CTkLabel(janela, text="Checagem:")
label_result.grid(row=5,column=0,columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
