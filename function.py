S = input('Please enter a string : ')
import operator
def most_frequent(string):
    d = dict()
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    d = dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))

    return d

print(most_frequent(S))
