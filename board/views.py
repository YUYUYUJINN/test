from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from board.models import Post


@login_required(login_url='/accounts/login')
def create(request):
    if request.method == 'GET':
        return render(request, 'board/create.html')
    elif request.method == 'POST':
        post = Post()
        post.title = request.POST.get('title')
        post.contents = request.POST.get('contents')
        post.writer = request.user
        post.save()
        return redirect('/board/read' + str(post.id))
