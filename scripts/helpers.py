import hurry.filesize

def load_text_from_file(path: str):
    """Loads a textfile from the given path and returns it"""
    pass

def generate_text(textsize):
    """Generate text of a given size"""
    pass

def save_text_to_file(text, path):
    """Saves given text""" 
    pass

def utf8len(s):
    return len(s.encode('utf-8'))

def get_file_size(text):
    """Returns file size in MB"""
    return hurry.filesize.size(utf8len(text))

