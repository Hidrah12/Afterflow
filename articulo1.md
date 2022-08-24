La mayoria de sitios web de hoy en día dan la posibilidad de iniciar sesión o registrarse con alguna cuenta de una red social, por ejemplo: Google Twitter, Facebook, solo por decir algunas.   
Hoy vamos a aprender a como implementar un inicio de sesión y un registro con Google y Github, en próximos artículos estaré hablando sobre como hacer lo mismo pero con Facebook y Twitter. Cabe señalar que los pasos de implementación son muy similares para cada red social.


### Paso 1
Lo primero que debemos hacer es iniciar un proyecto en django, puedes colocarle el nombre que quieras:
~~~
django-admin startproject src
~~~
### Paso 2
Instalar django-allauth, este es el paquete que nos va a permitir iniciar sesión o registrarnos con redes sociales.   
~~~
pip install django-allauth
~~~
### Paso 3
Ahora debemos dirigirnos a settings.py y agregar lo siguiente a INSTALLED_APPS:
~~~
INSTALLED_APPS = [
	...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
]
~~~
### Paso 4
Agregar las siguientes líneas de código al final del settings.py:   
~~~
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SITE_ID = 1
~~~
### Paso 5
Dirigite al archivo settings.py y agrega la siguiente linea de codigo a urlpatterns: 
~~~
from django.urls import include
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
]
~~~
### Paso 6
Realizar las migraciones (recuerda configurar la base de datos que quieras)
~~~
py manage.py makemigrations
py manage.py migrate
~~~
## 🎉 Bien ya hemos terminado con las configuraciones 🎉
Ahora falta lo más importante 😅 , debemos dirigirnos a [Google Cloud](https://console.cloud.google.com/) e iniciar sesión con nuestra cuenta de google.   
   
![Captura](/static/images/content/console-google1.png)   

Debemos crear un nuevo proyecto    

![Captura](/static/images/content/console-google2.png)     

Puedes ponerle el nombre que quieras.    

![Captura](/static/images/content/console-google3.png)    

Bien, ahora dirigete a __Pantalla de consetimiento__, selecciona la opción __Externos__ y dale al botón __Crear__.  

![Captura](/static/images/content/console-google4.png)   

Aquí hay muchas opciones que podemos cambiar 😅
, una de ellas es __Nombre de la aplicación__, aquí puedes poner el nombre de tu sitio web.   
También puedes colocar el __Correo electrónico de asistencia del usuario__ que por defecto es el correo con el que iniciaste sesión, puedes agregar el __Logotipo de tu sitio__, etc.   
El apartado que realmente nos interesa es el de __Dominio de la app__, en __Página principal de la aplicación__, debes colocar la url a la página principal de tu sitio (lo que se muestra primero al momento de acceder a tu sitio pues), como el servidor se esta ejecutando en local, colocamos 
`http://127.0.0.1:8000/`    
Tambíen nos intera la sección de __Dominios autorizados__, aquí debes colocar el dominio que tenga tu sitio, como no tenemos uno pues no lo tocamos por ahora, le damos al botón __Guardar y Continuar__.   

Ahora pulsa el botón __AGREGAR O QUITAR PERMISOS__, los permisos que nos interesan son los primeros tres, así que los seleccionas y le das al botón __ACTUALIZAR__.     

![Captura](/static/images/content/console-google6.png)

Ahora le das a el botón __GUARDAR Y CONTINUAR__, el apartado __Usuarios de prueba__, no nos interesa por ahora, le damos a __GUARDAR Y CONTINUAR__ y a __VOLVER AL PANEL__.  

Ahora nos dirigimos al apartado de __Credenciales__ y le damos a __CREATE CREDENTIALS__ y luego seleccionamos  __ID de cliente de OAuth__.   

![Captura](/static/images/content/console-google8.png)

En __Tipo de aplicación__ seleccionamos Aplicación Web.  
En la opción de __Nombre__ pon el nombre que quieras, en __URI de redireccionamiento autorizados__ debemos añadir una url un tanto peculiar:  

`http://127.0.0.1:8000/accounts/google/login/callback/` o si tenemos un dominio:   
`http://dominio.com/accounts/google/login/callback/` nosotros colocaremos estos dos: 


`http://127.0.0.1:8000/accounts/google/login/callback/`  
`http://localhost/accounts/google/login/callback/`   

![Captura](/static/images/content/console-google9.png)   

Ahora te debería aparecer un mensaje con tu __ID de cliente__ y tu __Secreto del cliente__, guardalos y no los pierdas. xd.

## Bien ya hemos terminado con Google✅, ahora falta Github🥲
Es casi el mismo proceso:   
### Paso 1
Acceder a este [enlace](https://github.com/settings/applications)   
### Paso 2
Dirigete a __Developer settings__   

![Captura](/static/images/content/github-1.png)

### Paso 3
Accede a OAuth Apps y dale a botón __Register a new application__

![Captura](/static/images/content/github-2.png)

### Paso 4
Ahora en __Application name__ coloca el nombre de tu sitio, en __Homepage URL__ coloca la url principal de tu sitio, y en __Authorization callback URL__ copia la url como está en la imagen.  

![Captura](/static/images/content/github-3.png)

Dale a el botón __Register application__, te debería de aparecer el __Client ID__ y tu __Client secrets__.   

Bien una vez llegado a este punto solo nos falta agregar algunos datos desde el administrador de django, ahora crea un nuevo super usuario.
~~~
py manage.py createsuperuser
~~~
Ejecuta el servidor
~~~
py manage.py runserver
~~~
Ahora dirigete al panel de administración de django

![Captura](/static/images/content/admin-1.png)

Entra a __Sites__ y agrega un dominio (preferentemente el dominio de tu sitio web).

![Captura](/static/images/content/admin-2.png)

Ahora debemos configurar algunas cosas para que todo funcione, primero con google, en __Client id__ colocamos el ID de cliente que se nos generó al terminar de configurar las credenciales de google lo mismo con tu Secreto de cliente de google.

![Captura](/static/images/content/admin-3.png)

Lo mismo con github:   

![Captura](/static/images/content/admin-4.png)

Solo nos queda comprobar si funciona:   
Primero accede a   
`http://127.0.0.1:8000/accounts/logout/` para cerrar la sesión, luego ve a    `http://127.0.0.1:8000/accounts/login/` 
deberias de encontrar algo como esto 

![Captura](/static/images/content/login-1.png)

bien, ya tenemos los enlaces para iniciar sesión con Google y Github, probemos a iniciar sesión con Google: 

![Captura](/static/images/content/login.png)

Funciona 🎉🎉
Probemos con Github: 

![Captura](/static/images/content/login-3.png)

También funciona!!!   🎉🎉    
Bien en este artículo hemos aprendido a hacer un inicio de sesión y un registro, pero los estilos son un poco (por no decir bastantes) feos, así que voy a estar publicando en los próximos días un articulo en el que te enseño a como personalizar el inicio de sesión y el registro para que nos quede igual o mejor al [inicio de sesión de AfterFlow](https://afterflow.herokuapp.com/accounts/login/)