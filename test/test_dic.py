import pytest

def test__count_words_from_file__return_word_pair_dic__when_read_txt_file():
    text_from_file = "hola soy Italo"

    expected_word_pair_dic = {
        "hola" : 1,
        "soy" : 1,
        "Italo" : 1,
    }

    word_pair_dic = count_words_from_file(text_from_file)

    assert expected_word_pair_dic == word_pair_dic