import customtkinter as ctk

def contar_batidas():
    try:
        numero = int(entrada_numero.get())

        total = 8.50 + 3.50 * max(0,  numero - 3) #taxa fixa + valorPorHora*maximo
        label_resultado.configure(text=f"Custo: {total}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("locadora de charretes")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Locacao Charrete :")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero = ctk.CTkEntry(janela,placeholder_text="Hora :")
entrada_numero.grid(column=1,row=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=contar_batidas,hover_color="green")
botao_calcular.grid(column=0,row=2, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Custo:")
label_resultado.grid(column=0,row=3, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()