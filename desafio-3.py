def analisar_faturamento(faturamento_diario):
    
    if not faturamento_diario:
        return None, None, 0

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)

    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    faturamento_diario = [200, 150, 300, 250, 400, 350, 500, 300, 150, 100, 250, 300]

    menor, maior, dias_acima_da_media = analisar_faturamento(faturamento_diario)

    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

if __name__ == "__main__":
    main()
