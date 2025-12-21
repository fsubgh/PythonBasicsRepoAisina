def count_vowels(text: str) -> int:
    vowels = "aeiou"
    text_lower = text.lower()

    count = 0
    for char in text_lower:
        if char in vowels:
            count += 1

    return count

if __name__ == "__main__":
    test_string = "Hello World"
    result = count_vowels(test_string)
    print(f"Количество гласных в '{test_string}': {result}")

