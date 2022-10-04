import requests
import json
import pandas as pd
from time import sleep

while True:

    try:
        print("Atualização em 15 segundos.. ")
        sleep(15)
        data = requests.get(
            'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

        json_data = json.loads(data.content)

        candidato = []
        votos = []
        porcentagem = []

        total_apurado = json_data['psi']

    except Exception as error:
        print("Ops, algo deu errado na busca dos Dados! Tentando novamente... ")
        print("Erro: ", error)
    else:
        try:
            for informacoes in json_data['cand']:
                candidato.append(informacoes['nm'])
                votos.append(informacoes['vap'])
                porcentagem.append(informacoes['pvap'])

            df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
                'Candidato', 'N Votos', 'Porcentagem'])

            print(f""""
            
            Total apurado: {total_apurado}%
                
            {df_eleicao} """)
        except Exception as error:
            print("Ops, algo deu errado com os dados recebidos! Tentando novamente... ")
            print("Erro: ", error)
        else:
            print()
