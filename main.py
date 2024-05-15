# resultado = input('Dame tu nombre:')
# print('Hola',resultado)
text ='Hello World'

print(text[-1])

# esta funcion lo que hace es que imprime el ultimo caracter de la cadena de texto
# en este caso la cadena de texto es 'Hello World' y el ultimo caracter es 'd' por lo que imprime 'd' en la consola
# la funcion de esta linea de codigo es imprimir el ultimo caracter de una cadena de texto
# si pongo 6 en vez de -1 me imprime el caracter en la posicion 6 de la cadena de texto

# text = 'Hello World'
# print(len(text))
# # esta funcion lo que hace es que imprime la longitud de la cadena de texto

# text = 'Hello World'
# print(type(text))
# # esta funcion lo que hace es que imprime el tipo de dato de la cadena de texto

# text = 'Hello World'
# print(type(text))dsadsadsadasdasdadasda
# shift = 3
# print(shift)
# #  


# numero1 = input('Dame un numero:')
# numero2 = input('Dame otro numero:')
# resultado = int(numero1) + int(numero2)
# print('El resultado es:',resultado)


# dia = int(input('Como estuvo tu dia?: '))
# print('tu dia estuvo de: ', dia)

# titulo = input('Me puedes dar tu libro favorito?: ')
# autor = input('Me puedes dar tu autor favorito?: ')
# print(titulo, 'fue escrito por', autor)


# ancho = int(input('Dame el ancho: '))
# largo = int(input('Dame el largo: '))

# resultadoArea = largo*ancho
# resultadoPerimetro= 2*(largo + ancho)
# print(f'El area es: {resultadoArea}' )
# print('area: ', ancho) 
# print(f'El perimetro es: {resultadoPerimetro}')


# # Inicializar una variable
# x = 10
# print("Valor inicial de x:", x)

# # Asignación con suma
# x += 5
# print("Después de sumar 5:", x)

# # Asignación con resta
# x -= 3
# print("Después de restar 3:", x)

# # Asignación con multiplicación
# x *= 2
# print("Después de multiplicar por 2:", x)

# # Asignación con división
# x /= 4
# print("Después de dividir por 4:", x)

# # Asignación con módulo
# x %= 3
# print("Después de tomar el módulo 3:", x)

# # Asignación con división entera
# x //= 2
# print("Después de la división entera por 2:", x)

# # Asignación con potencia
# x **= 3
# print("Después de elevar a la potencia 3:", x)


# miVariable = 10

# miVariable += 10
# miVariable -= 15
# print(miVariable)

# miVariable += 15
# print(miVariable)


# miVariable /= 2
# print(miVariable)

# miVariable *= 3
# print(miVariable)



# # Definir dos números
# x = 5
# y = 10

# # Operador de igualdad (==)
# print("¿Es 5 igual a 10?", x == y)  # Resultado: False

# # Operador de desigualdad (!=)
# print("¿Es 5 diferente de 10?", x != y)  # Resultado: True

# # Operador de mayor que (>)
# print("¿Es 5 mayor que 10?", x > y)    # Resultado: False

# # Operador de menor que (<)
# print("¿Es 5 menor que 10?", x < y)    # Resultado: True

# # Operador de mayor o igual que (>=)
# print("¿Es 5 mayor o igual que 10?", x >= y)  # Resultado: False

# # Operador de menor o igual que (<=)
# print("¿Es 5 menor o igual que 10?", x <= y)  # Resultado: True


# a = int(input('Escribe un valor numerico: '))

# if a % 2 == 0:
#     print(f'Si es numero par {a}')

# else:
#     print(f'NO es numero par {a}')


# edad = int(input('Eres mayor de edad...dime tu edad?: '))

# if edad >= 18:
#     print('Eres mayor de edad.. pasale')
# else:
#     print('No eres mayor de edad')


# OR

# vacaciones = False
# diaDescanso = False

# if vacaciones or diaDescanso:
#     print('Puede asistir al juego')
# else:
#     print('Tiene deberes por hacer')

# si los 2 valores son falsos, entonces regresa falso


# AND hace que los 2 valores sean verdaderos para que regrese verdadero

# vacaciones = True
# diaDescanso = True

# if vacaciones and diaDescanso:
#     print('Puede asistir al juego')
# else:
#     print('Tiene deberes por hacer')


# NOT hace que el valor sea falso si es verdadero y viceversa

# vacaciones = True
# diaDescanso = True

# if not vacaciones:
#     print('Tiene deberes por hacer')
# else:
#     print('Puede asistir al juego')


# ejecicio con and
# edad = int(input('Dime tu edad: '))

# resultado = edad >= 18 and edad <= 30
# resultado2 = edad >= 30 and edad <= 40

# print(resultado)
# print(resultado2)

# if resultado or resultado2:
#     if resultado:
#         print(f'Tienes {edad} años, puedes entrar al antro')
#     elif resultado2:
#         print(f'Tienes {edad} años, puedes entrar al antro')
# else:
#     print('No puedes entrar al antro')



# numero1 = int(input('Dame un numero: '))
# numero2 = int(input('Dame otro numero: '))

# if numero1 > numero2:
#     print('El numero 1 es mayor que el numero 2')
# else:
#     print('El numero 2 es mayor que el numero 1')

# EJERCICIO DE TIENDA DE LIBROS


print('Proporcione los siguientes datos del libro:')
nombreLibro = input('Proporciona el nombre del libro: ')
id = int(input('Proporciona el ID del libro: '))
precio = int(input('Proporcione el precio del libro: '))
envio = input('El envio es gratis?: ')

if envio == 'si':
    envio = True
elif envio == 'no':
    envio = False


# print(f'Nombre del libro es: {nombreLibro}')
# print(f'El ID del libro es: {id}')
# print(f'El precio del libro es: {precio} ')


print(f''' 
    Nombre: {nombreLibro}
    id: {id}
    precio: {precio}
    Envio gratuito: {envio}
'''
)