#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

numero = int(input("Digite um número inteiro positivo: "))

fibonacci = [0, 1]  # Inicializa a sequência de Fibonacci com os dois primeiros valores

while fibonacci[-1] < numero:  # Enquanto o último valor da sequência for menor que o número informado
    proximo = fibonacci[-1] + fibonacci[-2]  # Calcula o próximo valor da sequência
    fibonacci.append(proximo)  # Adiciona o próximo valor à sequência

if numero in fibonacci:  # Verifica se o número informado pertence à sequência de Fibonacci
    print(f"O número {numero} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")