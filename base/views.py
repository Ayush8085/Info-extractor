from django.shortcuts import render, redirect

from PIL import Image

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

import pytesseract

from .models import ImageFile

# Create your views here.

@login_required
def home(request):

    if request.method == 'POST':
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

        image = request.FILES['image-file']

        text = pytesseract.image_to_string(Image.open(image))
        
        ImageFile.objects.create(
            user = request.user,
            image = image,
            image_text = text
        )

        return redirect('home')

    images = ImageFile.objects.all().order_by('-id')

    context = {'images': images}
    return render(request, 'imageprocess.html', context)

def registerUser(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required
def image(request, pk):
    image = ImageFile.objects.get(id=pk)

    context = {'image': image}
    return render(request, 'image-detail.html', context)