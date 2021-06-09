def wordSearch(words, text):
    if len(text) ==0:
        return True
    
    for i in range(1, len(text)+1):
        potential = text[:1]
        if potential not in words:
            continue
        if wordSearch(words, text[i:]):
            return True
        
    return False

WORDS = ['ala','mama','mam','ma']
TEXT = 'ala'

WORDS = list(map(lambda x: x.lower(), WORDS))
TEXT = TEXT.lower()

print(wordSearch(WORDS, TEXT))