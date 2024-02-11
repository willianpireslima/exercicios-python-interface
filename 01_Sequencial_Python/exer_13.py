import customtkinter as ctk

def definir_maior():
    try:
        numero1 = int(entrada_numero1.get())
        numero2 = int(entrada_numero2.get())
        resultado = (numero1 + numero2 + abs(numero1 - numero2))/2
        label_resultado.configure(text=f"Maior: {resultado}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Custo da Lata")

# Criar os widgets
rotulo_numero1 = ctk.CTkLabel(janela, text="Numeros :")
rotulo_numero1.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Primeiro Numero")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Segundo Numero")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

botao_somar = ctk.CTkButton(janela, text="Calcular", command= definir_maior,hover_color="green",border_color="blue")
botao_somar.grid(row=2,column=0, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Maior:")
label_resultado.grid(row=3,column=1, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
