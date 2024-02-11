import math

import customtkinter as ctk

def calcular_operacoes() :
    try:
        # entrada_numero1.get() captura da entrada
        # combo.get()  captura da combobox entrada

        idade = int(entrada_numero.get())

        if idade >= 5 and idade <= 7 : mensa = "Infantil A"
        elif idade >= 8 and idade <= 10 : mensa = "Infantil B"
        elif idade >= 11 and idade <= 13 : mensa = "Juvenil A"
        elif idade >= 14 and idade <= 17 : mensa ="Juvenil B"
        elif idade >= 18 : mensa ="Senior A"

        label_resultado.configure(text=f"Categoria : {mensa}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

janela = ctk.CTk()
janela.title("Verificacao Aluguel")
janela.geometry('250x200')

ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite a Idade:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero = ctk.CTkEntry(janela,placeholder_text="Idade")
entrada_numero.grid(column=0,row=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Checar", command=calcular_operacoes,hover_color="green")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=1, pady=10)

janela.mainloop()