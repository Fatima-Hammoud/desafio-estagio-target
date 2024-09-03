def inverter_string(s):
   
    lista_caracteres = list(s)
    
    inicio = 0
    fim = len(lista_caracteres) - 1
    
    while inicio < fim:
       
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        
      
        inicio += 1
        fim -= 1
    
   
    return ''.join(lista_caracteres)

def main():
    
    s = input("Digite a string que deseja inverter: ")
    
    
    string_invertida = inverter_string(s)
    
   
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    main()
