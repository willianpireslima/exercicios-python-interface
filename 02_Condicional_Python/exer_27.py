import customtkinter as ctk
import math
def codigo_area():
    try:
        teleM = int(entrada_numero.get())

        if teleM == 3223 or teleM == 3225 or teleM == 3212: mensagem ="Oeste"
        elif teleM == 3224 : mensagem ="Centro"
        elif teleM == 3241 or teleM == 3242 or teleM == 3243 or teleM == 3281: mensagem ="Sul"
        elif teleM == 3251 or teleM == 3285: mensagem ="Bueno"
        elif teleM == 3233 or teleM == 3291: mensagem ="Campinas "
        else : mensagem ="Codigo Nao Listado"

        label_resultado.configure(text=f"{mensagem}")
    except ValueError:
        label_resultado.configure(text="Por favor, insira números válidos.")

# Criar a janela principal
janela = ctk.CTk()
ctk.set_appearance_mode("system")
ctk.set_appearance_mode("dark")

janela.geometry("200x200")
janela.title("Codigo Area")

# Criar os widgets
rotulo_numero = ctk.CTkLabel(janela, text="Digite Codigo :")
rotulo_numero.grid(column=0,row=0, padx=10, pady=10)

entrada_numero = ctk.CTkEntry(janela,placeholder_text="Codigo")
entrada_numero.grid(column=0,row=1, padx=10, pady=10)

botao_calcular = ctk.CTkButton(janela, text="Calcular", command=codigo_area,hover_color="green",border_color="blue")
botao_calcular.grid(column=0,row=4, columnspan=2, pady=10)

label_resultado = ctk.CTkLabel(janela, text="Verificacao:")
label_resultado.grid(column=0,row=5, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()