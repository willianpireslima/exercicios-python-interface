import customtkinter as ctk

def custo_faren_pole():
    try:
        farenheit = float(entrada_numero1.get())
        polegada = float(entrada_numero2.get())

        celsius = 5/9 * (farenheit-32)
        milimetros = 25.4*polegada

        label_celsius.configure(text=f"Celsius: {celsius}")
        label_milimetros.configure(text=f"Milimetros: {milimetros}")
    except ValueError:
        label_celsius.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Custo da Lata")

# Criar os widgets
rotulo_numero1 = ctk.CTkLabel(janela, text="Farenheit :")
rotulo_numero1.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Farenheit")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

rotulo_numero2 = ctk.CTkLabel(janela, text="Polegadas :")
rotulo_numero2.grid(row=1,column=0, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Polegadas")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

botao_somar = ctk.CTkButton(janela, text="Calcular", command=custo_faren_pole,hover_color="green")
botao_somar.grid(row=2,column=0, columnspan=2, pady=10)

label_celsius = ctk.CTkLabel(janela, text="Celsius:")
label_celsius.grid(row=3,column=0,columnspan=2, pady=10)

label_milimetros = ctk.CTkLabel(janela, text="Milimetros:")
label_milimetros.grid(row=4,column=0,columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()