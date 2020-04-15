"""
Main:
    A simple program that allows testing of nose2
"""

def printWords(words):
    """
    Takes a list of words and prints them individually.

    Parameters
    ----------
    words : List of strings to be printed.

    """
    for word in words:
        print(word)
        
    return words

def printTupleWords(words):
    """
    Takes a tuple of words and prints each letter individually.

    Parameters
    ----------
    words : Tuple of strings to be printed.

    """
    for word in words:
        print(word)
        
    return words
        
def main():
    """
    Main function.

    """
    words = ("Hello", "World!")
    printWords(words)
    

if __name__ == "__main__":
    main()
