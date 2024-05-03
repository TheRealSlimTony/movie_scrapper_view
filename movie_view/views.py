import json
import requests
from django.shortcuts import render

def home(request):
    # url = 'https://cinepolisscrapper.azurewebsites.net/'
    # response = requests.get(url)
    # if response.status_code == 200:
    #     peliculas = response.json()  # Asumiendo que la respuesta es un JSON con los datos esperados
    #     return render(request, 'home_page.html')
    # else:
    #     peliculas = []  # Asegura que 'peliculas' esté definido aunque la petición falle
    #     print("Error al obtener datos:", response.status_code, response.text)
    
    return render(request, 'home_page.html')

def cartelera(request):
    if request.method == 'POST':
        reqUrl = 'https://cinepolisscrapper.azurewebsites.net/cartelera'
        response = requests.post(reqUrl, json={"cinema_id": int(request.POST['pelicula'])})
        if response.status_code == 200:
            cinema_name = {'490': 'Moravia', '251': 'Cartago', '509': 'Lindora'}
            return render(request, 'cartelera.html', {'peliculas': response.json(), 'cinema_name': cinema_name[request.POST['pelicula']]})
        else:
            return render(request, 'cartelera.html', {'error': 'Error al obtener la cartelera.'})
    else:
        url = 'https://cinepolisscrapper.azurewebsites.net/cartelera/'
        response = requests.post(url, json={'cinema_id': 490})

        if response.status_code == 200:
            return render(request, 'cartelera.html', {'peliculas': response.json(), 'cinema_name': 'Moravia'})
        else:
            return render(request, 'cartelera.html', {'error': 'Error al obtener la cartelera.'})
