import pytest

from stringz import count_characters, uppercase_each_word, split_comma, decorate


def test_uppercase_each_word():
    assert uppercase_each_word('coucou les amis') == 'Coucou Les Amis'
    assert uppercase_each_word('Deja Uppercase') == 'Deja Uppercase'

    with pytest.raises(ValueError):
        uppercase_each_word(123)


def test_count_characters():
    assert count_characters('quelques caracteres') == 19
    assert count_characters('beaucoup plus de caracteres ici dirait-on') == 41

    with pytest.raises(ValueError):
        count_characters(None)


def test_split_comma():
    assert split_comma('Bonjour, cher ami') == ['Bonjour', ' cher ami']
    assert split_comma('Ceci, va, etre, coupe, de partout') == [
        'Ceci', ' va', ' etre', ' coupe', ' de partout'
    ]

    with pytest.raises(ValueError):
        split_comma(["die!"])


def test_decorate():
    assert decorate('Au revoir.') == """Quelle phrase magnifique !
Jugez-en par vous-meme : Au revoir.
N'est-ce pas ?."""

    with pytest.raises(ValueError):
        decorate({"you": "may die"})
