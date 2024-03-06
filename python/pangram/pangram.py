def is_pangram(sentence):
    alpha_chars = [char for char in sentence.lower() if char.isalpha()]
    return len(set(alpha_chars)) == 26
