from django.shortcuts import render, redirect
from .models import Comment

def index(request):
    if request.method == "POST":
        Comment.objects.create(
            text=request.POST.get("comment")
        )
        return redirect("/")

    comments = Comment.objects.all()
    return render(request, "index.html", {"comments": comments})
