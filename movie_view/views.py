import requests
from django.shortcuts import render

def home(request):
    url = 'http://127.0.0.1:8001/cartelera'
    data = {'location': 'moravia', 'cinema_id': 490}
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        peliculas = response.json()  # Asumiendo que la respuesta es un JSON con los datos esperados
    else:
        peliculas = []  # Asegura que 'peliculas' esté definido aunque la petición falle
        print("Error al obtener datos:", response.status_code, response.text)
    
    return render(request, 'home.html', {'peliculas': peliculas})
