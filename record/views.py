from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Record, Review
from .forms import ReviewForm

# Create your views here.
class RecordList(generic.ListView):
    queryset = Record.objects.filter(status=1)
    template_name = "record/index.html"
    paginate_by = 6

 #   def post_detail(request, slug):
  #  """
   # Display an individual :model:`blog.Post`.

    #**Context**

    #``post``
    #    An instance of :model:`blog.Post`.

    #**Template:**

    #:template:`blog/post_detail.html`
    #"""

    #queryset = Post.objects.filter(status=1)
    #post = get_object_or_404(queryset, slug=slug)

    #return render(
    #    request,
    #    "blog/post_detail.html",
    #    {"post": post},
    #)


def record_detail(request, id):
    """
    Display an individual :model:`record.Record`.

    **Context**

    ``record``
        An instance of :model:`record.Record`.

    **Template:**

    :template:`record/record_detail.html`
    """
    
    queryset = Record.objects.filter(status=1)
   
    record = get_object_or_404(queryset, id=id)
    reviews = record.reviews.all().order_by("created_on")
    review_count = record.reviews.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.record = record
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
    )

    review_form = ReviewForm() 
    
    return render(
        request,
        "record/record_detail.html",
        {"record": record,
         "reviews": reviews,
         "review_count": review_count,
         "review_form": review_form,
         },
    )

def review_edit(request, id, review_id):
    """
    view to edit reviews
    """   
    
    if request.method == "POST":
            
            queryset = Record.objects.filter(status=1)
            record = get_object_or_404(queryset, id=id)
            review = get_object_or_404(Review, pk=review_id)
            review_form = ReviewForm(data=request.POST, instance=review)

            if review_form.is_valid() and review.author == request.user:
                review = review_form.save(commit=False)
                review.record = record
                review.approved = False
                review.save()
                messages.add_message(request, messages.SUCCESS, 'Review Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('record_detail', args=[id]))



