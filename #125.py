def isPalindrome(s):
    s = ''.join(i if i.isalnum() else '' for i in s)
    s = s.lower()
    l = 0
    while l < int(len(s)/2):
        if s[l] != s[-(l+1)]:
            return False
        l += 1
    return True
