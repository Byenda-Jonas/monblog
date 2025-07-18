from django import forms
from .models import Article
from .models import MessageContact

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'auteur', 'categorie', 'contenu', 'image']
class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label='Votre nom')
    postenom = forms.CharField(max_length=100, label='Votre postenom')
    prénom = forms.CharField(max_length=100, label='Votre prénom')
    email = forms.EmailField(label='Votre email')
    téléphone = forms.CharField(max_length=100, label='Votre téléphone')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class ContactForm(forms.ModelForm):
    captcha = forms.CharField(
        required=True,
        label="Quel est le résultat de 2 + 2 ?",
        widget=forms.TextInput(attrs={'placeholder': 'Entrez la réponse'})
    )

    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput
    )

    class Meta:
        model = MessageContact
        fields = ['nom', 'postenom', 'prénom', 'téléphone', 'email', 'message']

    def clean_honeypot(self):
        data = self.cleaned_data['honeypot']
        if data:
            raise forms.ValidationError("Spam détecté.")
        return data