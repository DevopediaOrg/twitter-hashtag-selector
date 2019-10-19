import spacy

sp = spacy.load('en_core_web_sm')

def pharse_collector(sentence):
    """
    returns proper noun using spacy library
    # TODO: Proper noun + verb combinations
    """
    data = sp(sentence)
    print(data)
    results = [word.text.lower() for word in data if word.pos_ == "PROPN" or word.pos_ == "NOUN"] 
    return results
