# Escritura en el archivo "my_notes.txt"
with open("my_notes.txt", "w") as file:
    # Escribiendo tres líneas de notas personales en el archivo
    file.write("Primera nota: Aprendiendo manejo de archivos en Python.\n")
    file.write("Segunda nota: Python es un lenguaje muy versátil.\n")
    file.write("Tercera nota: Me gusta trabajar con datos.\n")

# Lectura del archivo "my_notes.txt"
with open("my_notes.txt", "r") as file:
    # Leyendo el contenido línea por línea y mostrándolo en consola
    for line in file:
        print(line.strip())  # strip() elimina espacios en blanco innecesarios

# El archivo se cierra automáticamente al salir del bloque 'with'