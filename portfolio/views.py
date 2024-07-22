from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PortfolioForm
from .models import Portfolio

# Create your views here.


@login_required
def index(request):
    pp_list = Portfolio.objects.all()
    return render(
        request,
        "portfolio/index.html",
        {
            "pp_list": pp_list,
        },
    )


@login_required
def new_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/")
    else:
        form = PortfolioForm()

    return render(request, "portfolio/post_form.html", {"form": form})
