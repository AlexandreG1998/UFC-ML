import requests
import bs4
import pandas as pd


abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
link_busca = 'http://www.ufcstats.com/statistics/fighters?char='

links_lutadores_compilado = []
for i in range(len(abc)):

    page = requests.get(link_busca + abc[i] + '&page=all', 'html.parser')

    page_bs4 = bs4.BeautifulSoup(page.text)


    links_lutadores  = page_bs4.find_all(class_ = 'b-link b-link_style_black')

    for k in range(len(links_lutadores)):
        link_tratado =  links_lutadores[k].prettify()
        link_tratado = link_tratado.replace(' ', '')
        link_tratado = link_tratado.replace('\n', '')
        try:
            link_tratado = link_tratado.split('href')[1].split('"')[1]
        except:
            link_tratado = 'erro'
        
        if((link_tratado in links_lutadores_compilado) == False):
            links_lutadores_compilado.append(link_tratado)
            print(link_tratado)


dados_lutadores = []
len(links_lutadores_compilado)
for i in range(5):
    page = requests.get(links_lutadores_compilado[i], 'html.parser')
    page_bs4 = bs4.BeautifulSoup(page.text)
    tabela_dados = page_bs4.find_all(class_ = 'b-list__box-list-item b-list__box-list-item_type_block')
    nome_lutador = page_bs4.find_all(class_ = 'b-content__title')
    nome_lutador = nome_lutador[0].text.split('\n')
    nome_lutador = nome_lutador[2].replace('                ', '')
    
    dados_lutador = []
    dados_lutador.append([nome_lutador])

    for k in range(len(tabela_dados)):
        txt = tabela_dados[k].text.replace('\n', '')
        txt = txt.replace(' ', '')
        if((txt != '') & (len(txt.split(':')) > 1)):
            txt = txt.split(':')[1]
            dados_lutador.append([txt])
        
    dados_lutadores.append(dados_lutador)
    
        
    
