"""Main module for tests."""
from pytest import raises

from scrabble import scrabble_sentence


def test_empty_sentence_handled_correctly():
    """Test that empty strings are handled correctly."""
    with raises(Exception, match='Incorrect word not valid: '):
        scrabble_sentence('')


def test_white_space():
    """Test whitespaces are handled correctly."""
    with raises(Exception, match='Incorrect word not valid: '):
        scrabble_sentence('test  test')


def test_scrabble_sentence():
    """Test that the scrabble_sentence returns random sentences."""
    test_sentence = 'this test sentence should differ'
    result = scrabble_sentence(test_sentence)
    result_2 = scrabble_sentence(test_sentence)
    assert result != result_2
