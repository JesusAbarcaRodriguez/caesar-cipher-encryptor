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
        self.decryptButton.clicked.connect(self.desencrypt_text)

    def toggle_key_input(self):
        cipher_type = self.cipherType.currentText()
        if cipher_type == "Cifrado César con secuencia":
      
            self.keyInput.hide()
            self.keyLabel.hide()
        else:
            self.keyLabel.setText("Clave:")
            self.keyInput.setPlaceholderText("")
            self.keyInput.show()
            self.keyLabel.show()

    def encrypt_text(self):
        text_to_encrypt = self.textToEncrypt.toPlainText().upper()
        cipher_type = self.cipherType.currentText()

        if cipher_type == "Cifrado César con secuencia":
            try:
                sequence_number = random.randint(1, 27)
                self.generate_cesar_cipher_with_sequence(text_to_encrypt, sequence_number)
            
            except ValueError:
                self.show_error_message("Por favor ingrese un número válido.")
        else:
            key_input = self.keyInput.text()
            if cipher_type == "Cifrado César con palabra clave":
                self.generate_cesar_cipher(key_input, text_to_encrypt)
            elif cipher_type == "Cifrado Vigenère":
                self.generate_vigenere_autoclave_cipher(key_input, text_to_encrypt)
    
    def desencrypt_text(self):
        text_to_desencrypt = self.decryptedText.toPlainText().upper()
        cipher_type = self.cipherType.currentText()

        if cipher_type == "Cifrado César con secuencia":
            try:    
                self.brute_force_cesar_cipher(text_to_desencrypt)
            except ValueError:
                self.show_error_message("Por favor ingrese un número válido.")
        else:
            key_input = self.keyInput.text()
            if cipher_type == "Cifrado César con palabra clave":
                self.brute_force_cesar_cipher_with_key(text_to_desencrypt, key_input)
            elif cipher_type == "Cifrado Vigenère":
                self.show_error_message("No se puede desencriptar un cifrado Vigenère.")
        
    def brute_force_cesar_cipher(self, encrypted_text):
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        results = []

        for sequence in range(1, 28):
            decrypted_text = ""
            alphabet_with_secuence = alphabet[sequence:] + alphabet[:sequence]
            for char in encrypted_text:
                if char in alphabet_with_secuence:
                    pos = alphabet_with_secuence.index(char)
                    decrypted_text += alphabet[pos]
                else:
                    decrypted_text += char

            results.append(f"Desplazamiento {sequence}: {decrypted_text}")

        self.textToEncrypt.setPlainText("\n\n".join(results))
        
    def brute_force_cesar_cipher_with_key(self, encrypted_text, key):
        alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        results = []

        
        key = ''.join(sorted(set(key.upper()), key=key.index)) 
        alphabet_modificado = key + ''.join([char for char in alphabet if char not in key])


        for sequence in range(1, 28):
            decrypted_text = ""
            alphabet_with_secuence = alphabet_modificado[sequence:] + alphabet_modificado[:sequence]
            for char in encrypted_text:
                if char in alphabet_with_secuence:
                    pos = alphabet_with_secuence.index(char)
                    decrypted_text += alphabet[pos]
                else:
                    decrypted_text += char

            results.append(f"Desplazamiento {sequence}: {decrypted_text}")

        self.textToEncrypt.setPlainText("\n\n".join(results))

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

        #self.decryptedText.setPlainText(alphabet_aux + "\n" +custom_alphabet + "\n" +encrypted_text)
        self.decryptedText.setPlainText(encrypted_text)

    # def generate_vigenere_cipher(self, key, text):
    #     vigenere_matrix = []
    #     alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    #     encrypted_text = ""
    #     key = key.upper()
    #     text = text.upper()

    #     for i in range(len(alphabet)):
    #         row = alphabet[i:] + alphabet[:i]
    #         vigenere_matrix.append(list(row))

    #     countText = 0
    #     countKey = 0

    #     while countText < len(text):
    #         j = 0
    #         while j < len(alphabet):
    #             if text[countText] == vigenere_matrix[0][j]:
    #                 i = 0
    #                 while i < len(alphabet):
    #                     if key[countKey] == vigenere_matrix[i][0]:
    #                         encrypted_text += vigenere_matrix[i][j]
    #                         countText += 1
    #                         countKey = (countKey + 1) % len(key)
    #                         break
    #                     i += 1
    #                 break
    #             j += 1

    #     self.decryptedText.setPlainText(encrypted_text)

    def generate_vigenere_autoclave_cipher(self, key, text):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encrypted_text = ""
        key = key.upper()
        text = text.upper()

        key_length = len(key)
        alphabet_length = len(alphabet)

        for i in range(len(text)):
            if text[i] in alphabet:
                text_pos = alphabet.index(text[i])
                if key[i % key_length] in alphabet:
                    key_pos = alphabet.index(key[i % key_length])
                else:
                    key_pos = 0 

           
                encrypted_pos = (text_pos + key_pos) % alphabet_length
                encrypted_text += alphabet[encrypted_pos]

                
                key += alphabet[encrypted_pos]
                key_length += 1
            else:
                encrypted_text += text[i]
                key += text[i]
                key_length += 1

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
    
        self.decryptedText.setPlainText(encrypted_text)
       # self.decryptedText.setPlainText(alphabet + "\n" +alphabet_with_secuence + "\n" +encrypted_text)

    def show_error_message(self,message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error", message)