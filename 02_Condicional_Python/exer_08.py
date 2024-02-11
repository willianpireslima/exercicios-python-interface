import customtkinter as ctk

def par_impar():
    try:
        num1 = int(entrada_numero1.get())
        num2 = int(entrada_numero2.get())
        num3 = int(entrada_numero3.get())

        if   (num1 > num2 and num1 > num3) : maior = num1
        elif (num2 > num1 and num2 > num3) : maior = num2
        elif (num3 > num1 and num3 > num2) : maior = num3

        label_resultado.configure(text=f"{maior}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("300x300")
janela.title("Maior")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Numeros:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Numero 1")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Numero 2")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Numero 3")
entrada_numero3.grid(column=0,row=3, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=par_impar,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()