from posts.forms import PostForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.forms.utils import to_current_timezone
from posts.models import Post
from django.core.paginator import Paginator


def posts(request):
    title = 'Блог'
    template = 'posts.html'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'title': title,
    }
    return render(request, template, context)


@csrf_exempt
@login_required
def new_post(request):
    title = 'Новый пост'
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if not form.is_valid():
        return render(request, 'new_post.html', {
            'form': form, 'title': title}
        )
    post = form.save(commit=False)
    post.author = request.user
    post.pub_date = to_current_timezone
    post.save()
    return redirect('posts')
