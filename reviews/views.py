from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def submitReview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reviews:success)
    else:
        form = ReviewForm()
    return render(request, 'reviews/postReview.html', {'form': form})

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
                            'number_of_reviews': number_of_reviews})
    context = {
            'review_list': review_list
    }
    return render(request, 'reviews/review_list.html', context)

def success(request):
    return render(request, 'reviews:success')
