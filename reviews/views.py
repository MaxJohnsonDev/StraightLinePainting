# from django.shortcuts import render, get_object_or_404
# from .models import Post
# from .forms import CommentForm
#
# # Create your views here.
# def post_detail(request, slug):
#     template_name = 'post-detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#
#     if request.method == 'POST':
#         commetn_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, template_name, {'post': post,
#                                             'comments': comments,
#                                             'new_comment': new_comment,
#                                             'comment_form': comment_form})


from django.shortcuts import render
from .models import Review
from .utils import average_rating

def review_list(request):
    reviews = Review.objects.all()
    review_list = []
    for review in reviews:
        reviews = review.review_set.all()
        if reviews:
            job_rating = average_rating([review.rating for \
                                            review in reviews])
            number_of_reviews = len(reviews)
        else:
            job_rating = None
            number_of_reviews = 0
        review_list.append({'review': review,\
                            'job_rating': job_rating,\
                            'number_of_reviews',: number_of_reviews})
    context = {
            'review_list': review_list
    }
    return render(request, 'reviews/review_list.html', context)
