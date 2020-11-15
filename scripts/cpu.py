def counting_vowels_in_text(text: str):
    """Returns the number of vowels found in the text?"""
    result = 0
    for i in range(text.__len__()):
        if (text[i] == 'a' or text[i] == 'A' or text[i] == 'ą' or text[i] == 'Ą' or text[i] == 'e' or text[i] == 'E'
        or text[i] == 'ę' or text[i] == 'Ę' or text[i] == 'i' or text[i] == 'I' or text[i] =='o' or text[i] =='O'
        or text[i] == 'u' or text[i] == 'U' or text[i] == 'y' or text[i] == 'Y'):
                result += 1
    return result