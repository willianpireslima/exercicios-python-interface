import customtkinter as ctk

def data_dia():
    try:
        mes = int(entrada_numero1.get())
        ano = int(entrada_numero2.get())

        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: mens = 31
        elif mes == 2 and ano % 4 == 0: mens = 29
        elif mes == 2:  mens = 28
        else : mens = 30

        label_resultado.configure(text=f"Dia da Data : {mens}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("200x300")
janela.title("Vericacao de dia por mes e ano")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Lados Triangulo:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Mes")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Ano")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=data_dia,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Dia da Data:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()