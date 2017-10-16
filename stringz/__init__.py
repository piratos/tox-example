import jinja2


def uppercase_each_word(string):
    """Uppercase the first letter of each word."""
    if type(string) is not str:
        raise ValueError("This is not a string")

    return string.title()


def count_characters(string):
    """Return the amount of characters in the string."""
    if type(string) is not str:
        raise ValueError("This is not a string")

    return len(string)


def split_comma(string):
    """Split the string at the comma and return the list."""
    if type(string) is not str:
        raise ValueError("This is not a string")

    return string.split(',')


def decorate(string):
    """Add text around the string to "decorate" it."""
    if type(string) is not str:
        raise ValueError("This is not a string")

    text = """Quelle phrase magnifique !
Jugez-en par vous-meme : {{sentence}}
N'est-ce pas ?"""

    return jinja2.Environment().from_string(text).render(sentence=string)
