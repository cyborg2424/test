from collections import Counter

def document_analyzer():
    freq = Counter()
    with open('document.txt') as file:
        for line in file:
            freq.update(line.split())
    mFreq = sorted(freq.most_common(5), key = lambda x: (-x[1], x[0]))
    print('\r')
    for (word, count) in mFreq:
        print(f'{word:{count}}')

document_analyzer()
