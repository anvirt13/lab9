from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def movies(request):
    movies = Movie.objects.all()
    
    context = {
        "page_title": "Movies",
        "movies": movies
    }

    return render(request, "homepage.html", context)


def movie(request, pk):
    movie = Movie.objects.get(id=pk)


    context = {
        "page_title": "Movie",
        "movie": movie
    }

    print(context)
    return render(request, "movie.html", context)

@login_required(login_url="login")
def addMovie(request):
    form = MovieForm()

    if (request.method == 'POST'):
        Movie.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            year = request.POST.get('year'),
            rating = request.POST.get('rating'),
            posted_by = request.user,
        
        )

        return redirect("/")

    context = {
        "page_title": "Add Movie",
        "form": form
    }

    return render(request, "movie_form.html", context)

@login_required(login_url="login")
def updateMovie(request,pk):
    movie = Movie.objects.get(id=pk)
    form = MovieForm(instance=movie)

    if (movie.posted_by != request.user):
        return render(request, "not_authorized.html")

    if (request.method == 'POST'):
        movie.name = request.POST.get('name')
        movie.description = request.POST.get('description')
        movie.year = request.POST.get('year')
        movie.rating = request.POST.get('rating')
        
        
        movie.save()
        return redirect("/")

    context = {
        "page_title": "Review Movie",
        "form": form
    }

    return render(request, "movie_form.html", context)

@login_required(login_url="login")
def deleteMovie(request,pk):
    movie = Movie.objects.get(id=pk)

    if (movie.posted_by != request.user):
        return render(request, "not_authorized.html")
        
    if (request.method == 'POST'):
        movie.delete()
        
        return redirect("/")
    
    context = {
        "movie": movie
    }


    return render(request, "delete.html", context)


def reviewMovie(request, pk):
    movie = Movie.objects.get(id=pk)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        review = Review.objects.create(movie=movie, rating=rating, comment=comment)
        review.save()
        return redirect('movie', pk=pk)

    context = {
        'movie': movie,
        'page_title': 'Review Movie',
    }

    return render(request, 'review_form.html', context)

@login_required(login_url="login")
def deleteReview(request, pk):
    review = Review.objects.get(id=pk)
    
    movie = review.movie

    if request.method == 'POST':
        review.delete()
        return redirect('movie', pk=movie.pk)  # Redirect to the movie detail page after deleting review

    context = {
        'review': review,
        'movie': movie,
    }
    return render(request, 'delete_review.html', context)

@login_required(login_url="login")
def editReview(request, pk):
    review = Review.objects.get(id=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movie', pk=review.movie.pk)  
    else:
        form = ReviewForm(instance=review)  

    context = {
        'form': form,
        'review': review,
        'edit_review_window': True,  
    }
    return render(request, 'review_form.html', context)


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            print("USer does not exist")
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Username or password is invalid")

    context = {
        "page": page
    }
    
    return render(request, "login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("/")

def registerUser(request):
    form = UserCreationForm()

    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect("/")
        else:
            print("Error in registration")

    context = {
        "form": form
    }

    return render(request, "login_register.html", context)
