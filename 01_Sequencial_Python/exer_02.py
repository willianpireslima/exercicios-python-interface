import customtkinter as ctk

def custo_area_lata():
    try:
        numero1 = int(entrada_numero1.get())
        numero2 = int(entrada_numero2.get())
        resultado = 3.14*numero1*numero1*2 + 2*numero1*numero2
        resultado +=resultado*100
        label_resultado.configure(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Custo da Lata")

# Criar os widgets
rotulo_numero1 = ctk.CTkLabel(janela, text="Raio :")
rotulo_numero1.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Raio")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

rotulo_numero2 = ctk.CTkLabel(janela, text="Altura :")
rotulo_numero2.grid(row=1,column=0, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Altura")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

botao_somar = ctk.CTkButton(janela, text="Calcular", command=custo_area_lata,hover_color="green",border_color="blue")
botao_somar.grid(row=2,column=0, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Resultado:")
label_resultado.grid(row=3,column=1, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
