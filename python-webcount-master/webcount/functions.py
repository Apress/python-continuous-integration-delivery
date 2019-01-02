import requests

def most_common_word_in_web_page(words, url):
    """
    finds the most common word from a list of words
    in a web page, identified by its URL
    """
    response = requests.get(url)
    return most_common_word(words, response.text)
    

def most_common_word(words, text):
    """
    finds the most common word from a list of words
    in a piece of text
    """
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]
