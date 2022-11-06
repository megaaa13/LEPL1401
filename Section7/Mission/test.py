from search import *


def test_readfile():
    assert readfile('text_example_1.txt') == ["I'm nobody!\n", "Who are you?"], 'The test of readfile gave an error'
    assert readfile('text_example_2.txt') == ["The steamer's course\n", "had been slightly\n",
                                              "altered in the night"], 'The test of readfile gave an error'


def test_getwords():
    assert get_words(readfile('text_example_1.txt')[0]) == ['i', 'm', 'nobody'], 'The test of get_words gave an error'
    assert get_words(readfile('text_example_2.txt')[0]) == ['the', 'steamer', 's',
                                                            'course'], 'The test of get_words gave an error'


def test_createindex():
    assert create_index('text_example_1.txt') == {'i': {0: 1}, 'm': {0: 1}, 'nobody': {0: 1}, 'who': {1: 1},
                                                  'are': {1: 1},
                                                  'you': {1: 1}}, 'The test of create_index gave an error'
    assert create_index('text_example_2.txt') == {'the': {0: 1, 2: 1}, 'steamer': {0: 1}, 's': {0: 1}, 'course': {0: 1},
                                                  'had': {1: 1}, 'been': {1: 1}, 'slightly': {1: 1}, 'altered': {2: 1},
                                                  'in': {2: 1},
                                                  'night': {2: 1}}, 'The test of create_index gave an error'


def test_getlines():
    assert get_lines(['i', 'm', 'nobody'], create_index('text_example_1.txt')) == [0], 'Test of get_lines gave an error'
    assert get_lines(['the', 'steamer', 's'], create_index('text_example_2.txt')) == [
        0], 'Test of get_lines gave an error'


if __name__ == '__main__':
    print('Test a function: ')
    try:
        while True:
            entry = input('> ')
            if entry == 'readfile':
                test_readfile()
                print('The function "readfile" works')
            elif entry == 'getwords':
                test_getwords()
                print('The function "getwords" works')
            elif entry == 'createindex':
                test_createindex()
                print('The function "createindex" works')
            elif entry == 'getlines':
                test_createindex()
                print('The function "get lines" works')
    except:
        print('An error occurred')
