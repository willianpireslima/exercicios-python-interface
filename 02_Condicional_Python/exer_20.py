import customtkinter as ctk

def calcular_aluguel() :
    try:
        # entrada_numero1.get() captura da entrada
        # combo.get()  captura da combobox entrada

        num = int(entrada_numero.get())

        if (combo.get() == "Segunda"
        or combo.get() == "Terça"
        or combo.get() =="Quinta"):
            valor = num*0.60

        if "DVD Lancamento": valor = num*1.15

        label_resultado.configure(text=f"Valor Final : {valor:.2f}" )
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

janela = ctk.CTk()
janela.title("Verificacao Aluguel")
janela.geometry('250x300')
janela.resizable(False, False)

ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite o Valor do Aluguel:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero = ctk.CTkEntry(janela,placeholder_text="Valor Aluguel")
entrada_numero.grid(column=0,row=1, padx=10, pady=10)

combo = ctk.CTkComboBox(master=janela,values=["Segunda", "Terça","Quarta","Quinta","Sexta","Sabado","Domingo"])
combo.grid(column=0,row=2, padx=10, pady=10)
combo.set("Dias Da Semana")

combo2 = ctk.CTkComboBox(master=janela,values=["DVD Comum", "DVD Lancamento"])
combo2.grid(column=0,row=3, padx=10, pady=10)
combo2.set("Tipo DVD")

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_aluguel,hover_color="green")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=1, pady=10)

janela.mainloop()