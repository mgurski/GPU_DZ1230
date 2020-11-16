
def counting_vowels_in_text(text):
    """Returns the number of vowels found in the text"""
    sum=0
    for i in text:
        if (i == 'a'):
           sum+=1
        if (i == 'A'):
           sum+=1
        if (i == 'e'):
           sum+=1
        if (i == 'E'):
           sum+=1
        if (i == 'i'):
           sum+=1
        if (i == 'I'):
           sum+=1
        if (i == 'o'):
           sum+=1
        if (i == 'O'):
           sum+=1
        if (i == 'u'):
           sum+=1
        if (i == 'U'):
           sum+=1
        if (i == 'y'):
           sum+=1
        if (i == 'Y'):
           sum+=1


    #print(sum)
    return sum
