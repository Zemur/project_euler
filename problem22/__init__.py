"""
Using p022_names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def name_score(name, pos):
    return pos * sum([ord(c) - 64 for c in name])


if __name__ == '__main__':
    with open('./p022_names.txt', 'r') as f:
        names = sorted(f.read().replace('"', '').split(','))

    print(sum([name_score(i, names.index(i)+1) for i in names]))
