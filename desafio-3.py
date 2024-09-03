import json

def analisar_faturamento(faturamento_diario):
   

   
    faturamentos = [valor for valor in faturamento_diario.values() if valor > 0]

    if not faturamentos:
        return None, None, 0

   
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)

    
    media_mensal = sum(faturamentos) / len(faturamentos)

    
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    try:
        
        with open('faturamento.json', 'r') as file:
            data = json.load(file)

        faturamento_diario = data.get("faturamento_diario", {})

        menor, maior, dias_acima_da_media = analisar_faturamento(faturamento_diario)

        if menor is not None:
            print(f"Menor valor de faturamento: {menor}")
            print(f"Maior valor de faturamento: {maior}")
            print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
        else:
            print("Nenhum dado de faturamento disponível para análise.")
    
    except FileNotFoundError:
        print("Arquivo 'faturamento.json' não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Verifique a formatação do arquivo.")

if __name__ == "__main__":
    main()
