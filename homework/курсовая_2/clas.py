class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return self.word

    def check_word(self, userword):
        if userword in self.subwords:
            return True
        return False

    def subwords_count(self):
        return len(self.subwords)


class Player:
    def __init__(self,name):
        self.name = name
        self.usedwords = []

    def __repr__(self):
        return self.name

    def usedwords_count(self):
        return len(self.usedwords)

    def add_word(self, userword):
        self.usedwords.append(userword)

    def check_used(self, userword):
        if userword in self.usedwords:
            return True
        return False