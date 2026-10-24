def is_valid(string: str) -> bool:
    stack = []  # Time O(1) for push/pop, Space O(n)

    # single pass Time O(n), all work (comparisons, etc.) O(1)
    for char in string:
        # openning char is added to stack ("{([(...")
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        # any closing char - check if the last is matching one, and pop from stack
        elif char == ")" and stack and stack[-1] == "(":
            stack.pop()
        elif char == "]" and stack and stack[-1] == "[":
            stack.pop()
        elif char == "}" and stack and stack[-1] == "{":
            stack.pop()
        else:
            # not matching to openning char or starts with closing char
            return False

    # stack is empty - all parethesis are matching
    return not stack


def is_valid2(string: str) -> bool:
    stack = []  # LIFO -> keep correct ordering of open-close chars (e.g. "{([({})])}")
    # closing char only maps to its correct type opening one
    valid_mappings = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in valid_mappings:  # closing char is valid...
            # ...and, there's correct opening char in stack
            if stack and stack[-1] == valid_mappings[char]:
                stack.pop()  # eliminate correct char pair
            else:
                return False  # invalid char mapping
        else:
            # ...or, opening char is always added to stack
            stack.append(char)

    return True if not stack else False


print(is_valid2("([{}])"))
# print(is_valid2("[(])"))
