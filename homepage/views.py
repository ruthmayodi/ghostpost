from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Posts
from django.db.models import F
from .forms import InputPostForm



def index_view(request):
    data = Posts.objects.order_by('-postdate')
    return render(request, 'index.html', {'data': data})


def boast_view(request):
    data = Posts.objects.filter(boast=True).order_by('-postdate')
    return render(request, 'boast.html', {'data': data})

def roast_view(request):
    data = Posts.objects.filter(boast=False).order_by('-postdate')
    return render(request, 'roast.html', {'data': data})


def score_view(request):
    data = Posts.objects.order_by(
        -(F('upvote') - F('downvote'))
    )
    return render(request, 'score.html', {'data': data})


def upvote_view(request, post_id):
    post_value = Posts.objects.get(id=post_id)
    post_value.upvote = F('upvote') + 1
    post_value.save()
    return HttpResponseRedirect(reverse('homepage'))


def downvote_view(request, post_id):
    post_value = Posts.objects.get(id=post_id)
    post_value.downvote = F('downvote') + 1
    post_value.save()
    return HttpResponseRedirect(reverse('homepage'))

def add_post_view(request):
    if request.method == 'POST':
        form = InputPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posts.objects.create(
                text=data.get('text'), 
                boast=data.get('boast')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = InputPostForm()
    return render(request, 'addPost.html', {'form': form})

    



