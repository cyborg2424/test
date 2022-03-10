from collections import Counter

data = open("documents.txt", "r", encoding="utf8")
data_text = data.read()

split = data_text.split()
test_dict = {}
for i in split:
    if i not in test_dict:
        test_dict[i] = 1
    else:
        test_dict[i] += 1

test_dict = sorted(test_dict.items(), key = lambda x: x[1])
test_dict.reverse()