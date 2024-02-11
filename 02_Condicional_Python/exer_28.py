import customtkinter as ctk
import math
def checar_aprov():
    try:
        num1 = int(entrada_numero1.get())
        num2 = int(entrada_numero2.get())
        num3 = int(entrada_numero3.get())
        num4 = int(entrada_numero4.get())
        resul = ( num1 + 2*num2 + 3*num3 + num4)/7

        if resul > 9 and resul <= 10 : mens = "A" + "Aprovado"
        elif resul > 7.5 and resul <= 9 : mens ="B" + "Aprovado"
        elif resul > 6 and resul <= 7.5 : mens = "C" + "Aprovado"
        elif resul > 4 and resul <= 6  : mens = "D" + "Reprovado"
        elif resul <= 4 : mens ="E" + "Reprovado"


        label_resultado1.configure(text=f"{mens[0:1]}")
        label_resultado2.configure(text=f"{mens[1:9]}")
    except ValueError:
        label_resultado1.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("200x400")
janela.title("Checar aprovacao")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite as Notas :")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Nota 1")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Nota 2")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Nota 3")
entrada_numero3.grid(column=0,row=3, padx=10, pady=10)

entrada_numero4 = ctk.CTkEntry(janela,placeholder_text="Media Exer")
entrada_numero4.grid(column=0,row=4, padx=10, pady=10)


botao_calcular = ctk.CTkButton(janela, text="Calcular", command=checar_aprov,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=5, columnspan=2, pady=10)

label_resultado1 = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado1.grid(column=0,row=6, columnspan=2, pady=10)

label_resultado2 = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado2.grid(column=0,row=7, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()