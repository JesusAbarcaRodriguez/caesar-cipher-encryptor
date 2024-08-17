from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import random
class MainView(QMainWindow):
    def __init__(self):  # this
        super(MainView, self).__init__()
        uic.loadUi("view/view.ui", self)
        self.encryptButton.clicked.connect(self.encrypt_text)

    def encrypt_text(self):
        text_to_encrypt = self.textToEncrypt.toPlainText()


        key_input = self.keyInput.toPlainText()


        cipher_type = self.cipherType.currentText()
        if cipher_type == "Cifrado César":
           self.generate_custom_alphabet(key_input, text_to_encrypt)
        elif cipher_type == "Cifrado Vigenère":
            print("Cifrado Vigenère")
        # Mostrar el texto cifrado en el campo de salida
        

    def generate_custom_alphabet(self, key, text):
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        alphabet_aux = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        key = ''.join(sorted(set(key), key=key.index))

        for char in key:
            alphabet = alphabet.replace(char, "")

        index_random = random.randint(0, len(alphabet))

        custom_alphabet = alphabet[:index_random] + key + alphabet[index_random:]

        encrypted_text = ""
        for char in text:
            if char in alphabet_aux:
                pos = alphabet_aux.index(char)
                encrypted_text += custom_alphabet[pos]
            else:
                encrypted_text += char

        self.decryptedText.setPlainText(alphabet_aux + "\n" +custom_alphabet + "\n" +encrypted_text)

