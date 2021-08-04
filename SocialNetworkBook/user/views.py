from django.http import HttpResponse
from django.shortcuts import render
from .models import Profile, Relationship
from .forms import ProfileForm
from django.shortcuts import render, get_object_or_404


# Create your views here.

def profile_view(request):
    data = get_object_or_404(Profile, username=request.user)
    context = {
        'username': data.username,
        'fullname': data.full_name,
    }
    return render(request, 'profile.html', context)


def profile_view_by_id(request, usr_id):
    data = get_object_or_404(Profile, id=usr_id)
    context = {
        'username': data.username,
        'fullname': data.full_name,
    }
    return render(request, 'profile_id.html', context)
    # return HttpResponse(context['username']+context['fullname'])


def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('successful')
        else:
            context = {
                'errors': form.errors
            }
            return render(request, 'profile_edit.html', context)
    else:
        form = ProfileForm()
        return render(request, 'profile_edit.html', {'form': form})
