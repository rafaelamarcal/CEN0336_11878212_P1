#!/usr/bin/env python3
import sys

# Função para ver se os números são inteiros e menores que 500
def verificar_inteiros_positivos(valores):
    # Checar se os dois números são válidos e estão entre 1 e 499
    return all(v.isdigit() and 1 <= int(v) < 500 for v in valores)

# Verificar se o usuário passou dois números como argumento
if len(sys.argv) != 3:
    print("Erro: Digite dois números inteiros, positivos e menores que 500.")
    sys.exit(1)

# Pega os dois números digitados pelo usuário
a, b = sys.argv[1], sys.argv[2]

# Verifica se os números são inteiros e estão no intervalo de 1 a 499
if not verificar_inteiros_positivos([a, b]):
    print("Erro: Os números devem ser inteiros positivos e menores que 500.")
    sys.exit(1)

# Transforma os números em inteiros
a = int(a)
b = int(b)

# Faz o cálculo da área do triângulo retângulo
area = (a * b) / 2

# Mostra o resultado final da área calculada
print(f"A área do triângulo retângulo com lados a={a} e b={b} é {area}")