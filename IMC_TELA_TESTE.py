import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def imc_calculo():
    altura = float(altura_caixa.get())
    peso = float(peso_caixa.get())
    IMC = peso / (altura ** 2)
    resultado.configure(text=f"Seu IMC é: {IMC:.2f}")
    if(IMC < 16.9):
        status.configure(text="Você está muito abaixo do peso!")
    elif(IMC <= 18.4):
        status.configure(text="Você está abaixo do peso!")
    elif(IMC <=24.9 ):
        status.configure(text="Você está no peso ideal!")
    elif(IMC <= 29.9):
        status.configure(text="Você está acima do peso!")
    elif(IMC <= 34.9):
        status.configure(text="Você está com Obesidade grau I")
    elif(IMC <= 40):
        status.configure(text="Você está com Obesidade grau II")
    elif(IMC > 40):
        status.configure(text="Você está com Obesidade grau III")

janela = ctk.CTk()
janela.geometry("500x300")
janela.title("IMC Calculator")

texto = ctk.CTkLabel(janela, text="Calcule seu IMC!")
altura_caixa = ctk.CTkEntry(janela, placeholder_text="Altura")
peso_caixa = ctk.CTkEntry(janela, placeholder_text="Peso")
botao = ctk.CTkButton(janela, text="Calcular", command=imc_calculo)
resultado = ctk.CTkLabel(janela)
status = ctk.CTkLabel(janela)

texto.pack(padx=10, pady=10)
altura_caixa.pack(padx=10, pady=10)
peso_caixa.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)
resultado.pack(padx=10, pady=10)
status.pack(padx=10, pady=10)

janela.mainloop()

