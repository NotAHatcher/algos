def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in t:
        if i not in d:
            return False
        else:
            d[i] -= 1
            if d[i] < 0:
                return False
    return True

print(isAnagram("anagram","nagaram"))