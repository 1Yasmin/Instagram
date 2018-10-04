from django.contrib.auth.models import User

def create_user(username, password, email):
        mi_usuario = User(username=username, password=password, email = email)
        mi_usuario.save()

def list_users():
  for user in User.objects.all():
    print("pk={0}:  {1} - {2}".format(user.id, user.username, user.email))
      
  
def acceder(username, email):
  try:
    User.objects.get(username=username, email=email)
    print("Inicio de sesion exitoso")
  except:
     print("Oops!  El usuario o el email son incorrectos")
        