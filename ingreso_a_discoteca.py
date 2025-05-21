print("¡Bienvenido/a a nuestra discoteca!")

while True:
    try:
        nombre = input("Por favor, ingrese su nombre: ")
        edad = int(input(f"{nombre}, por favor ingrese su edad: "))
        if edad >= 18:
            print("Estás permitido/a ingresar a la discoteca.")   
        else:
            print("No estás permitido ingresar a la discoteca, lo sentimos mucho.") 
    except ValueError:
        print("Por favor, ingrese un valor válido.")
        continue
    print("¿Eres un nuevo cliente? Sí/No")
    respuesta = input()
    if respuesta not in("sí", "si"):
        print("Muchas gracias por visitar nuestro espacio. ¡Diviértete!")

        
        
