class Domino:
    def __init__(self, initial_dominoes):
        self.dominoes = initial_dominoes
        self.current_domino = None
        self.left_neighbor = None
        self.right_neighbor = None

    def next_position_of_dominoes(self, iteration=1):
        for i in range(iteration):
            dominoes_in_words = self.__covert_domino_to_words(self.dominoes)
            new_dominoes = []
            for index, domino in enumerate(dominoes_in_words):
                self.neighbors_of_domino(index, domino, dominoes_in_words)
                self.change_position_next()
                new_dominoes.append(self.current_domino)
            self.dominoes = self.__convert_words_to_domino(new_dominoes)

    def previous_position_of_dominoes(self, iteration=1):
        for i in range(iteration):
            dominoes_in_words = self.__covert_domino_to_words(self.dominoes)
            new_dominoes = []
            for index, domino in enumerate(dominoes_in_words):
                self.neighbors_of_domino(index, domino, dominoes_in_words)
                self.change_position_previous()
                new_dominoes.append(self.current_domino)
            self.dominoes = self.__convert_words_to_domino(new_dominoes)

    def change_position_next(self):
        position = self.current_domino
        if position == 'center':
            if self.left_neighbor == 'right' and self.right_neighbor != 'left':
                position = 'right'
            elif self.right_neighbor == 'left' and self.left_neighbor != 'right':
                position = 'left'
        self.current_domino = position

    def change_position_previous(self):
        position = self.current_domino
        if position == 'right':
            if self.left_neighbor == 'right' and self.right_neighbor != 'right':
                position = 'center'
        elif position == 'left':
            if self.right_neighbor == 'left' and self.left_neighbor != 'left':
                position = 'center'
        self.current_domino = position

    def neighbors_of_domino(self, index, domino, dominoes):
        self.current_domino = domino
        if index == 0:
            self.left_neighbor = None
        else:
            self.left_neighbor = dominoes[index - 1]
        if index == len(dominoes) - 1:
            self.right_neighbor = None
        else:
            self.right_neighbor = dominoes[index + 1]

    @staticmethod
    def __covert_domino_to_words(dominoes):
        dominoes_in_words = []
        for i in dominoes:
            if i == '|':
                dominoes_in_words.append('center')
            elif i == '/':
                dominoes_in_words.append('right')
            elif i == '\\':
                dominoes_in_words.append('left')
        return dominoes_in_words

    @staticmethod
    def __convert_words_to_domino(domino_in_words):
        dominoes = ''
        for word in domino_in_words:
            if word == 'center':
                dominoes += r'|'
            elif word == 'right':
                dominoes += r'/'
            elif word == 'left':
                dominoes += '\\'
        return dominoes
