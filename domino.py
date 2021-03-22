import unittest
from typing import List


class Domino():
    def __init__(self, Initial_dominos):
        self.dominos = Initial_dominos


    def next_iteral(self, iterals=1):
        for i in range(iterals):
            dominos_in_words = self.__covert_domino_to_words(self.dominos)
            new_dominos = []
            for index, domino in enumerate(dominos_in_words):
                if index == 0:
                    left_neighbor = None
                else:
                    left_neighbor = dominos_in_words[index - 1]
                if index == len(dominos_in_words) - 1:
                    right_neighbor = None
                else:
                    right_neighbor = dominos_in_words[index + 1]
                position = domino

                if position == 'center':
                    if left_neighbor == 'right' and right_neighbor != 'left':
                        position = 'right'
                    elif right_neighbor == 'left' and left_neighbor != 'right':
                        position = 'left'
                new_dominos.append(position)
            self.dominos = self.__convert_rowrds_to_domino(new_dominos)



    def previous_iteral(self, iterals=1):
        for i in range(iterals):
            dominos_in_words = self.__covert_domino_to_words(self.dominos)
            new_dominos = []
            for index, domino in enumerate(dominos_in_words):
                if index == 0:
                    left_neighbor = None
                else:
                    left_neighbor = dominos_in_words[index - 1]
                if index == len(dominos_in_words) - 1:
                    right_neighbor = None
                else:
                    right_neighbor = dominos_in_words[index + 1]
                position = domino

                if position == 'right':
                    if left_neighbor == 'right' and right_neighbor != 'right':
                        position = 'center'
                elif position == 'left':
                    if right_neighbor == 'left' and left_neighbor != 'left':
                        position = 'center'
                new_dominos.append(position)

            self.dominos = self.__convert_rowrds_to_domino(new_dominos)




    def change_position(domino, direction):
        if direction == 'right':
            if domino == 'left':
                return 'center'
            if domino == 'center':
                return 'right'
        if direction == 'left':
            if domino == 'right':
                return 'center'
            if domino == 'center':
                return 'left'


    def __covert_domino_to_words(self, dominos):
        dominos_in_words = []
        for i in dominos:
            if i == '|':
                dominos_in_words.append('center')
            elif i == '/':
                dominos_in_words.append('right')
            elif i == '\\':
                dominos_in_words.append('left')
        return dominos_in_words

    def __convert_rowrds_to_domino(self, domino_in_words):
        dominos = ''
        for word in domino_in_words:
            if word == 'center':
                dominos += (r'|')
            elif word == 'right':
                dominos += (r'/')
            elif word == 'left':
                dominos += ('\\')
        return dominos

domino = Domino(r'/||||\\')
print(domino.dominos)
domino.next_iteral(2)
domino.previous_iteral(4)
print(domino.dominos)
