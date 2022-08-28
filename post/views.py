from django.contrib import messages
from django.shortcuts import render, redirect
from post.forms import PostForm, RegisterForm
# Create your views here.
from post.models import Post,UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import decorators
from django.contrib.admin.views.decorators import staff_member_required


def logoutView(request):
    logout(request)
    return redirect("index")


def RegisterView(request):
    form = RegisterForm()

    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("index")

    return render(request, 'auth/Register.html', context={
        'form': form
    })


def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =  authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

    return render(request, 'auth/Login.html')

@decorators.login_required
def ProfileView(request):
    return render(request, 'auth/profile.html')



def IndexView(request):

    return render(request, 'Index.html', context={
        'post': Post.objects.all()
    })

#pagina de detalle
def DetailsView(request, pk):
    return render(request, 'Details.html', context={
        'details': Post.objects.get(pk=pk)
    })


def AboutView(request):
    return render(request, 'About.html')


#crear Post
@decorators.login_required
def CreatePostView(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("index")
    return render(request, 'CreatePost.html', context={
        'form': form
    })
