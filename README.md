# Meu app de Clima — Barueri

Este é um aplicativo feito totalmente no celular em código Python com interface gráfica (Tkinter) que exibe a temperatura, umidade, data e hora atuais da cidade de Barueri. Além disso, mostra uma imagem ilustrativa de acordo com o clima atual, legal né?

## O que ele faz?

- Captura temperatura e umidade do site G1.
- Exibe data e hora da última atualização.
- Mostra imagem do clima:
  - **Chuvoso:** umidade acima de 80%.
  - **Nublado:** umidade entre 40% e 80%.
  - **Ensolarado:** umidade abaixo de 40%.
- Salva as informações em uma planilha `.xlsx`.

## O que usei pra fazer?

- Pydroid 3
- Tkinter (interface gráfica)
- Requests e BeautifulSoup (raspagem de dados)
- OpenPyXL (planilha Excel)
- Pillow (exibição de imagens)

## Como usar?

1. Instale as bibliotecas necessárias:
   ```bash
   pip install requests beautifulsoup4 openpyxl pillow
