from django.shortcuts import redirect, render
from .models import pactice, testimonie,feedback,Post,Gallery,Content
from .forms import testimonialForm,feedbackForm,pacticeForm


def index(request):
    testimony = testimonie()
    if request.method == 'POST':
        testimonyform = testimonialForm(request.POST,instance=testimony)
        if testimonyform.is_valid():
            testimonyform.save()
        return redirect('index')
    else:
        testimonyform = testimonialForm()

    visitor_feedback = feedbackForm()
    if request.method == 'POST':
        if visitor_feedback.is_valid():
            visitor_feedback.save()
        return redirect('index')
    else:
        visitor_feedback = feedbackForm()

    testimonies = testimonie.objects.all()
    blog_feed = Post.objects.all()
    gallery_stock = Gallery.objects.all().order_by('-date_uploaded')
    contents_feed = Content.objects.all()
    context = {
        'testimonyform':testimonyform,
        'visitor_feedback':visitor_feedback,
        "testimonies":testimonies,
        "blog_feed":blog_feed,
        "gallery_stock":gallery_stock,
        "contents_feed":contents_feed,
    }
    return render(request, 'unifiedLangCenter_website/index.html',context)

def practice(request):
    if request.method == 'POST':
        form = pacticeForm()
        if form.is_valid():
            pract = form.cleaned_data('body')
        return redirect('practice')
    else:
        form = pacticeForm()

    contents_feed = Content.objects.all()
    context={
        "form":form,
        'contents_feed':contents_feed,
    }
    return render(request, 'unifiedLangCenter_website/practice.html',context)