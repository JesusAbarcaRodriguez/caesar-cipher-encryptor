from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
import random
import tkinter as tk
from tkinter import messagebox

class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        uic.loadUi("view/view.ui", self)
        self.encryptButton.clicked.connect(self.encrypt_text)
        self.cipherType.currentIndexChanged.connect(self.toggle_key_input)

    def toggle_key_input(self):
        cipher_type = self.cipherType.currentText()
        if cipher_type == "Cifrado César con secuencia":
            self.keyLabel.setText("Elegir número de secuencia:")
            self.keyInput.setPlaceholderText("Ingrese un número (1-25)")
            self.keyInput.show()
            self.keyLabel.show()
        else:
            self.keyLabel.setText("Clave:")
            self.keyInput.setPlaceholderText("")
            self.keyInput.show()
            self.keyLabel.show()

    def encrypt_text(self):
        text_to_encrypt = self.textToEncrypt.toPlainText()
        cipher_type = self.cipherType.currentText()

        if cipher_type == "Cifrado César con secuencia":
            try:
                sequence_number = int(self.keyInput.text())
                if 1 <= sequence_number <= 25:
                    self.generate_cesar_cipher_with_sequence(text_to_encrypt, sequence_number)
                else:
                    self.show_error_message("Por favor ingrese un número válido (1-25).")
            except ValueError:
                self.show_error_message("Por favor ingrese un número válido.")
        else:
            key_input = self.keyInput.text()
            if cipher_type == "Cifrado César":
                self.generate_cesar_cipher(key_input, text_to_encrypt)
            elif cipher_type == "Cifrado Vigenère":
                self.generate_vigenere_cipher(key_input, text_to_encrypt)
        

    def generate_cesar_cipher(self, key, text):
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        alphabet_aux = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        key = ''.join(sorted(set(key), key=key.index))

        key = key.upper()
        text = text.upper()

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

    def generate_vigenere_cipher(self, key, text):
        vigenere_matrix = []
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        encrypted_text = ""
        key = key.upper()
        text = text.upper()

        for i in range(len(alphabet)):
            row = alphabet[i:] + alphabet[:i]
            vigenere_matrix.append(list(row))

        countText = 0
        countKey = 0

        while countText < len(text):
            j = 0
            while j < len(alphabet):
                if text[countText] == vigenere_matrix[0][j]:
                    i = 0
                    while i < len(alphabet):
                        if key[countKey] == vigenere_matrix[i][0]:
                            encrypted_text += vigenere_matrix[i][j]
                            countText += 1
                            countKey = (countKey + 1) % len(key)
                            break
                        i += 1
                    break
                j += 1

        self.decryptedText.setPlainText(encrypted_text)

    def generate_cesar_cipher_with_sequence(self, text_to_encrypt, sequence):
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        alphabet_with_secuence = alphabet[sequence:] + alphabet[:sequence]
        encrypted_text = ""
        for char in text_to_encrypt:
            if char in alphabet:
                pos = alphabet.index(char)
                encrypted_text += alphabet_with_secuence[pos]
            else:
                encrypted_text += char
            
        self.decryptedText.setPlainText(alphabet + "\n" +alphabet_with_secuence + "\n" +encrypted_text)

    def show_error_message(self,message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", message)