import customtkinter as ctk
import math

def calcular_determinante():
    try:
        a11 = int(entrada_numero1.get())
        a12  = int(entrada_numero2.get())
        a21 = int(entrada_numero3.get())
        a22 = int(entrada_numero1.get())

        determinante = a11*a22 - a21*a12

        label_determinante.configure(text=f"Determinante: {determinante}")

    except ValueError:
        label_determinante.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Calcular Determinante")

# Criar os widgets
rotulo_numero1 = ctk.CTkLabel(janela, text="Determinante :")
rotulo_numero1.grid(row=0,column=0,columnspan=4, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="a11")
entrada_numero1.grid(row=1,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="a12")
entrada_numero2.grid(row=1,column=2, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="a21")
entrada_numero3.grid(row=2,column=1, padx=10, pady=10)

entrada_numero4 = ctk.CTkEntry(janela,placeholder_text="a22")
entrada_numero4.grid(row=2,column=2, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_determinante,hover_color="green")
botao_calcular.grid(row=4,column=0, columnspan=4, pady=10)

label_determinante = ctk.CTkLabel(janela, text="Distancia:")
label_determinante.grid(row=5,column=0,columnspan=4, pady=3)

# Iniciar o loop principal da aplicação
janela.mainloop()