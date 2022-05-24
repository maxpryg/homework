import unittest
from word_utils import remove_punctuation_marks, create_word_list
from word_utils import find_longest_word


class TestRemovePunctuationMarks(unittest.TestCase):
    def test_remove_all_signs(self):
        self.input_sentence = '\'Ok\'. a, b; all: "yes!" sure? hey-hey'
        self.correct_sentence = 'Ok a b all yes sure hey hey'
        self.output_sentenct = remove_punctuation_marks(
            self.input_sentence, add_signs='#()')
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_additional_signs(self):
        self.input_sentence = '(#ilikepython.)'
        self.correct_sentence = 'ilikepython'
        self.output_sentenct = remove_punctuation_marks(
            self.input_sentence, add_signs='#()')
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_point(self):
        self.input_sentence = 'I like English.'
        self.correct_sentence = 'I like English'
        self.output_sentenct = remove_punctuation_marks(self.input_sentence)
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_comma(self):
        self.input_sentence = 'I speak English, French, Thai'
        self.correct_sentence = 'I speak English French Thai'
        self.output_sentenct = remove_punctuation_marks(self.input_sentence)
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_semi_colon(self):
        self.input_sentence = 'I often go swimming; I also play tennis'
        self.correct_sentence = 'I often go swimming I also play tennis'
        self.output_sentenct = remove_punctuation_marks(self.input_sentence)
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_colon(self):
        self.input_sentence = 'You have two choices: a or b'
        self.correct_sentence = 'You have two choices a or b'
        self.output_sentenct = remove_punctuation_marks(self.input_sentence)
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_ellipsis_mark(self):
        self.input_sentence = 'This is... ok'
        self.correct_sentence = 'This is ok'
        self.output_sentenct = remove_punctuation_marks(self.input_sentence)
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_exclamation_mark(self):
        self.input_sentence = "I can swim!"
        self.correct_sentence = "I can swim"""
        self.output_sentenct = remove_punctuation_marks(self.input_sentence)
        self.assertEqual(self.correct_sentence, self.output_sentenct)

    def test_remove_question_mark(self):
        self.input_sentence = 'Who are you?'
        self.correct_sentence = 'Who are you'
        self.output_sentenct = remove_punctuation_marks(self.input_sentence)
        self.assertEqual(self.correct_sentence, self.output_sentenct)


if __name__ == '__main__':
    unittest.main()
