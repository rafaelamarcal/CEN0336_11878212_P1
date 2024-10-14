#!/usr/bin/env python3
# script_CDS.py

import sys

def main():
    # Checa se o número certo de argumentos foi passado
    if len(sys.argv) != 8:
        print("Uso: escreva a sequência de DNA <sequência_DNA> e as coordenadas <n1> <n2> <n3> <n4> <n5> <n6>")
        sys.exit(1)

    # Pega a sequência de DNA e os números inteiros dos argumentos
    dna_sequence = sys.argv[1]
    indices = sys.argv[2:8]

    # Confere se a sequência de DNA é válida
    if not isinstance(dna_sequence, str):
        print("O primeiro argumento precisa ser uma string com a sequência de DNA.")
        sys.exit(1)

    # Tenta converter os índices para inteiros e checa se tá tudo certo
    try:
        n_indices = [int(n) for n in indices]
    except ValueError:
        print("Os últimos seis argumentos têm que ser números inteiros.")
        sys.exit(1)

    # Verifica se algum índice é maior que o tamanho da sequência
    if any(n > len(dna_sequence) for n in n_indices):
        print("Nenhum índice pode ser maior que o tamanho da sequência de DNA.")
        sys.exit(1)

    # Pega as sequências entre as CDS
    cds1 = dna_sequence[n_indices[0]:n_indices[1]]
    cds2 = dna_sequence[n_indices[2]:n_indices[3]]
    cds3 = dna_sequence[n_indices[4]:n_indices[5]]

    # Pega a sequência entre CDS 1 e CDS 2
    sequence_12 = dna_sequence[n_indices[1]:n_indices[2]]
    starts_with_gt_12 = sequence_12.startswith("GT")
    ends_with_ag_12 = sequence_12.endswith("AG")

    # Pega a sequência entre CDS 2 e CDS 3
    sequence_23 = dna_sequence[n_indices[3]:n_indices[4]]
    starts_with_gt_23 = sequence_23.startswith("GT")
    ends_with_ag_23 = sequence_23.endswith("AG")

    # Verifica as condições e imprime a sequência resultante se tudo estiver ok
    if starts_with_gt_12 and ends_with_ag_12 and starts_with_gt_23 and ends_with_ag_23:
        # Junta as CDS
        result_sequence = cds1 + cds2 + cds3
        print("Sequência resultante da concatenação:", result_sequence)
    else:
        print("As sequências entre as CDS não estão começando e terminando como esperado.")

if __name__ == "__main__":
    main()
