import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 2 
  

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chorme")
pyautogui.press("enter")
pyautogui.click(x=906, y=632)
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
 
# Passo 2: Fazer login
pyautogui.click(x=1355, y=444)
pyautogui.write("cris@gmail.com")
pyautogui.press("Tab")
pyautogui.write("16381")
pyautogui.click(x=1530, y=619)


# 3° importa a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# 4° cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=1390, y=332)

    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("Tab")

    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("Tab")

    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("Tab")

    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("Tab")

    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("Tab")

    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("Tab")

    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# 5° repetir o cadastro para todos os produtos