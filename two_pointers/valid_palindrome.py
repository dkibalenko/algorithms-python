def is_palindrome(string: str) -> bool:
    result_string = ""  # build a new string skipping non-alphanums

    for char in string:
        if char.isalnum():  # allow anly letters & numbers
            result_string += char.lower()

    return result_string == result_string[::-1]


def is_palindrome2(string: str) -> bool:
    left, right = 0, len(string) - 1  # two pointers at both ends

    while left < right:
        # move pointers, to make sure both chars are alphanumeric
        while left < right and not is_alpha_num(string[left]):  # move left if not alphanumberic
            left += 1
        while left < right and not is_alpha_num(string[right]):  # move right if not alphanumeric
            right -= 1

        # compare alphanumeric chars at both pointers
        if string[left].lower() != string[right].lower():
             return False  # when chars don't match - it's not a palindrome

        # move pointers to each other
        left, right = left + 1, right - 1

    # loop with test is done, means it's a palindrome
    return True


def is_palindrome3(string: str) -> bool:
    string = string.lower()
    left = 0  # at the start
    right = len(string) - 1  # at the end

    # move pointers until they meet
    while left < right:
        # skip non-alphanumeric char
        if not string[left].isalnum():
            left += 1
            continue
        if not string[right].isalnum():
            right -= 1
            continue

        if string[left] != string[right]:
            return False
        
        left += 1
        right -= 1

    return True


def is_alpha_num(char: str) -> bool:
    return (
        ord('A') <= ord(char) <= ord('Z')
        or ord('a') <= ord(char) <= ord('z')
        or ord('0') <= ord(char) <= ord('9')
    )

print(is_palindrome3("A man, a plan, a canal: Panama"))
print(is_palindrome3("race a car"))
print(is_palindrome3(" "))
