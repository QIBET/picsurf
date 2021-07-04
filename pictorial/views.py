from django.shortcuts import render
from pictorial.models import Image


# Create your views here.
def pictorial(request):
    all_pics = Image.get_pics()
    return render(request, 'pictorial.html',{"all_pics":all_pics})

def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_pics/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_pics/search.html',{"message":message})
