from django.contrib.auth.models import User
from insta.models import Post

# Crear un usuario nuevo
def create_user(first_name, last_name, email, username):
  try:
    mi_usuario = User(first_name = first_name, last_name = last_name, email = email, username = username)
    mi_usuario.save()
    print("Creación de usuario exitoso")
  except:
    print("Lo sentimos no se pudo crear el usuario")

#Imprime una lista de los usuarios existentes
def list_users():
  for user in User.objects.all():
    print("pk={0}:  {1} {2} - {3}".format(user.id, user.first_name, user.last_name, user.email))
      
#Verifica que exista un usuario
def acceder(username, email):
  try:
    return User.objects.get(username=username, email=email)
  except:
     print("Oops!  El usuario o el email son incorrectos")

#Permite crear un post segun un usuario
def create_post(title, content, user):
  try:
    mi_post = Post(title = title, content = content, posted_by = user)
    mi_post.save()
    print("Creación de post exitosa!")
  except:
    print("Lo sentimos no pudimos crear su post")
    
#Regresa la lista de todos los post 
def list_all_post():
  for post in Post.objects.all():
    print("pk={0}:  {1}  ({2}) \n {3}".format(post.id, post.title, post.like.all().count(), post.content))

#Guarda el like segun el usuario  
def like_post(post_id, usuario):
  try:
    like_to = Post.objects.get(id = post_id)
    like_to.like.add(usuario)
    print("Se realizo el Like")
  except:
    print("No se encontro el numero de post")
  
  
#Lista los post de un usuario especifico
def list_my_posts(user_id):
  for post in Post.objects.filter(posted_by_id = user_id):
    print("pk={0}:  {1}  ({2}) \n {3}".format(post.id, post.title, post.like.all().count(), post.content))
  
#Borra un post del usuario
def delete_post(post_id, user_id):
  find = False
  for post in Post.objects.filter(posted_by_id = user_id):
    if(post.id == post_id):
      post_deleted = Post.objects.get(id = post_id)
      post_deleted.delete()
      find = True
  if(find == True):
    print ("Eliminación exitosa!!")
  else:
    print("No se encontro el numero de post")
  
  
  
  
  