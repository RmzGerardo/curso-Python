# # # ejericio 1

# print('Hola mundo')

# # # ejercicio 2

# texto = 'Hola mundo'
# print(texto)

# # # ejercicio 3

# entarda = input('Cual es tu nombre: ')
# print(f'Hola {entarda}')

# # ejercicio 4

# operacion = ( ( (3+2)/(2*5))**2)
# print(operacion)


# # #  ejercicio 5

# horasT = int(input('Dame las horfsfsdfssfpor hora: '))

# sueldo = horasT * costoH
# print(f'Tu sueldo es: {sueldo}')


# #  ejercicio 6

# n = int(input('Introduceun numero entero: '))
# suma = n * (n + 1) / 2
# print(f'La suma de los primeros numeros enteros desde 1 hasta {n} es {suma}')


# # ejercicio 7

# peso = float(input('Dame tu peso: '))
# altura = float(input('Dame tu altura: '))

# imc = peso / altura**2
# print(f'Tu indice de masa corporal es: {imc}')



# # ejercicio 8

# cantidad = int(input('Cual es la cantidad que vas a invertir?: '))
# interes = float(input('Cual es el interes anual?: '))
# años = int(input('A que numero de años vas a invertirlo: ' ))

# coi = (cantidad*(1 + interes)**años)

# print(coi)


# # ejercicio 9

# nPayasos = int(input('Cuantos payasos se vendieron?: '))
# muñecas = int(input('Cuantas muñecas se vendieron?: '))

# pesoPayaso = float(112)
# pesoMuñeca = float(75)

# resultadoMuñecos = (nPayasos * pesoPayaso) + (muñecas * pesoMuñeca)

# print(f'el peso del paquete es {resultadoMuñecos}g')


# # ejercicio 10

# inversion = float(input("Introduce la inversión inicial: "))
# interes = 0.04
# balance1 = inversion * (1 + interes)
# print("Balance tras el primer año:" + str(round(balance1, 2)))
# balance2 = balance1 * (1 + interes)
# print("Balance tras el segundo año:" + str(round(balance2, 2)))
# balance3 = balance2 * (1 + interes)
# print("Balance tras el tercer año:" + str(round(balance3, 2)))




# print('Estudiando Python')
# print('Python es muy versatil para programar :)')



# Ejercicios condicionales



# edad = int(input('Dime tu edad y te digo si eres mayor de edad: '))

# if edad >=18:
#     print('Eres mayor de edad')
# else:
#     print('No eres mayor de edad')


# text = int(input('Dime tu contraseña numerica: '))

# contrasea = text

# validacion = input(f'La contraseña es correcta?: {contrasea} ')

# if validacion == 'si':
#     validacion = True   
# else:
#     validacion = False
#     print("Contraseña incorrecta.")

# print(f'''
#     La contraseña se validó y es correcta: {contrasea}
# ''')


# contraseña = 'Hola2132'

# contraseña_ingresada = input('Ingresa la contraseña: ')

# if contraseña_ingresada.lower() == contraseña.lower():
#     print('Contraseña correcta') 
# else:
#     print('Contraseña incorrecta')

# input("Presiona Enter para salir...")




# dividendo = float(input('Introduce el dividendo: '))
# divisor = float(input('Introduce el dividendo: '))

# if divisor == 0:
#     print('Error, no se puede dividir por 0.')
# else:
#     print(dividendo/divisor)




print('Dame 2 numeros para que te diga cual es mayor')
num1 = int(input('Dame un numero: '))
num2 = int(input('Dame otro numero: '))

if num1 > num2:
    print(f'Numero 1: {num1} es mayor que Numero 2: {num2}')
elif num2 > num1:
   print(f'Numero 2: {num2} es mayor que Numero 1: {num1}')
else:
    print('No es mayor')
           


