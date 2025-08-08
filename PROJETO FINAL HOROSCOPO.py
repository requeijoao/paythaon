import tkinter as tk
from tkinter import messagebox

def descobrir_signo(dia, mes):
    if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        return "Áries"
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        return "Touro"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
        return "Gêmeos"
    elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
        return "Câncer"
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return "Leão"
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
        return "Virgem"
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return "Libra"
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return "Escorpião"
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return "Sagitário"
    elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        return "Capricórnio"
    elif (dia >= 20 and mes == 1) or (dia <= 18 and mes == 2):
        return "Aquário"
    elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
        return "Peixes"
    else:
        return "Data inválida"

def verificar_combina_joao(signo):
    boas_combinacoes = ["Touro", "Capricórnio", "Peixes"]
    ruins_combinacoes = ["Áries", "Gêmeos", "Sagitário"]

    if signo in boas_combinacoes:
        return "Você é uma boa combinação com o João."
    elif signo in ruins_combinacoes:
        return "Você não é uma boa combinação com o João, mas podemos tentar."
    else:
        return "Você é uma combinação normal com o João, faça um esforcinho e ele será seu."

def verificar_signo():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        ano = int(entry_ano.get())

        signo = descobrir_signo(dia, mes)
        if signo == "Data inválida":
            messagebox.showerror("Erro", "Data de nascimento inválida.")
        else:
            mensagem = verificar_combina_joao(signo)
            resultado = f"Você nasceu em {dia:02d}/{mes:02d}/{ano} e seu signo é {signo}.\n{mensagem}"
            messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos.")

# Interface com Tkinter
root = tk.Tk()
root.title("Signo e João")

tk.Label(root, text="Dia de nascimento:").grid(row=0, column=0, padx=10, pady=5)
entry_dia = tk.Entry(root)
entry_dia.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Mês de nascimento:").grid(row=1, column=0, padx=10, pady=5)
entry_mes = tk.Entry(root)
entry_mes.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Ano de nascimento:").grid(row=2, column=0, padx=10, pady=5)
entry_ano = tk.Entry(root)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

btn_verificar = tk.Button(root, text="Verificar Signo", command=verificar_signo)
btn_verificar.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()