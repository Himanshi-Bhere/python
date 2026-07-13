# test statistics.output should me characters, words, sentences, vowels, consonants print the output of the function with a sample text


def text_statistics(text):
    # count the number of charaters in the text
    count_characters = len(text)
    print(f"Number of characters: {count_characters}")
 
    # count the number of words in the text 
    count_words = len(text.split())
    print(f"Number of words: {count_words}")
    
    # count number of sentences in the text 
    count_sentences = text.count('.') + text.count('!') + text.count('?')  # counting sentences based on punctuation marks
    print(f"Number of sentences: {count_sentences}")
   
    # count vowles in the text 
    count_vowels = sum(1 for char in text if char.lower() in 'aeiou')  # counting vowels (case-insensitive)
    print(f"Number of vowels: {count_vowels}")

 
    # count consonants in the text
    count_consonants = sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')  # counting consonants (case-insensitive)
    print(f"Number of consonants: {count_consonants}")
    

text = input("Please enter a text: ")
text_statistics(text)
