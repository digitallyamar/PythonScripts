import sys

def count_syllables(word):
    vowels = "aeiouy"
    word = word.lower()
    syll_count = 0
    
    if word[0] in vowels:
        syll_count += 1
    
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syll_count += 1
    
    if word.endswith('e'):
        syll_count -= 1
    if syll_count == 0:
        syll_count += 1
    
    return syll_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Usage: python syllable_count.py <word>")
        sys.exit(0)

    word = sys.argv[1]
    print (word)
    syll_count = count_syllables(word)
    print ("The word: " + word + " has " + str(syll_count) + " syllables in it.")