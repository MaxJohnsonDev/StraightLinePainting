from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

# Create your views here.
def post_detail(request, slug):
    template_name = 'post-detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        commetn_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                            'comments': comments,
                                            'new_comment': new_comment,
                                            'comment_form': comment_form})
