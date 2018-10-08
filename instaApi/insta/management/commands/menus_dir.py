#Menus 

def menuInicio():
  print("1. Crear Cuenta")
  print("2. Listar Usuario")
  print("3. Acceder")
  print("4. Salir")
  return input("Escribir el numero de la opción: ")

def menuUsuario(user):
  print("Menu de {0}".format(user))
  print("-------------------------")
  print("3.1 Crear post")
  print("3.2 Like de post")
  print("3.3 Delete post ")
  print("3.4 Menu principal")
  return input("Escribir el numero de la opción: ")
