"""Functions for creating, transforming, and adding prefixes to strings."""
from typing import List


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un' + word


def make_word_groups(vocab_words: List[str]) -> str:
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
    by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    if len(vocab_words) < 1:
        raise ValueError('The list of of vocab words must be at least 1 long')

    prefix = vocab_words[0]

    new_words = [prefix + word for word in vocab_words[1:]]
    new_words.insert(0, prefix)

    return ' :: '.join(new_words)


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    word_without_suffix = word[:-4]

    if word_without_suffix[-1] == 'i':
        word_without_suffix = word_without_suffix[:-1] + 'y'

    return word_without_suffix


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    words_in_sentence = sentence.split(' ')
    word_to_verbify = words_in_sentence[index]

    # handle word at the end of the sentence
    if word_to_verbify[-1] == '.':
        word_to_verbify = word_to_verbify[:-1]
    
    return word_to_verbify + 'en'