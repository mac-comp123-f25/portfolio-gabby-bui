def nextWord(text):
    """
    Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next
    sequence of characters up to a space, tab, or newline.
    """
    wordStr = ""
    i = 0
    for ch in text:
        if ch in " \t\n":  # if character is space, tab (\t), or newline (\n)
            break
        else:
            wordStr = wordStr + ch

    return print(wordStr)

nextWord("apiu and gabby")