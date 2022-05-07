from django.http import HttpResponse
from django.shortcuts import render



from . models import newUser
# Create your views here.
def index(request):
    print("outisede")
    if request.method == 'POST':
        print("hello")
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        profilephoto = request.POST['profilephoto']
        Bio = request.POST['Bio']
        Tag = request.POST['Tag']
        school = request.POST['school']
        schoolBoard = request.POST['school-Board']
        Graduation = request.POST['Graduation']
        GradUniversity = request.POST['GradUniversity']
        PostGraduation = request.POST['PostGraduation']
        postGradUniversity = request.POST['postGradUniversity']
        Linkedin = request.POST['Linkedin']
        Github = request.POST['Github']
        Instagram = request.POST['Instagram']
        Facebook = request.POST['Facebook']
        Position = request.POST['Position']
        Organization = request.POST['Organization']
        From = request.POST['From']
        to = request.POST['to']
        
        if newUser.objects.filter(email=email).exists():
            return HttpResponse('email already in use')
        else:
            user = newUser(firstName=firstName, lastName=lastName, email=email, profile_photo=profilephoto, shortBio=Bio,tags=Tag, schoolName=school, schoolBoard=schoolBoard, Graduation=Graduation,GraduationUniversity=GradUniversity, postUniversity=PostGraduation, postGradUniversity=postGradUniversity, Linkedin=Linkedin, facebook=Facebook, Github=Github, Instagram=Instagram, Position=Position, org=Organization, From=From, to=to
            )
            user.save()
            return HttpResponse("registered sucessfully")
    else:
        return render(request, "pages/index.html")