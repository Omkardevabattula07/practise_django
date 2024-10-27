import requests
from django.shortcuts import render

def book_search(request):
    results = []
    title = request.GET.get('title')  # Get title from query parameters
    if title:
        # Call Google Books API
        response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={title}')
        if response.status_code == 200:
            results = response.json().get('items', [])
    return render(request, 'book_search.html', {'results': results})
