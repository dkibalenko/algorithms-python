def longest_substring(string: str) -> int:
    # brute force O(n^2)
    result = 0

    for i in range(len(string)):  # set 'i' pointer (slow)
        char_set = set()  # keep current substing
        for j in range(i, len(string)):  # set 'j' pointer (fast)
            if string[j] in char_set:  # once 'j' hits duplicate...
                break  # ...stop building substring
            char_set.add(string[j])  # build substring by adding to set
        result = max(result, len(char_set))  # update best substring length
    return result


def longest_substring2(string: str) -> int:
    # sliding window
    char_set: set = set()
    result: int = 0
    left: int = 0

    for right in range(len(string)):
        while string[right] in char_set:  # hit a duplicate (shrink)
            # shrink from the left repeatedly until the duplicate is gone
            char_set.remove(string[left])
            left += 1
        # add the new char
        char_set.add(string[right])
        # update best result - longest substring
        result = max(result, right - left + 1)
    
    return result


print(longest_substring("abcabcbb"))
