def calcular_percentuais(faturamento_estado):
    

    total_mensal = sum(faturamento_estado.values())
    
    percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento_estado.items()}
    
    return percentuais

def main():
   
    faturamento_estado = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }
    
    percentuais = calcular_percentuais(faturamento_estado)
    
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()
