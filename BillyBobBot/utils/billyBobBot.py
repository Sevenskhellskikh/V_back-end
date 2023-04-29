class BillyBobBot:
    def __init__(self, message, key):
        self.message = message
        self.key = key
        self.alphabet = alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.encrypted = ""

    def __encrypt_word(self):
        if self.message:
            message = self.message.lower()
            for letter in message:
                position = self.alphabet.find(letter)
                new_position = position + self.key
                if letter in self.alphabet:
                    self.encrypted += self.alphabet[new_position]
                else:
                    self.encrypted += letter
            return self.encrypted

    @property
    def encrypt(self):
        return self.__encrypt_word()