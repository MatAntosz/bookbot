def main():
    filesource="books/frankenstein.txt"
    wordcount = word_count(filesource)
    letters = letter_count(filesource)
    print(f"---Begin report of {filesource}---")
    print(f"{wordcount} words in the document")
    for letter in letters:
        
            print(f"The '{letter[0]}' character was found {letter[1]} times")

def word_count(filesource):
        with open(filesource) as file:
            text = file.read()
            WORDS = text.split()
            return(len(WORDS))

def letter_count(filesource):
        with open(filesource) as file:
            text = file.read()
            strlen = str(text).lower()
            dicti = {}
            for letter in strlen:
                if letter.isalpha():    
                    if letter in dicti:
                        dicti[letter] += 1
                    else:
                        dicti[letter] = 1
            finallist = list(dicti.items())
            finallist.sort(reverse=True, key=lambda tup: tup[1]) 
        return finallist 

main()
