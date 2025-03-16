txt = input("Enter string: ")
vowels = "aeiouAEIOU"

vowel_count = sum(1 for c in txt if c in vowels)

print(vowel_count)