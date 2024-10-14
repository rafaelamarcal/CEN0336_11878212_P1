#!/usr/bin/env python3

# script_popsim.py

def main():
    # Para solicitar o tamanho inicial da população
    while True:
        try:
            P0 = float(input("Digite o tamanho inicial da população: "))
            if P0 <= 0:
                print("Inserir um número positivo.")
                continue
            break
        except ValueError:
            print("Inválido. Por favor, insira um número.")

    # Solicita a taxa de crescimento anual
    while True:
        try:
            r = float(input("Digite a taxa de crescimento anual (número decimal): "))
            if r < 0:
                print("Por favor, insira um número positivo.")
                continue
            break
        except ValueError:
            print("Inválido. Por favor, insira um número.")

    # Solicita o número de anos
    while True:
        try:
            t = int(input("Digite o número de anos: "))
            if t <= 0:
                print("Por favor, insira um número positivo.")
                continue
            break
        except ValueError:
            print("Inválido. Por favor, insira um número.")

    # Calcula e exibe o tamanho da população a cada ano
    for year in range(1, t + 1):
        P = P0 * (1 + r) ** year
        print(f"Ano {year}: {P}")

if __name__ == "__main__":
    main()
