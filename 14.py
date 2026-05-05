# ТВПС 14. Заполняем таблицу снизу, выбираем кол-во бит
# Использует символы: 0, 1, 2
import itertools


# The table's indexing starts from 1 (индексация с 1)
# The rows are qs (строки таблицы ниже - разные q)
# (next_q, output) (следующий q, выходной символ)
transposed_table = (
    ((2, 0), (2, 0), (1, 0)),
    ((2, 1), (5, 1), (1, 0)),
    ((2, 1), (1, 0), (1, 0)),
    ((1, 0), (4, 0), (2, 1)),
    ((4, 0), (1, 1), (1, 0))
)

bits = 3
found = False
while not found:
    word_gen = itertools.product(range(3), repeat=bits)
    for word in word_gen:
        print(word)
        word_results = []
        for starting_q in range(1, len(transposed_table)+1):
            # print(f"q'{starting_q}")
            next_q = transposed_table[starting_q-1][word[0]][0]
            result = str(transposed_table[starting_q-1][word[0]][1])
            # print(next_q)
            # print(result)
            for x in word[1:]:
                result += str(transposed_table[next_q-1][x][1])
                next_q = transposed_table[next_q-1][x][0]
            word_results.append(result)
        print(word_results)
        print(set(word_results))
        if len(word_results) == len(set(word_results)):
            found = True
            print(f'Word found: {word}')
            break
    bits += 1