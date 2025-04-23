from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {"header": "Добро пожаловать на сайт статей!", "message": "Здесь вы найдете интересные публикации, полезную информацию и актуальные новости."}
    return render(request, 'homepage.html', context=data)

def about(request):
    header = "About us"
    staff = ['John Nichols', 'John Rogers', 'Timothy Smith']
    director = {"name": "David Lee ", "img": '/director.jpg'}
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"header": header,"staff": staff,"director": director,"address": address}
    return render(request, 'about.html', data)
