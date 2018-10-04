from django.core.management.base import BaseCommand
from .menus_dir import *
from .utilities import *

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    print("Bienvenido al Instagram Command Line")
    select = menuInicio()
    
    while True:    
      
      if select == "1":
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contrasena: ")
        email = input("Ingrese su email: ")
        create_user(username, password, email)
        print("Creación de usuario exitoso")
      
      elif select == "2":
        print("La lista de usuarios actuales es: ")
        list_users()
        select = menuInicio()
      
      elif select == "3":
        username = input("Ingrese el nombre de usuario: ")
        email = input("Ingrese su email: ")
        acceder(username, email)
      
      elif select == "4":
        print("Adios!")
        break
      
  
  