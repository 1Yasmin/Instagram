from insta.models import Users

def create_user(username, password, email):
        mi_usuario = Users(username=username, password=password, email = email)
        mi_usuario.save()

def list_users():
  for user in Users.objects.all():
    print("pk={0}:  {1} - {2}".format(user.id, user.username, user.email))
      
  
def acceder(username, email):
  try:
    Users.objects.get(username=username, email=email)
    print("Inicio de sesion exitoso")
  except:
     print("Oops!  El usuario o el email son incorrectos")
        