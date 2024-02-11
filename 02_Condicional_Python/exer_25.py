import math

import customtkinter as ctk

def calcular_medias() :
    try:
        # entrada_numero1.get() captura da entrada
        # combo.get()  captura da combobox entrada

        num1 = int(entrada_numero1.get())
        num2 = int(entrada_numero2.get())
        num3 = int(entrada_numero3.get())

        if combo.get() == "Aritmetica": resul = (num1 + num2 + num3)/3
        elif combo.get() == "Ponderada": resul = (3*num1 + 3*num2 + 4*num3)/3
        elif combo.get() == "Harmonica":resul = 3/(1/num1 + 1/num2 + 1/num3)
        elif combo.get() == "Geometrica":resul = math.cbrt(num1*num2*num3)
        elif combo.get() == "Quadratica":resul = math.sqrt((num1*num1*num2*num2*num3*num3)/3)

        label_resultado.configure(text=f"Resultado : {resul:.2f}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

janela = ctk.CTk()
janela.title("Verificacao Aluguel")
janela.geometry('250x350')

ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite o Valor:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero 1")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Numero 2")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Numero 3")
entrada_numero3.grid(column=0,row=3, padx=10, pady=10)

combo = ctk.CTkComboBox(master=janela,values=["Aritmetica","Ponderada","Harmonica","Geometrica","Quadratica"])
combo.grid(column=0,row=4, padx=10, pady=10)
combo.set("Medias")

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_medias,hover_color="green")
botao_calcular.grid(column=0,row=5, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=6, columnspan=1, pady=10)

janela.mainloop()