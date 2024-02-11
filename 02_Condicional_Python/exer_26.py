import customtkinter as ctk
import math
def bissexto():
    try:
        ano = int(entrada_numero1.get())

        mensagem= 'Sim' if ano%4==0 and ano%400==0 and ano%100!=0 else 'Nao'

        label_resultado.configure(text=f" O Ano e Bissexto? {mensagem}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("200x200")
janela.title("Quadrado perfeito")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Ano :")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Ano")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=bissexto,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()