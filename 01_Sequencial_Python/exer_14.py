import customtkinter as ctk
import math

def calcular_RSD():
    try:
        a = int(entrada_numero1.get())
        b = int(entrada_numero2.get())
        c = int(entrada_numero3.get())

        s = math.pow(b+c,2)
        r = math.pow(a+b,2)
        d = (r+s)/2

        label_s.configure(text=f"S: {s}")
        label_r.configure(text=f"R: {r}")
        label_d.configure(text=f"D: {d}")

    except ValueError:
        label_s.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.title("area do triangulo")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Numeros :")
rotulo_numero.grid(row=0,column=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Inteiro A :")
entrada_numero1.grid(row=0,column=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Inteiro B : ")
entrada_numero2.grid(row=1,column=1, padx=10, pady=10)

entrada_numero3 = ctk.CTkEntry(janela,placeholder_text="Inteiro C : ")
entrada_numero3.grid(row=2,column=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_RSD,hover_color="green")
botao_calcular.grid(row=3,column=0, columnspan=2, pady=10)

label_s = ctk.CTkLabel(janela, text="S:")
label_s.grid(row=4,column=0,columnspan=2, pady=3)

label_r = ctk.CTkLabel(janela, text="R:")
label_r.grid(row=5,column=0,columnspan=2, pady=3)

label_d = ctk.CTkLabel(janela, text="D:")
label_d.grid(row=6,column=0,columnspan=2, pady=3)

# Iniciar o loop principal da aplicação
janela.mainloop()