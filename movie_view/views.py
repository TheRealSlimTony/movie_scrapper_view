import requests
from django.shortcuts import render

def home(request):
    url = 'http://127.0.0.1:8001/cartelera'
    data = {'cinema_id': request.POST['pelicula']}
    response = requests.post(url, json=data)
    cinema_name = {'490':'Moravia',
                 '251':'Cartago',
                 '509':'Lindora'}
    
    if response.status_code == 200:
        peliculas = response.json()  # Asumiendo que la respuesta es un JSON con los datos esperados
    else:
        peliculas = []  # Asegura que 'peliculas' esté definido aunque la petición falle
        print("Error al obtener datos:", response.status_code, response.text)
    
    return render(request, 'home.html', {'peliculas': peliculas, 'cinema_name': cinema_name[request.POST['pelicula']]})
