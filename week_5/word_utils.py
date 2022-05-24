def remove_punctuation_marks(sentence, add_signs=''):
    """Принимает на вход строку и удаляет из нее знаки препинания(.,;:!?'"-).
    Возвращает новую строку без этих знаков.
    В переменной add_signs можно передать дополнительные символы, которые будут
    удалены из строки."""

    # символ "-" является особым случаем, так как может выступать в двух
    # контекстах: дефис и тире. Дефис окружен буквами и его нужно просто
    # удалить. Тире окружен пробелами, и все три символа " - " нужно заменить
    # на один пробел
    if '-' in sentence:
        sentence = sentence.replace(' - ', ' ')
        sentence = sentence.replace('-', ' ')
    signs = '.,;:!?\'"'
    return sentence.translate(''.maketrans(dict.fromkeys(signs+add_signs)))


def create_word_list(sentence):
    """Принимает на вход строку и возвращает список со словами из этой
    строки."""

    return remove_punctuation_marks(sentence).split()


def find_longest_word(sentence):
    """Принимает на вход строку и возвращает самое длинное слово из этой
    строки."""

    word_list = create_word_list(sentence)
    word_list_with_length = ((len(w), w) for w in word_list)
    return max(word_list_with_length)[1]
