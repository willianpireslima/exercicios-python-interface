import customtkinter as ctk
import math

def calculos_triang():
    try:
        lado1 = int(entrada_numero1.get())
        lado2 = int(entrada_numero2.get())
        cateto1 = abs(math.pow(lado1, 2) - math.pow(lado2, 2))
        cateto2 = 2*lado1*lado2
        hipotenusa = math.pow(lado1, 2) + math.pow(lado2, 2)

        label_cateto1.configure(text=f"Cateto 1: {cateto1}")
        label_cateto2.configure(text=f"Cateto 2: {cateto2}")
        label_hipotenusa.configure(text=f"Hipotenusa: {hipotenusa}")
    except ValueError:
        label_cateto1.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Calculos usando Teorema de Pitágoras")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Lados :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Lado 1 ")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Lado 2 ")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calculos_triang,hover_color="green",border_color="blue")
botao_calcular.grid(row=2,column=0, columnspan=2, pady=10)

label_cateto1 = ctk.CTkLabel(janela, text="Tamanho Cateto 1:")
label_cateto1.grid(row=3,column=0,columnspan=2, pady=10)

label_cateto2 = ctk.CTkLabel(janela, text="Tamanho Cateto 2:")
label_cateto2.grid(row=4,column=0,columnspan=2, pady=10)

label_hipotenusa = ctk.CTkLabel(janela, text="Tamanho Hipotenusa:")
label_hipotenusa.grid(row=5,column=0,columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()