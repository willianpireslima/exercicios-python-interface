import math

import customtkinter as ctk

def calcular_figuras() :
    try:
        # entrada_numero1.get() captura da entrada
        # combo.get()  captura da combobox entrada

        raio = int(entrada_numero1.get())
        altura = int(entrada_numero2.get())

        if combo.get() == "Cone Reto":
            volume = (3.14*raio*raio*altura)/3
            area = 3.14 * raio * math.sqrt(raio*raio + altura*altura)

        elif combo.get() == "Cilindro":
            volume = 3.14 * raio * raio * altura
            area = 2*3.14 * raio * altura

        elif combo.get() == "Esfera":
            volume = 3.14 * raio * raio * altura
            area = (4/3) * 3.14 * math.pow(raio,3)

        label_resultado1.configure(text=f"Volume : {volume:.2f}")
        label_resultado2.configure(text=f"Area   : {area:.2f}")
    except ValueError:
        label_resultado1.configure(text="Por favor, insira números válidos.")

janela = ctk.CTk()
janela.title("Verificacao Aluguel")
janela.geometry('250x350')

ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite os Valores:")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero1 = ctk.CTkEntry(janela,placeholder_text="Raio")
entrada_numero1.grid(column=0,row=1, padx=10, pady=10)

entrada_numero2 = ctk.CTkEntry(janela,placeholder_text="Altura")
entrada_numero2.grid(column=0,row=2, padx=10, pady=10)

combo = ctk.CTkComboBox(master=janela,values=["Cone Reto","Cilindro","Esfera"])
combo.grid(column=0,row=3, padx=10, pady=10)
combo.set("Figuras")

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=calcular_figuras,hover_color="green")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado1 = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado1.grid(column=0,row=5, columnspan=1, pady=10)

label_resultado2 = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado2.grid(column=0,row=6, columnspan=1, pady=10)

janela.mainloop()