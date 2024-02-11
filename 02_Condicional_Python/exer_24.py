import math

import customtkinter as ctk

def calcular_medias() :
    try:
        # entrada_numero1.get() captura da entrada
        # combo.get()  captura da combobox entrada

        num = int(entrada_numero.get())

        if combo.get() == "1": resul = num*0.90
        elif combo.get() == "2": resul = num*0.95
        elif combo.get() == "4":resul = num*1.10

        label_resultado.configure(text=f"Resultado : {resul:.2f}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

janela = ctk.CTk()
janela.title("Verificacao pagamentos")
janela.geometry('250x250')

ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite o Valor:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero = ctk.CTkEntry(janela,placeholder_text="Numero")
entrada_numero.grid(column=0,row=1, padx=10, pady=10)

combo = ctk.CTkComboBox(master=janela,values=["1","2","3","4"])
combo.grid(column=0,row=4, padx=10, pady=10)
combo.set("Medias")

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_medias,hover_color="green")
botao_calcular.grid(column=0,row=5, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=6, columnspan=1, pady=10)

janela.mainloop()