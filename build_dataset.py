import pandas as pd

df = pd.read_csv('4000-most-common-english-words-csv.csv')

# create first column
df['words'] = df['the']
df.drop(columns='the', inplace=True)

# create word length column
def get_word_length(word):
    return len(word)

df['word length'] = df['words'].map(get_word_length)

# create # unique characters column
def count_unique_characters(word):
    seen = []
    unique = 0

    for c in word:
        if c in seen:
            continue
        seen.append(c)
        unique = unique + 1

    return unique

df['# unique characters'] = df['words'].map(count_unique_characters)

# create # non-unique characters column
def count_non_unique_characters(word):
    word_count = {}
    
    for c in word:
        if c not in word_count:
            word_count[c] = 1
        else:
            word_count[c] += 1
        
    return len([c for c in word_count.keys() if word_count[c] > 1])

df['# non-unique characters'] = df['words'].map(count_non_unique_characters)

# create contains repeat characters column 
df['contains repeat characters?'] = df['words'].map(lambda x: count_non_unique_characters(x) > 0)

# create # vowels column
def vowel_count_non_unique(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for c in word:
        if c in vowels:
            count = count + 1
    return count

df['# vowels'] = df['words'].map(vowel_count_non_unique)
print(df['# vowels'])

# create # consonants count
df['# consonants'] = df['words'].map(lambda x: len(x) - vowel_count_non_unique(x))

df.to_csv('words-dataset.csv')