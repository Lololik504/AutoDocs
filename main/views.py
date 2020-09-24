from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from main import services
import aiohttp

ALLOWED_EXTENSIONS = set(['.doc', '.docx'])


def home_page(request):
    return render(request, 'main/home_page.html')


@csrf_exempt
def handing_page(request):
    if request.method == 'POST':
        file = request.FILES['userfile']
        for i in ALLOWED_EXTENSIONS:
            if file.name.endswith(i):
                content = services.handling(file)
                response = HttpResponse(open(content, 'rb'), content_type='application/zip', reason="main/handing.html")
                return response
    return render(request, 'main/home_page.html')
