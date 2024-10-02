# Este programa cuenta las palabras en una frase

# Pedimos al usuario que escriba una frase
frase = input("Escribe una frase: ")

# Contamos cuántas palabras hay en la frase
palabras = frase.split()

# Mostramos el número de palabras
print(f"Tu frase tiene {len(palabras)} palabras.")
