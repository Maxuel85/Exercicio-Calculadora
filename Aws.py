def calculadora(num1, num2, operacao):

    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return 0
    else:
        print("Operação inválida. Resultado: 0")
        return 0

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
codigo_operacao = int(input("Digite o código da operação (1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão): "))

resultado = calculadora(numero1, numero2, codigo_operacao)
print(f"Resultado: {resultado}")