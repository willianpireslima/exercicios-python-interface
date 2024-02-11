import customtkinter as ctk

def area_cilindro():
    try:
        numero1 = int(entrada_numero1.get())
        numero2 = int(entrada_numero2.get())
        volume = 1/3*numero1*numero2

        label_volume.configure(text=f"Volume: {volume}")
    except ValueError:
        label_volume.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Volume Cilindro")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Piramide :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Base")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Altura")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

botao_somar = ctk.CTkButton(janela, text="Calcular", command=area_cilindro,hover_color="green",border_color="blue")
botao_somar.grid(row=2,column=0, columnspan=2, pady=10)

label_volume = ctk.CTkLabel(janela, text="Volume:")
label_volume.grid(row=3,column=1, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()