import customtkinter as ctk

def par_impar():
    try:
        dep = int(entrada_numero1.get()) # numero de dependentes
        sal = int(entrada_numero2.get()) # Salario
        impP = int(entrada_numero3.get()) # Imposto Pago
        salM = 1200 #Salario Minimo

        if 12*salM > sal: impB = sal*0.80
        elif sal > 5*salM  and sal < 12*salM : impB = sal*0.92

        sal = impB*0.96
        impB = sal - dep*300

        mens = "Imposto a pagar" if impP < impB else "“Imposto a receber"

        label_resultado.configure(text=f"{mens}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("300x300")
janela.title("Imposto")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Numeros:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Número de Dependentes")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Salário do Funcionário")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Imposto Normal Pago")
entrada_numero3.grid(column=0,row=3, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=par_impar,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()