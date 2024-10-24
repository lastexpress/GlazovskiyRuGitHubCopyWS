from django.shortcuts import render
from django import views
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PageVisit
# Artist, Album, Customer, CartProduct, Cart,
from tg.models import tgCard, tgCategory, countVisitTg
from blog.models import Post, Comment, PostCategory, postPostCategory
from book.models import Books, CategoryBook
from clothesShop.models import Product, CategoryClothes
from account.models import Profile
from .forms import LoginForm, RegistrationForm, CommentForm
from django.utils import timezone
import random
from django.urls import reverse


def BaseView(request):
	page_visit = get_object_or_404(PageVisit)
	# Увеличение количества просмотров
	if request.user.is_authenticated:
		session_key = f'viewed_post_{page_visit.id}_user_{request.user.id}'
	else:
		session_key = f'viewed_post_{page_visit.id}_anon'

	if not request.session.get(session_key):
		page_visit.visits += 1
		page_visit.save()
		request.session[session_key] = str(timezone.now())

	page_visit.visits = 0
	page_visit.save()
		
	dic_obj = {
		'page_visit':page_visit.visits,
	}

	return render(request, "base.html", dic_obj)

#Здесь .select_related('category__category') это в посте выбрали категорию и связали с подкатегорией
def news_list(request):
	posts = Post.published_posts.all().select_related('category__category')
	posts_for_main = Post.published_posts.all()[:5]
	latest_post = Post.objects.latest('published')
	hot_post = Post.objects.filter(hot_post=True).order_by('-published')[:4]
	recent_post = Post.objects.order_by('-published').exclude(slug=latest_post.slug)[:12]
	paginator = Paginator(recent_post, 10)
	page_number = request.GET.get('page', 1)
	try:
		recent_post = paginator.page(page_number)
	except PageNotAnInteger:
		recent_post = paginator.page(1)
	except EmptyPage:
		recent_post = paginator.page(paginator.num_pages)
	popular_posts = Post.objects.order_by('-views')[:5]
	category = PostCategory.objects.all()
	category_1 = PostCategory.objects.get(pk=2)
	category_2 = PostCategory.objects.get(pk=3)
	act_category = PostCategory.objects.get(name="Актуальное")
	act_category_view = Post.objects.filter(category=act_category)
	news_category1 = Post.objects.filter(category=category_1)
	news_category2 = Post.objects.filter(category=category_2).order_by('?')
	dic_obj = {
		'posts' : posts,
		'posts_for_main' : posts_for_main,
		'latest_post' : latest_post,
		'hot_post' : hot_post,
		'recent_post' : recent_post,
		'popular_posts' : popular_posts,
		'category' : category,
		'news_category1' : news_category1,
		'news_category2' : news_category2,
		'category_1' : category_1,
		'category_2' : category_2,
		'act_category' : act_category,
		'act_category_view' : act_category_view
	}
	return render(request, 'news/news_list.html', dic_obj)

def post_detail(request, slug):
	post_detail = get_object_or_404(Post, slug=slug)
	comments_count = post_detail.comments.all().count()

	# Увеличение количества просмотров
	if request.user.is_authenticated:
		session_key = f'viewed_post_{post_detail.id}_user_{request.user.id}'
	else:
		session_key = f'viewed_post_{post_detail.id}_anon'

	if not request.session.get(session_key):
		post_detail.views += 1
		post_detail.save()
		request.session[session_key] = str(timezone.now())

	popular_posts = Post.objects.order_by('-views')[:12]
	recently_posts = Post.objects.order_by('?')[:6]

	comments = post_detail.comments.filter(active=True)

	if request.method == 'POST':
		if request.user.is_authenticated:
			form = CommentForm(request.POST)
			if form.is_valid():
				new_comment = form.save(commit=False)
				new_comment.post = post_detail
				new_comment.user = request.user
				new_comment.save()
				return redirect('post_detail', slug=post_detail.slug)
		else:
			return redirect('login')
	else:
		form = CommentForm()

	profile = Profile.objects.get(user=post_detail.author)

	related_posts_main = Post.objects.filter(category=post_detail.category).exclude(slug=slug).order_by('?')[:1]
	main_post_id = related_posts_main[0].id if related_posts_main else None
	related_posts = list(Post.objects.filter(category=post_detail.category).exclude(slug=slug))
	if main_post_id:
		related_posts = [post for post in related_posts if post.id != main_post_id]
	random_related_posts = random.sample(related_posts, min(4, len(related_posts)))
	random_recently_posts = random.sample(related_posts, min(4, len(related_posts)))

	

	dic_obj = {
		'post_detail' : post_detail,
		'comments' : comments,
		'form' : form,
		'profile' : profile,
		'random_related_posts' : random_related_posts,
		'related_posts_main' : related_posts_main,
		'popular_posts' : popular_posts,
		'random_recently_posts' : random_recently_posts,
		'comments_count' : comments_count,

	}
	return render(request, 'blog/post_detail.html', dic_obj)


