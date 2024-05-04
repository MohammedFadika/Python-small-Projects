txtfile = open('/Users/mohammed/Desktop/PYTHON /FCC')
print(txtfile)

set_ofwords = dict()

for line in txtfile:
    words = line.split()
    for word in words:
        set_ofwords[word] = set_ofwords.get(word, 0) + 1

print(set_ofwords)


sorted_words = list()
for key,val in set_ofwords.items():
    newtup = (val, key)
    sorted_words.append(newtup)

print("\n\n", sorted_words)
    
sorting = sorted(sorted_words, reverse=True)

most_comm = sorting[:10]
print("\n\n", most_comm)
print ("hello git ")