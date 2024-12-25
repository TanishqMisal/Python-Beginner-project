#PIG LATIN TRANSLATOR PROJECT


# get sentence from user

original = input("TYPE A SENTENCE:").strip().lower()

# split sentence into words

words = original.split()

# loop through words and convert to pig latin

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "YaY"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        new_word = rest + cons + "aY"
        new_words.append(new_word)
            

# stick words back together

output = " ".join(new_words)

#display the output

print(output)
