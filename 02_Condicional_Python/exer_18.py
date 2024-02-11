import customtkinter as ctk

def calcular_conta() :
    try:
        # entrada_numero1.get() captura da entrada
        # combo.get()  captura da combobox entrada

        num = int(entrada_numero.get())

        if combo.get()   == "Residencial": valor = 5 + num*0.05
        elif combo.get() == "Comercial"  and num < 80  : valor = 500
        elif combo.get() == "Comercial"  and num > 80  : valor = 500 + num*0.25
        elif combo.get() == "Industrial" and num < 100 : valor = 800
        elif combo.get() == "Industrial" and num > 100 : valor = 800 + num*0.04

        label_resultado.configure(text=f"Valor Pago : {valor:.2f}" )
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

janela = ctk.CTk()
janela.title("Primeiro Combobox")
janela.geometry('250x250')
janela.resizable(False, False)

ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite A Quantia de Agua:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero = ctk.CTkEntry(janela,placeholder_text="m3 Agua")
entrada_numero.grid(column=0,row=1, padx=10, pady=10)

combo = ctk.CTkComboBox(master=janela,values=["Residencial", "Comercial","Industrial"])
combo.grid(column=0,row=2, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_conta,hover_color="green")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=1, pady=10)

janela.mainloop()