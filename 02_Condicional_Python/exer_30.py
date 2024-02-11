import customtkinter as ctk

def par_impar():
    try:
        hora = int(entrada_numero1.get())
        salMin = 545
        valorHoraExtra = 10

        salaHoraExtra = hora * valorHoraExtra
        salaBruto = 3 * salMin + salaHoraExtra
        descontINSS = 0.12* salaBruto if salaBruto > 1500 else 0
        descontRenda = 0.20 * salaBruto if salaBruto > 2000 else 0
        salaLiq = salaBruto - descontINSS - descontRenda

        label_resultado.configure(text=f"Salario Liquido : {salaLiq}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("300x200")
janela.title("Número Capicua")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Salario:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Salario")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=par_impar,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Resultado:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()