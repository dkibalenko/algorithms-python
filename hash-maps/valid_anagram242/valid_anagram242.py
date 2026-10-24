# Input: s = "anagram", t = "nagaram"
# Output: true

def is_anagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    sorted_s = sorted(s) 
    sorted_t = sorted(t)

    return sorted_s == sorted_t


print(is_anagram1("anagram", "nagaram"))


def is_anagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
    return count_s == count_t
