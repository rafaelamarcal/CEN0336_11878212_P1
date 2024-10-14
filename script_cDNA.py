#!/usr/bin/env python3
# Importa a biblioteca sys para pegar os argumentos que o usuário vai passar
import sys

# Função que vai conferir se os argumentos estão certinhos
def validar_entrada(args):
    # O primeiro argumento tem que ser a sequência de DNA (uma string)
    dna_sequence = args[1]
    
    # Os outros seis precisam ser números inteiros e menores que o tamanho do DNA
    for i in range(2, 8):
        if not args[i].isdigit():  # Vê se o argumento é um número
            print(f"Erro: O argumento {args[i]} não é um número inteiro.")
            return False
        if int(args[i]) > len(dna_sequence):  # Confere se o número não é maior que o DNA
            print(f"Erro: O valor {args[i]} é maior que o tamanho da sequência de DNA.")
            return False
    return True

# Função principal que vai rodar tudo
def main():
    # Vê se o número certo de argumentos foi passado
    if len(sys.argv) != 8:
        print("Erro: O número de argumentos está incorreto. Você deve passar 7 argumentos.")
        return
    
    # Pegando os argumentos
    dna_sequence = sys.argv[1]
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    n3 = int(sys.argv[4])
    n4 = int(sys.argv[5])
    n5 = int(sys.argv[6])
    n6 = int(sys.argv[7])
    
    # Chama a função para validar os argumentos
    if not validar_entrada(sys.argv):
        return

    # Pegando as partes do DNA entre CDS1 e CDS2, e entre CDS2 e CDS3
    intron1 = dna_sequence[n2:n3]
    intron2 = dna_sequence[n4:n5]
    
    # Verifica se essas partes começam com GT e terminam com AG
    if intron1.startswith('GT') and intron1.endswith('AG'):
        print("A sequência entre CDS1 e CDS2 está correta (GT...AG).")
    else:
        print("Erro: A sequência entre CDS1 e CDS2 não começa com GT ou não termina com AG.")
        return
    
    if intron2.startswith('GT') and intron2.endswith('AG'):
        print("A sequência entre CDS2 e CDS3 está correta (GT...AG).")
    else:
        print("Erro: A sequência entre CDS2 e CDS3 não começa com GT ou não termina com AG.")
        return
    
    # Se estiver tudo certo, junta as partes das CDS
    cds1 = dna_sequence[n1:n2]
    cds2 = dna_sequence[n3:n4]
    cds3 = dna_sequence[n5:n6]
    
    # Junta as três CDS
    resultado = cds1 + cds2 + cds3
    
    # Mostra a sequência final
    print("A sequência resultante da junção das CDS 1, CDS 2 e CDS 3 é:")
    print(resultado)

# Faz o script rodar se for executado diretamente
if __name__ == "__main__":
    main()
