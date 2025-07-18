from django.urls import path
from . import views
from .views import contact

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('a-propos/', views.a_propos, name='a_propos'),
    path('ajouter/', views.ajouter_article, name='ajouter_article'),
    path('', views.liste_articles, name='accueil'),
    path('contact/', contact, name='contact'),
    path('message-envoye/', views.message_envoye, name='message_envoye'),
]