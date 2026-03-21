def getPalindrome(s, cur_s, cur, l, r):
    f = 1
    while f:
        l += 1
        r += 1
        if cur - l >= 0 and cur + r < len(s) and s[cur - l] == s[cur + r]:
            cur_s = s[cur - l] + cur_s + s[cur + r]
        else:
            f = 0
    return cur_s


def longestPalindrome(s):
    max_s = ''
    for cur in range(len(s)):
        if cur + 1 < len(s) and s[cur] == s[cur + 1]:
            cur_s = getPalindrome(s, s[cur] + s[cur + 1], cur, 0, 1)
            if len(cur_s) > len(max_s):
                max_s = cur_s
        cur_s = getPalindrome(s, s[cur], cur, 0, 0)
        if len(cur_s) > len(max_s):
            max_s = cur_s
    return max_s