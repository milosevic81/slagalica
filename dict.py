import sys

def getletters(word):
    r = {}
    for letter in word:
        r[letter] = r.get(letter, 0) + 1
    return r

def check(word, available):
    letters = getletters(word.strip())
    for letter, need in letters.items():
        have = available.get(letter, 0)
        if have < need:
            return False
    return True

def scan(available):
    with open('sr.dic', 'r') as f:
        return [word for word in f if check(word, available)]

def solve(letters):
    s = getletters(letters)
    results = scan(s)
    maxlen = len(max(results, key=len))
    return [w for w in results if len(w) == maxlen]

s = solve(sys.argv[1])
if s:
    s.sort()
    print(len(s[0]), s)
