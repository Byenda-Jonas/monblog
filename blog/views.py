from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .models import Article, MessageContact
from .forms import ArticleForm, ContactForm

def liste_articles(request):
    articles = Article.objects.order_by('-date_creation')
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail_article.html', {'article': article})

def a_propos(request):
    return render(request, 'blog/a_propos.html')

def ajouter_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'blog/ajouter_article.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            captcha = form.cleaned_data.get('captcha')
            if captcha != '4':
                form.add_error('captcha', "Réponse incorrecte à la question anti-spam.")
            else:
                MessageContact.objects.create(
                    nom=form.cleaned_data['nom'],
                    postenom=form.cleaned_data['postenom'],
                    prénom=form.cleaned_data['prénom'],
                    téléphone=form.cleaned_data['téléphone'],
                    email=form.cleaned_data['email'],
                    message=form.cleaned_data['message']
                )
                messages.success(request, 'Votre message a été envoyé avec succès !')
                return redirect('message_envoye')
    else:
        form = ContactForm()
    
    return render(request, 'blog/contact.html', {'form': form})
def message_envoye(request):
    return render(request, 'blog/message_envoye.html')