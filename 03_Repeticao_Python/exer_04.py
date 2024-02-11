import customtkinter as ctk
from tkinter import *
import math

#) Um número inteiro positivo é triangular se este for o resultado do produto de três números naturais
#consecutivos. Por exemplo, o número 120 é triangular porque 120 = 4*5*6.
#Fazer um algoritmo que:
#leia um número inteiro;
#verifique se o número é ou não triangular. Se for imprimir: “Número Triangular” senão imprimir:"Número não Triangular”

def verificarTriangular():
    a = int(entrada_numero1.get())

    mens = "Nao"

    for i in range (1,a,1):
        if ( i*(i+1)*(i+2) == a) :mens = "Sim"

    label_result.configure(text=f"E Triangular ? : {mens}")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")
janela.geometry("200x300")

janela.title("Verificar Trianguridade")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite o Numero :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero :")
entrada_numero1.grid(row=1,column=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=verificarTriangular,hover_color="green")
botao_calcular.grid(row=2,column=0, columnspan=2, pady=10)

label_result= ctk.CTkLabel(janela, text="Checagem:")
label_result.grid(row=5,column=0,columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()