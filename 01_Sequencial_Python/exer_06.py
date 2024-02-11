import customtkinter as ctk

def contar_batidas():
    try:
        numero = int(entrada_numero.get())
        resultado = numero*1.42
        label_resultado.configure(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Calculadora Batidas em X anos")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Calculo Carro :")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero = ctk.CTkEntry(janela,placeholder_text="Custo Fabrica :")
entrada_numero.grid(column=1,row=0, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=contar_batidas,hover_color="green")
botao_calcular.grid(column=0,row=2, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Custo Consumidor:")
label_resultado.grid(column=0,row=3, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
