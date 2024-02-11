import customtkinter as ctk

def tipo_triangulo():
    try:
        dia = int(entrada_numero1.get())
        mes = int(entrada_numero2.get())
        ano = int(entrada_numero3.get())

        mens = "Sim " if (dia>0 and dia<32) and (mes>0 and mes<13) and (ano>1900 and ano<2100)  else "Nao"

        label_resultado.configure(text=f"{mens}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("300x300")
janela.title("Vericacao de Tipo de Triangulo")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Lados Triangulo:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Dia")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Mes")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Ano")
entrada_numero3.grid(column=0,row=3, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=tipo_triangulo,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()