from django.shortcuts import render
from .forms import StyleImageForm
from .models import StyleImage
# Require login LIB
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

# Create your views here.
def images(request):
    # Link for images
    template = 'galleries/images.html'
    form = StyleImageForm
    
    #get all item in database
    all_image = StyleImage.objects.all()

    # check request method
    if request.method == 'POST':
        image_form = StyleImageForm(request.POST or None, request.FILES or None)

        # check valid
        if image_form.is_valid():
            new_image_form = image_form.save(commit=False)
            new_image_form.save()

    return render(request, template, locals())

# Create function delete image
@login_required
def delete(request, id):
    # get an image by ID
    image = StyleImage.objects.get(id=id)

    # check method
    if request.method == 'POST':
        # use method delete to remove an image
        image.delete()

        # go to galleries
        return HttpResponseRedirect('/gallery/images/')
