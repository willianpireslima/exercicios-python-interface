import customtkinter as ctk
import math

def calcular_delta():
    try:
        x1 = int(entrada_numero1.get())
        y1 = int(entrada_numero2.get())
        x2 = int(entrada_numero3.get())
        y2 = int(entrada_numero4.get())

        distancia = math.sqrt( math.pow(x2 - x1,2) + math.pow(y2 - y1,2))

        label_area.configure(text=f"Distancia: {distancia}")

    except ValueError:
        label_distancia.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Distancia entre Pontos")

# Criar os widgets
rotulo_pontoa = ctk.CTkLabel(janela, text="Ponto A :")
rotulo_pontoa.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="x1")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="y1")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

rotulo_pontob = ctk.CTkLabel(janela, text="Ponto B :")
rotulo_pontob.grid(row=2,column=0, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="x2")
entrada_numero3.grid(row=2,column=1, padx=10, pady=10)

entrada_numero4 = ctk.CTkEntry(janela,placeholder_text="y2")
entrada_numero4.grid(row=3,column=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_delta,hover_color="green")
botao_calcular.grid(row=4,column=0, columnspan=2, pady=10)

label_distancia = ctk.CTkLabel(janela, text="Distancia:")
label_distancia.grid(row=5,column=0,columnspan=2, pady=3)

# Iniciar o loop principal da aplicação
janela.mainloop()