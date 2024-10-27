#!/usr/bin/env python3

# class MyString:
#   pass
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        return len([sentence for sentence in sentences if sentence.strip()])

# Example usage:
my_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(my_string.is_sentence())  # False
print(my_string.is_question())  # False
print(my_string.is_exclamation())  # False
print(my_string.count_sentences())  # 4
