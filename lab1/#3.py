def lengthOfLongestSubstring(s):
    l = 0
    r = 0
    max_length = 0
    sub_s = ''
    while r < len(s):
        a = sub_s.find(s[r])
        if a != -1:
            sub_s = sub_s[a+1:]
            l += a + 1
        sub_s += s[r]
        max_length = max(max_length, r - l + 1)
        r +=1
    return max_length
