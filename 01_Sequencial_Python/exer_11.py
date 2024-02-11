import customtkinter as ctk

def custo_area_lata():
    try:
        raio = int(entrada_numero1.get())
        altura = int(entrada_numero2.get())
        area =2*3.14*raio*(altura+ raio)
        volume = 3.14*raio*raio*altura

        label_area.configure(text=f"Area: {area}")
        label_volume.configure(text=f"Volume: {volume}")
    except ValueError:
        label_area.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("Valores Cilindro")

# Criar os widgets
rotulo_numero1 = ctk.CTkLabel(janela, text="Cilindro :")
rotulo_numero1.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Raio")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Altura")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

botao_somar = ctk.CTkButton(janela, text="Calcular", command=custo_area_lata,hover_color="green",border_color="blue")
botao_somar.grid(row=2,column=0, columnspan=2, pady=10)

label_area = ctk.CTkLabel(janela, text="Area:")
label_area.grid(row=3,column=1, pady=10)

label_volume = ctk.CTkLabel(janela, text="Volume:")
label_volume.grid(row=4,column=1, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
