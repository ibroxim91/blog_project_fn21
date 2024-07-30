from django.shortcuts import render
from .models import Category, Post

# Create your views here.
users = [
    {'id': 1, "first_name": "Olim", "last_name": "Olimov", "age": 18},
    {'id': 2, "first_name": "Sardor", "last_name": "Olimov", "age": 18},
    {'id': 3, "first_name": "Jasur", "last_name": "Olimov", "age": 18},
]



def home(request):
    fruits = ["Olma", "Anor", "behi", "limon"]
    # category = Category.objects.create(title="Siyosat")
    # category = Category.objects.all().order_by("-id")[:10]
    # category = Category.objects.last()
    # category = Category.objects.first()
    # category = Category.objects.exclude(title="Siyosat")
    # category = Category.objects.exclude(title="Siyosat").exists()
    
    # category = Category.objects.get(title='Siyosat')

    # category = Category.objects.get(id=1)
    # category.save()
    # category.title = 'Iqtisod'
    # category.save()
    # category.delete()


    # category = Category.objects.filter(title="Siyosat")
    # category = Category.objects.count()
    # category = Category.objects.filter(title="Siyosat").count()
    # all() -> list or list
    # get() -> object or Error 
    # filter() -> list or list 
    # create() -> object or Error  
    # count() -> int  
    print()
    print(request.GET)
    print(request.POST)
    print()
    page = request.GET.get('page')
    last_post = Post.objects.last()
    posts = Post.objects.exclude(id=last_post.id)[:2]
    if page == '2':
        print()
        print("Page 2")
        print()
        posts = Post.objects.exclude(id=last_post.id)[2:]
    print()
    categories = Category.objects.all()
    return render(request,
                  'index.html',
                  context={"hi": "Assalomu alaykum",
                           "fruits": fruits,
                           "users": users,
                           "categories": categories,
                           "last_post":last_post,
                           "posts":posts,
                           "page":page
                           })


def products(request):
    return render(request, 'products.html')

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category)
    data = {'posts': posts, "category":category}
    return render(request, 'category.html', data)


