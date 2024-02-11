import math

import customtkinter as ctk

def calcular_operacoes() :
    try:
        # entrada_numero1.get() captura da entrada
        # combo.get()  captura da combobox entrada

        num1 = int(entrada_numero1.get())
        num2 = int(entrada_numero2.get())

        if combo.get() == "+": resul = num1 + num2
        elif combo.get() == "-": resul = num1 - num2
        elif combo.get() == "*":resul = num1 * num2
        elif combo.get() == "/":resul = num1 / num2

        label_resultado.configure(text=f"Volume : {resul:.2f}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

janela = ctk.CTk()
janela.title("Verificacao Aluguel")
janela.geometry('250x300')

ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite os Valores:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero 1")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Numero 2")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

combo = ctk.CTkComboBox(master=janela,values=["+","-","*","/"])
combo.grid(column=0,row=3, padx=10, pady=10)
combo.set("Operacao")

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_operacoes,hover_color="green")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=1, pady=10)

janela.mainloop()