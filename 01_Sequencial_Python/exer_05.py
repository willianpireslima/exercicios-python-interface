import customtkinter as ctk
import math

def calcular_delta():
    try:
        a = int(entrada_numero1.get())
        b = int(entrada_numero2.get())
        c = int(entrada_numero3.get())

        delta =math.sqrt(b*b-4*a*c)

        label_delta.configure(text=f"Delta: {delta}")

    except ValueError:
        label_delta.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Calcular Delta")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Calcular Determinante :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Coeficiente A :")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Coeficiente B : ")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Coeficiente C : ")
entrada_numero3.grid(row=2,column=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_delta,hover_color="green")
botao_calcular.grid(row=3,column=0, columnspan=2, pady=10)

label_delta = ctk.CTkLabel(janela, text="Delta:")
label_delta.grid(row=4,column=0,columnspan=2, pady=3)

# Iniciar o loop principal da aplicação
janela.mainloop()