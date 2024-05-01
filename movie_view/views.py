import requests
from django.shortcuts import render

def home(request):
    url = 'https://cinepolisscrapper.azurewebsites.net/'
    response = requests.get(url)
    if response.status_code == 200:
        peliculas = response.json()  # Asumiendo que la respuesta es un JSON con los datos esperados
        return render(request, 'home_page.html')
    else:
        peliculas = []  # Asegura que 'peliculas' esté definido aunque la petición falle
        print("Error al obtener datos:", response.status_code, response.text)
    
    return render(request, 'home_page.html')


def cartelera(request):
    if request.method == 'POST':
        cinema_id = request.POST.get('cinema_id')
        url = 'https://cinepolisscrapper.azurewebsites.net/cartelera/'
        data = {'cinema_id': request.POST['pelicula']}
        response = requests.post(url, json=data)
        cinema_name = {'490':'Moravia',
                    '251':'Cartago',
                    '509':'Lindora'}
        return render(request, 'home.html', {'peliculas': response.json(), 'cinema_name': cinema_name[cinema_id]})
    else:
        url = 'https://cinepolisscrapper.azurewebsites.net/cartelera/'
        response = requests.get(url)
        cinema_name = {'490':'Moravia',
                    '251':'Cartago',
                    '509':'Lindora'}
        return render(request, 'home.html', {'peliculas': response.json(), 'cinema_name': cinema_name['490']})
        