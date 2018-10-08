from django.core.management.base import BaseCommand
from .menus_dir import *
from .utilities import *

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    print("Bienvenido al Instagram Command Line")
    select = menuInicio()
    global usuario
    
    while True:    
      #Crear cuenta
      if select == "1":
        first_name = input("Ingrese su primer nombre: ")
        lastname = input("Ingrese su apellido: ")
        email = input("Ingrese su email: ")
        username = input("Ingrese su nombre de usuario: ")
        create_user(first_name, lastname, email, username)
        select = menuInicio()
        
      #Ver usuarios registrados
      elif select == "2":
        print("La lista de usuarios actuales es: ")
        list_users()
        select = menuInicio()
        
      #Acceder a la cuenta
      elif select == "3":
        username = input("Ingrese el nombre de usuario: ")
        email = input("Ingrese su email: ")
        usuario = acceder(username, email)
        if(usuario != None):
          print("Bienvenido {0}".format(usuario.first_name))
          selectmu = menuUsuario(usuario.first_name)
          while True:
            #Crear un post
            if selectmu == "3.1":
              title = input("Ingrese Titulo: ")
              content = input("Ingrese el contenido: ")
              create_post(title, content, usuario)
              selectmu = menuUsuario(usuario.first_name)
            #Dar like a un post
            elif selectmu == "3.2":
              list_all_post()
              like = input("A que post quiere darle like: ")
              like_post(int(like), usuario)
              selectmu = menuUsuario(usuario.first_name)
            #borrar un post
            elif selectmu == "3.3":
              list_my_posts(usuario.id)
              post = input("Que post desea borrar: ")
              delete_post(int(post), usuario.id)
              selectmu = menuUsuario(usuario.first_name)
            #Salir de la cuenta  
            elif selectmu == "3.4":
              usuario = None
              select = menuInicio()
              break
            else:
              print("La opción seleccionada no se encuentra en la lista")
              selectmu = menuUsuario(usuario.first_name)    
        else:
          select = menuInicio()        
      #Salir del programa
      elif select == "4":
        print("Adios!")
        break
        
      else:
        print("La opción seleccionada no se encuentra en la lista")
        select = menuInicio()
        
      
  
  