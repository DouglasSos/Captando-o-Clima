# Depois de não sei quantas tentativa e alterações, esse é o produto final, graças à Deus.

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import openpyxl
import tkinter as tk
from PIL import ImageTk, Image

def capturar_clima():
    url = 'https://g1.globo.com/previsao-do-tempo/sp/barueri.ghtml'
    resposta = requests.get(url)
    sopa = BeautifulSoup(resposta.text, 'html.parser')

    temperatura_tag = sopa.find('span', class_='-bold -gray-dark-2 -font-55 _margin-l-20')
    temperatura = temperatura_tag.text.strip().replace("°", "") if temperatura_tag else 'N/A'

    umidade_tag = sopa.find('span', string='Umidade')
    if umidade_tag:
        umidade = umidade_tag.find_next('span').text.strip()
    else:
        umidade = 'N/D'

    try:
        temperatura_valor = int(temperatura)
    except:
        temperatura_valor = 0

    try:
        umidade_valor = int(umidade.replace('%', '').strip())
    except:
        umidade_valor = 0

    data = datetime.now().strftime('%d/%m/%Y')
    hora = datetime.now().strftime('%H:%M:%S')

    try:
        planilha = openpyxl.load_workbook('/storage/emulated/0/Download/DevPython/clima_barueri.xlsx')
        folha = planilha.active
    except FileNotFoundError:
        planilha = openpyxl.Workbook()
        folha = planilha.active
        folha.append(['Data', 'Hora', 'Temperatura', 'Umidade'])

    folha.append([data, hora, f"{temperatura}°", f"{umidade}%"])
    planilha.save('/storage/emulated/0/Download/DevPython/clima_barueri.xlsx')

    resultado_label.config(
        text=f"Data: {data}\nHora: {hora}\nTemperatura: {temperatura}°\nUmidade: {umidade}%"
    )

    # Me senti um gênio tendo essa ideia
    
    if umidade_valor > 80:
        imagem_path = "/storage/emulated/0/Download/DevPython/chuvoso.jpg"
    elif 40 <= umidade_valor <= 80:
        imagem_path = "/storage/emulated/0/Download/DevPython/nuvens.jpg"
    else:
        imagem_path = "/storage/emulated/0/Download/DevPython/sol.jpg"

    imagem = Image.open(imagem_path)
    imagem = imagem.resize((900, 800))
    imagem_tk = ImageTk.PhotoImage(imagem)
    imagem_label.config(image=imagem_tk)
    imagem_label.image = imagem_tk

# Deixando bonitinho, pq sou caprichoso

janela = tk.Tk()
janela.title("Clima Atual em Barueri")
janela.configure(bg="#e0f7f7")

titulo = tk.Label(janela, text="Clima Atual em Barueri", font=("Arial", 18, "bold"), bg="#e0f7f7", fg="#00695c")
titulo.pack(pady=10)

botao = tk.Button(janela, text="Qual o clima agora?", command=capturar_clima, bg="#4db6ac", fg="white", font=("Arial", 14, "bold"))
botao.pack(pady=10)

resultado_label = tk.Label(janela, text="Data: \nHora: \nTemperatura: \nUmidade:", font=("Arial", 14), bg="#e0f7f7", fg="#004d40", justify="center")
resultado_label.pack(pady=10)

imagem_label = tk.Label(janela, bg="#e0f7f7")
imagem_label.pack(pady=10)

janela.mainloop()

#Nem acredito que consegui, mesmo com a instabilidade do site, não connseguindo pegar a temperatura, eu estou feliz com o resultado.