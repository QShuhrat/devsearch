from django.shortcuts import render
from .models import *
# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profile.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact='')
    otherskills = profile.skill_set.filter(description='')
    context = {'profile': profile, 'topskills':topskills, 'otherskills':otherskills}
    return render(request, 'users/user-profile.html', context)
