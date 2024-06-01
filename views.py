from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post, Comment
from .forms import CommentForm, ThreadForm, PostForm
from django.db.models import Q



def search_for_thread(request):
    query = request.GET.get('search', '')  # Use request.GET to get the search query
    if query:
        threads = Thread.objects.filter(title__icontains=query)
        return render(request, 'searched_for.html', {'searched': query, 'threads': threads})
    else:
        return render(request, 'searched_for.html', {'searched': None, 'threads': []})
def home(request):
    threads = Thread.objects.all()
    return render(request, 'posts_list.html', {'threads': threads})

def thread_detail(request, slug):
    thread = get_object_or_404(Thread, slug=slug)
    posts = thread.posts.all()
    return render(request, 'post_page.html', {'thread': thread, 'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'post2_page.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

def new_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ThreadForm()
    return render(request, 'new_thread.html', {'form': form})

def new_post(request, thread_slug):
    thread = get_object_or_404(Thread, slug=thread_slug)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('home')  # Update the redirect URL to 'home'
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form, 'thread': thread})

def thread_list(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    if query:
        threads = Thread.objects.filter(Q(title__icontains=query))
    else:
        threads = Thread.objects.all()
    return render(request, 'thread_list.html', {'threads': threads, 'query': query})