def category_for_posts(request, slug):
    category = get_object_or_404(PostCategory, slug=slug)
    posts = Post.published_posts.filter(category=category)

    # Получаем список популярных постов для данной категории
    popular_post_for_category = Post.objects.filter(category=category).order_by('-views')[:2]

    # Получаем ID популярных постов
    popular_post_ids = list(popular_post_for_category.values_list('id', flat=True))

    # Получаем остальные посты для данной категории, исключая популярные посты
    other_posts = Post.objects.filter(category=category).exclude(id__in=popular_post_ids).order_by('-published')

    # Получаем все посты для данной категории
    post_for_category = Post.objects.filter(category=category).order_by('-published')

    # Получаем все категории, исключая текущую
    category_all = PostCategory.objects.exclude(slug=category.slug)

    dic_obj = {
        'category': category,
        'post_for_category': post_for_category,
        'popular_post_for_category': popular_post_for_category,
        'other_posts': other_posts,
        'category_all': category_all,
        'posts' : posts
    }

    return render(request, 'blog/category/categories.html', dic_obj)


def podCategory_for_posts(request, slug):
	podCategory = get_object_or_404(postPostCategory, slug=slug)
	posts = Post.objects.filter(category__category=podCategory)
	dic_obj = {
		'podCategory' : podCategory,
		'posts' : posts
	}
	return render(request, 'blog/category/podCategory.html', dic_obj)


def shops(request):
	all_product = Product.objects.all()
	all_category = CategoryClothes.objects.all()
	dic_obj = {
		'all_product' : all_product,
		'all_category' : all_category
	}
	return render(request, 'shop_list.html', dic_obj)

def product_detail(request, slug):
	product = get_object_or_404(Product, slug=slug)
	all_rec_category = CategoryClothes.objects.all()
	all_rec_products = Product.objects.filter(category=product.category).exclude(slug=slug)[:4]
	dic_obj = {
		'product' : product,
		'all_rec_products' : all_rec_products,
		'all_rec_category' : all_rec_category
	}
	return render(request, 'clothesShop/product_detail.html', dic_obj)

def catalogShop(request, slug):
	category = get_object_or_404(CategoryClothes, slug=slug)
	all_category = CategoryClothes.objects.all()
	product = Product.objects.filter(category=category)
	dic_obj = {
		'category' : category,
		'product' : product,
		'all_category' : all_category
	}
	return render(request, 'clothesShop/catalogShop.html', dic_obj)

def handler404(request, exception):
	return render(request, '404.html', status=404)

def tg_card_list(request):
	# Увеличение количества просмотров
	if request.user.is_authenticated:
		session_key = f'viewed_page_tg_themes_user_{request.user.id}'
	else:
		session_key = f'viewed_page_tg_themes_anon'
# Получение или создание объекта счетчика для страницы tg_themes
	page_counter, created = countVisitTg.objects.get_or_create(name='tg_themes')
	if not request.session.get(session_key):
		page_counter.views += 1
		page_counter.save()
		# Установка сессии для предотвращения повторного увеличения
		request.session[session_key] = str(timezone.now())

	cards = tgCard.objects.all()
	all_category = tgCategory.objects.all()
	paginator = Paginator(cards, 9) # Показать 9 карт на страни
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)


	dic_obj = {
		'cards':cards,
		'all_category':all_category,
		'page_obj' : page_obj,
		'page_counter' : page_counter.views

	}
	return render(request, "tg.html", dic_obj)

def tg_card_detail(request, slug):
	card = get_object_or_404(tgCard, slug=slug)
	all_cards = tgCard.objects.all()
	allCard_exclude = tgCard.objects.exclude(slug=slug)
	other_category = tgCategory.objects.all()

	# Увеличение количества просмотров
	if request.user.is_authenticated:
		session_key = f'viewed_post_tg_user_{request.user.id}'
	else:
		session_key = f'viewed_post_tg_anon'

	if not request.session.get(session_key):
		card.visits += 1
		card.save()
		request.session[session_key] = str(timezone.now())

	dic_obj = {
		'card':card,
		'all_cards':all_cards,
		'allCard_exclude':allCard_exclude,
		'other_category' : other_category
	}

	return render(request, 'tg_card_detail.html', dic_obj)

def tg_Category(request, slug):
	category_all = get_object_or_404(tgCategory, slug=slug)
	cards_in_category = tgCard.objects.filter(category_id=category_all)
	other_category = tgCategory.objects.exclude(slug=slug)
	dic_obj = {
		'category_all':category_all,
		'cards_in_category':cards_in_category,
		'other_category':other_category
	}

	return render(request, 'tg_Category.html', dic_obj)

def Books_list(request):
	all_book = Books.objects.all()
	category_1 = CategoryBook.objects.get(pk=1)
	category_2 = CategoryBook.objects.get(pk=2)
	book_category_1 = Books.objects.filter(category=category_1)
	book_category_2 = Books.objects.filter(category=category_2)
	dic_obj = {
	'all_book' : all_book,
	'category_1' : category_1,
	'category_2' : category_2,
	'book_category_1' : book_category_1,
	'book_category_2' : book_category_2
	}
	return render(request, 'books/books.html', dic_obj)

def Books_detail(request, slug):
	detail_book = get_object_or_404(Books, slug=slug)
	dic_obj = {
	'detail_book' : detail_book
	}
	return render(request, 'book/detail_book', dic_obj)