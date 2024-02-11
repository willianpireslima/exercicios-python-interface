import math

import customtkinter as ctk

def par_impar():
    try:
        a = int(entrada_numero1.get())
        b = int(entrada_numero2.get())
        c = int(entrada_numero3.get())

        delta = math.sqrt(b*b - 4*a*c)

        if delta > 0: mens = "RAÍZES DISTINTAS"
        elif delta == 0: mens = "RAIZ ÚNICA"
        elif delta < 0 : mens = "RAÍZES IMAGINÁRIAS"

        label_resultado.configure(text=f"{mens }")
    except ValueError:
        label_resultado.configure(text="RAÍZES IMAGINÁRIAS")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Verificar Raizes da Equaacao")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Numeros:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Coeficiente 1")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Coeficiente 2")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Coeficiente 3")
entrada_numero3.grid(column=0,row=3, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=par_impar,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()