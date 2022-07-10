# 4 A practice question on the Fillword puzzle.
# The condition guarantees that all the words in the list can be crossed out in the
# Fillword puzzle, then to get the answer it is enough to count the number of each letter in
# the crossword puzzle, and then going through the words that are fed to the input,
# reduce the corresponding counter by 1. At the end you just need to display
# the letters on the screen. Try via width or depth search


def fill_word_puzzle(graph, word, filled):
    my_queue = []
    for letter in word:
        my_queue.append(ord(letter) - ord("A"))
    fromV = my_queue[0]

    while my_queue:
        toV = my_queue.pop(0)
        if toV >= len(graph):
            break
        array = graph[toV]
        filled[toV] = True
        if not my_queue or not array[my_queue[0]]:
            break
    if not my_queue:
        print("Found!", end=" ")
        count_letters(graph, filled, fromV)
    else:
        print(f"{word} wasn't found")


def count_letters(graph, filled, fromV):
    print("Frequency of letters:")
    size = len(graph)
    visited = [False] * size
    my_queue = [fromV]
    while my_queue:
        toV = my_queue.pop(0)
        arr = graph[toV]
        print(f"{chr(toV + ord('A'))} with 1" if filled[toV] else f"{chr(toV + ord('A'))} with 0")
        for i in range(size):
            if arr[i] != 0:
                if not visited[i]:
                    my_queue.append(i)
        visited[toV] = True


word_graph = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0]
]

filled = [False] * len(word_graph)
count_letters(word_graph, filled, 0)
fill_word_puzzle(word_graph, "EBCA", filled)

