import customtkinter as ctk
from tkinter import *
import math

#)Fazer um algoritmo que leia um número inteiro positivo, calcule e escreva se o número lido é perfeito ou não.
#Número perfeito é aquele cuja soma de seus divisores, exceto ele próprio, é igual ao número. Exemplo: 6 é um
#número perfeito porque 1 + 2 + 3 = 6.

def verificarPerfeito():
    num1 = int(entrada_numero1.get())

    resul=0
    for i in range (1,num1,1):
        if ( num1 % (num1-i) == 0): resul += (num1-i)

    mens = "Sim" if (num1 == resul) else "Nao"

    label_result.configure(text=f"e Perfeito ? : {mens}")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
janela.geometry("200x300")

janela.title("Verificar se e Perfeito")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite o Numero :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero:")
entrada_numero1.grid(row=1,column=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=verificarPerfeito,hover_color="green")
botao_calcular.grid(row=2,column=0, columnspan=2, pady=10)

label_result= ctk.CTkLabel(janela, text="Checagem:")
label_result.grid(row=3,column=0,columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()