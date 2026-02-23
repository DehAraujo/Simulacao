def validar_peso(peso):
    if(peso <= 0 or peso > 20):
        raise ValueError("Peso inválido")
        print(peso)
    elif peso <= 1:
        return 10
    elif(peso <= 5):
        return 15
    elif(peso <= 20):
        return 25
        
def validar_destino(destino):
    if destino not in ["mesma_regiao", "outra_regiao", "internacional"]:
        raise ValueError("Regiao invalida")
    return destino
        
def calcular_frete(peso, destino, valor_pedido):
    if(valor_pedido > 200):
        return 0
    else:
        if(valor_pedido <= 0):
            raise ValueError("Valor pedido invalido")
        else:
            if(validar_destino(destino) == "outra_regiao"):
                valor_frete = validar_peso(peso) + (validar_peso(peso) * 50) / 100
            elif(validar_destino(destino) == "internacional "):
                valor_frete = 2 * (validar_peso)

