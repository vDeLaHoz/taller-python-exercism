def is_pangram(sentence):
    alfab = set([ord(ch) for ch in "abcdefghijklmnopqrstuvwxyz"])
    sentenc = set([ord(ch) for ch in sentence.lower()])
    return alfab.issubset(sentenc)
