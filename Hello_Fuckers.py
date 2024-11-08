def separate_vowels_consonants_sorted():
    # Input: Get a name from the user
    name = input("Enter a name: ").strip().lower()

    # Define vowels
    vowels = "aeiou"

    # Initialize lists to store vowels and consonants
    vowel_list = []
    consonant_list = []

    # Process each character in the name
    for char in name:
        if char.isalpha():  # Only process alphabetic characters
            if char in vowels:
                vowel_list.append(char)
            else:
                consonant_list.append(char)

    # Sort vowels and consonants
    vowel_list = sorted(vowel_list)
    consonant_list = sorted(consonant_list)

    # Output: Display vowels and consonants
    print("\nVowels (sorted):")
    print(", ".join(vowel_list) if vowel_list else "None")

    print("\nConsonants (sorted):")
    print(", ".join(consonant_list) if consonant_list else "None")


# Run the program
separate_vowels_consonants_sorted()
