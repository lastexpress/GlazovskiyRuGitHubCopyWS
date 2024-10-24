from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from musicshop import views
from .views import BaseView, tg_card_list, tg_Category, shops, news_list, post_detail, category_for_posts, Books_list, Books_detail, product_detail, catalogShop, podCategory_for_posts


urlpatterns = [
    path('', views.BaseView, name='base'),
    path('telegramThemes/', views.tg_card_list, name='tg'),
    path('telegramThemes/<slug:slug>', views.tg_card_detail, name='tg_card_detail'),
    path('telegramThemes/Category/<slug:slug>', views.tg_Category, name='tg_category'),
    path('shop/', views.shops, name='shop'),
    path('shop/<slug:slug>/', views.product_detail, name="product_detail"),
    path('shop/catalog/<slug:slug>/', views.catalogShop, name="catalogShop"),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.post_detail, name='post_detail'),
    path('news/category/<slug:slug>/', views.category_for_posts, name='category_for_posts'),
    path('news/pc/<slug:slug>/', views.podCategory_for_posts, name='podCategory_for_posts'),
    path('books/', views.Books_list, name="Books_list"),
    path('books/<slug:slug>/', views.Books_detail, name="Books_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'musicshop.views.handler404'