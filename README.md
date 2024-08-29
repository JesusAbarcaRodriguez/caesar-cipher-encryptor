# Caesar Cipher Encryptor

Este proyecto implementa cifrados basados en el algoritmo de Cifrado César y Vigenère, con una interfaz gráfica creada en PyQt5.

## Descripción

El proyecto permite a los usuarios encriptar y desencriptar textos utilizando diferentes tipos de cifrados. Se utiliza el slicing de Python para manejar las rotaciones de letras, facilitando la implementación de los cifrados.

### Rotaciones de letras con slicing

Para manejar las rotaciones en el Cifrado César, se emplea el slicing de Python. A continuación, se explica cómo funciona:

- `alphabet[sequence:]`: Toma una "rebanada" del alfabeto desde el índice especificado por `sequence` hasta el final. Por ejemplo, si `sequence` es 3 y `alphabet` es `"ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"`, entonces `alphabet[3:]` devolverá `"DEFGHIJKLMNÑOPQRSTUVWXYZ"`.
  
- `alphabet[:sequence]`: Toma una rebanada desde el inicio del alfabeto hasta el índice `sequence`. En el mismo ejemplo, `alphabet[:3]` devolverá `"ABC"`.
  
- `alphabet[sequence:] + alphabet[:sequence]`: Combina las dos rebanadas anteriores, resultando en una rotación del alfabeto. Si `sequence` es 3, el resultado será `"DEFGHIJKLMNÑOPQRSTUVWXYZABC"`.

Este enfoque permite rotar cualquier alfabeto de acuerdo con una secuencia dada, facilitando la implementación de cifrados basados en rotaciones.

## Características

- **Cifrado César**: Permite especificar una clave que rota el alfabeto para cifrar el texto.
- **Cifrado César con secuencia**: Similar al Cifrado César, pero permite seleccionar el número de rotaciones directamente.
- **Cifrado Vigenère**: Utiliza una palabra clave para cifrar el texto, creando una encriptación más compleja.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el desarrollo de la lógica del cifrado.
- **PyQt5**: Librería utilizada para la creación de la interfaz gráfica de usuario.
- **Slicing de Python**: Método utilizado para rotar las letras del alfabeto en los cifrados.

## Enlaces útiles

- [StackOverflow: Explicación sobre slicing en Python](https://es.stackoverflow.com/questions/341559/qu%C3%A9-significa-1#:~:text=1%20respuesta&text=Es%20lo%20que%20se%20conoce,tuple)
