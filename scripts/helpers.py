import hurry.filesize
import string
import random

def generate_text(length: int):
    letters = string.ascii_letters + string.whitespace.replace('\x0b\x0c','') + 'ąĄęĘóÓżŻźŹćĆńŃśŚłŁ'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def load_text_from_file(path: str):
    """Loads a textfile from the given path and returns it"""
    pass

def save_text_to_file(text: str, path: str):
    file = open(path, "w")
    file.write(text)
    file.close
    
def utf8len(s):
    return len(s.encode('utf-8'))

def get_file_size(text):
    """Returns file size in MB"""
    return hurry.filesize.size(utf8len(text))