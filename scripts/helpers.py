import hurry.filesize
import string
import random
import lorem
import math

def generate_text(length: int):
    letters = string.ascii_letters + string.whitespace.replace('\x0b\x0c','') + 'ąĄęĘóÓżŻźŹćĆńŃśŚłŁ'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def generate_text_in_mb(size: int):
    text = generate_text(1000)
    size = size * 1000000
    text = text*math.ceil((size/int(1000)))
    return text

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