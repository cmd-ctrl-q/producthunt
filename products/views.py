from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def home(request):
    products = Product.objects # gets all projects out database
    return render(request, 'products/home.html', {'products': products})

@login_required
def create(request):
    # check if post request 
    if request.method == 'POST':
        # check all required fileds
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            # make new product object and store users fields into product
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                # preappend http
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user

            # save product. (inserts into database)
            product.save()
            # send them to the home page to view their product/post
            return redirect('/products/' + str(product.id))

        else: 
            return render(request, 'products/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

@login_required
def upvote(request, product_id):
    # increase vote count
    if request.method == 'POST':
        # get product
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))

