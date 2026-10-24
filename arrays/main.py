
def test(string: str) -> bool:  # "MCMXCIV"
    roman_base = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total_int = 0

    # two pointers
    for left in range(len(string)):
        right = left + 1
        if right < len(string) and roman_base[string[left]] < roman_base[string[right]]:
            total_int -= roman_base[string[left]]
        else:
            total_int += roman_base[string[left]]
    
    return total_int


if __name__ == "__main__":
    print(test("LVIII"))
    print(test("MCMXCIV"))
