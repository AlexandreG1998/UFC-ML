import requests
import bs4

import pandas as pd

nomes_colunas = ['Evento',	'LutadorA','LutadorB','Rounds','Tempo','Metodo',    'KD_A', 'SIG.STR._A',   'SIG.STR.%_A',  'TOTALSTR._A',	'TD_A',	'TD%_A',	'SUB.ATT_A',	'PASS_A',	'REV._A',	'SIG.STR_A',	'SIG.STR.%_A',	'HEAD_A',	'BODY_A',	'LEG_A',	'DISTANCE_A',	'CLINCH_A',	'GROUND_A',	'R_E_V_A',	'KD_B',	'SIG.STR._B',	'SIG.STR.%_B',	'TOTALSTR._B',	'TD_B',	'TD%_B',	'SUB.ATT_B',	'PASS_B',	'REV._B',	'SIG.STR_B',	'SIG.STR.%_B',	'HEAD_B',	'BODY_B',	'LEG_B',	'DISTANCE_B',	'CLINCH_B',	'GROUND_B',	'R_E_V_B',
]

lista_eventos = pd.read_csv('Eventos/Evento_Luta.csv', sep = ';')

dados_lutas = []

for contador in range(5000, len(lista_eventos)):
    print('Iniciando link: ' + str(contador))
    link_luta_completo = lista_eventos.iloc[:,1:2][contador:contador+1].values.ravel()[0]
    idevento_completo = lista_eventos.iloc[:,0:1][contador:contador+1].values.ravel()[0]
    page = requests.get(link_luta_completo, 'html.parser')
    page_bs4 = bs4.BeautifulSoup(page.text)

    titulo_1  = page_bs4.find_all(class_ = 'b-fight-details__fight-title')[0].text
    lutador_a = page_bs4.find_all(class_ = 'b-fight-details__person-name')[0].text
    lutador_b = page_bs4.find_all(class_ = 'b-fight-details__person-name')[1].text


    metodo_ = page_bs4.find_all(class_ = 'b-fight-details__text-item_first')
    metodo_ = metodo_[0].text
    mtd = metodo_.replace('\n', '')
    mtd = mtd.replace(' ','')
    mtd = mtd.replace('Method:', '')


    tabela_detalhes_luta = page_bs4.find_all(class_ = 'b-fight-details__text-item')

    rounds = tabela_detalhes_luta[0].text.replace(' ','')
    rounds = rounds.replace('\n','')
    rounds = rounds.replace('Round:','')


    time = tabela_detalhes_luta[1].text.replace(' ','')
    time = time.replace('\n','')
    time = time.replace('Time:','')


    tabela_totals = page_bs4.find_all(class_ = 'b-fight-details__table-row')
    tb1 = tabela_totals[1].text.replace('\n\n','\n')

    #Tratamento Tabela Total
    for g in range(10):
        tb1 = tb1.replace('\n\n','\n')

    tb1_ = tb1.split('\n')
    tb1_normal = []
    for k in range(len(tb1_)):
        if((tb1_[k] != '') & (tb1_[k] != '  ') & (tb1_[k] != ' ') & (tb1_[k] != '   ')& (tb1_[k] != '    ')):
            tb1_normal.append(tb1_[k])

    dados_totais_lutador1 ,dados_totais_lutador2= [], []

    for k in range(len(tb1_normal)):
        if((k%2) == 0):
            data = tb1_normal[k].replace('%','')
            data = data.replace(' ','')
            data = data.split('of')

            if (len(data) > 1):
                dados_totais_lutador1.append((data[1]))
            else:
                dados_totais_lutador1.append((data[0]))
        else:
            data = tb1_normal[k].replace('%','')
            data = data.replace(' ','')
            data = data.split('of')

            if (len(data) > 1):
                dados_totais_lutador2.append((data[1]))
            else:
                dados_totais_lutador2.append((data[0]))


        
    # Selecionar tabela strike certa
    ind = 0

    strikes = None
    for i in range(len(tabela_totals)):
        if(tabela_totals[i].text.find('Leg') >= 0):
            ind = i + 1
            strikes = tabela_totals[ind].text

            for k in range(10):
                strikes = strikes.replace('\n\n', '')
                                
                break

    strikes = strikes.split('\n')
    strikes_normal = []
    for k in range(len(strikes)):
        if((strikes[k] != '') & (strikes[k] != '  ') & (strikes[k] != ' ') & (strikes[k] != '   ')& (strikes[k] != '    ')):
            strikes_normal.append(strikes[k])


    dados_totais_lutador1_stk ,dados_totais_lutador2_stk= [], []

    for k in range(len(tb1_normal)):
        if((k%2) == 0):
            data = tb1_normal[k].replace('%','')
            data = data.replace(' ','')
            data = data.split('of')

            if (len(data) > 1):
                dados_totais_lutador1_stk.append((data[1]))
            else:
                dados_totais_lutador1_stk.append((data[0]))
        else:
            data = tb1_normal[k].replace('%','')
            data = data.replace(' ','')
            data = data.split('of')

            if (len(data) > 1):
                dados_totais_lutador2_stk.append((data[1]))
            else:
                dados_totais_lutador2_stk.append((data[0]))

    linha_final = []


    linha_final.append(idevento_completo)
    linha_final.append(lutador_a)
    linha_final.append(lutador_b)
    linha_final.append(rounds)
    linha_final.append(time)
    linha_final.append(mtd)
    linha_final.extend(dados_totais_lutador1)
    linha_final.extend(dados_totais_lutador1_stk)
    linha_final.extend(dados_totais_lutador2)
    linha_final.extend(dados_totais_lutador2_stk)

    linha_final_real = []

    linha_final_real.append([linha_final[0]])
    linha_final_real.append([linha_final[1]])
    linha_final_real.append([linha_final[2]])
    linha_final_real.append([linha_final[3]])
    linha_final_real.append([linha_final[4]])
    linha_final_real.append([linha_final[5]])
    linha_final_real.append([linha_final[7]])
    linha_final_real.append([linha_final[8]])
    linha_final_real.append([linha_final[9]])
    linha_final_real.append([linha_final[10]])
    linha_final_real.append([linha_final[11]])
    linha_final_real.append([linha_final[12]])
    linha_final_real.append([linha_final[13]])
    linha_final_real.append([linha_final[14]])
    linha_final_real.append([linha_final[15]])
    linha_final_real.append([linha_final[17]])
    linha_final_real.append([linha_final[18]])
    linha_final_real.append([linha_final[19]])
    linha_final_real.append([linha_final[20]])
    linha_final_real.append([linha_final[21]])
    linha_final_real.append([linha_final[22]])
    linha_final_real.append([linha_final[23]])
    linha_final_real.append([linha_final[24]])
    linha_final_real.append([linha_final[25]])
    linha_final_real.append([linha_final[27]])
    linha_final_real.append([linha_final[28]])
    linha_final_real.append([linha_final[29]])
    linha_final_real.append([linha_final[30]])
    linha_final_real.append([linha_final[31]])
    linha_final_real.append([linha_final[32]])
    linha_final_real.append([linha_final[33]])
    linha_final_real.append([linha_final[34]])
    linha_final_real.append([linha_final[35]])
    linha_final_real.append([linha_final[37]])
    linha_final_real.append([linha_final[38]])
    linha_final_real.append([linha_final[39]])
    linha_final_real.append([linha_final[40]])
    linha_final_real.append([linha_final[41]])
    linha_final_real.append([linha_final[42]])
    linha_final_real.append([linha_final[43]])
    linha_final_real.append([linha_final[44]])
    linha_final_real.append([linha_final[45]])

    linha_final_real = pd.DataFrame(linha_final_real)
    linha_final_real = linha_final_real.transpose()
    linha_final_real.columns = nomes_colunas
    dados_lutas.append(linha_final_real)
#Juntar lutas

dados_compilados_lutas = dados_lutas[0]

for i in range(1, len(dados_lutas)):
    dados_compilados_lutas = pd.concat((dados_compilados_lutas,dados_lutas[i] ), axis = 0)
    
