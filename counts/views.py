from django.shortcuts import render, redirect
from .models import Transaction
from .form import TransactionForm

# from django.http import HttpResponse
import datetime


def home(request):
    data = {}
    data["now"] = datetime.datetime.now()
    data["transactions"] = ["t1", "t2", "t3"]
    # html = "<html><body>It is now %s</body></html>" % now

    return render(request, "counts/home.html", data)


def listing(request):
    data = {}
    data["transactions"] = Transaction.objects.all()
    # manager ^^^^^^^
    return render(request, "counts/listing.html", data)


def create_transaction(request):
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("url_listing")

    return render(request, "counts/form.html", {"form": form})


def update(request, pk):
    data = {}
    transaction = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect("url_listing")

    data["form"] = form
    data["transaction"] = transaction
    return render(request, "counts/form.html", data)


def delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect("url_listing")
