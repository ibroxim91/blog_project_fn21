from django.shortcuts import render, redirect
from .models import Category, Post, Comment

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

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        comment = request.POST.get('comment')
        comment = Comment.objects.create(post=post,  content=comment)
        if request.user.is_authenticated:
            comment.author = request.user
        else:
            comment.first_name = first_name    
            comment.last_name = last_name    
        comment.save()
   
    post.views += 1
    post.save()
    categories = Category.objects.all()
    # post.comments.all()
    # comments = Comment.objects.filter(post=post)
    data = {'last_post': post, "categories":categories, }
    return render(request, 'post.html', data)


def post_reactions(request, post_id):
    reactions = request.GET.get('reactions')
    post = Post.objects.get(id=post_id)
    print()
    print(reactions)
    print(post)
    print()
    if reactions == 'likes':
        post.likes += 1
    elif reactions == 'dislikes':
        post.dislikes += 1
    post.save()
    return redirect(f'/post/{post_id}')

