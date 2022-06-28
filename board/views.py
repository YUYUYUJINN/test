from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from board.forms import PostForm
from board.models import Post
from django.contrib import messages


@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'GET':
        postForm = PostForm()
        context = {'postForm': postForm}
        return render(request, 'board/create.html', context)
    elif request.method == 'POST':
        postForm = PostForm(request.POST)
        context = {'postForm': postForm, 'has_error': False}
        post = Post()
        post.title = request.POST.GET('title')
        if len(post.title) < 5:
            messages.add_message(request, messages.ERROR, '제목은 5글자 이상')
            context['has_error'] = True
        post.contents = request.POST.get('contents')
        post.writer = request.user
        if context['has_error']:
            return render(request, 'board/create.html', context, status=400)
        post.save()
        return redirect('/board/read', str(post.id))


