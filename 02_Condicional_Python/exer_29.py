import customtkinter as ctk

def par_impar():
    try:
        min = int(entrada_numero1.get())


        if (min <= 3) :tax = 3;
        else :
            div5 = min / 5
            tax = div5 * 2.15 + 0.85 * min-div5

        label_resultado.configure(text=f"Taxa : {tax}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("300x200")
janela.title("Número Capicua")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Taxa:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Taxa")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=par_impar,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Resultado:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()