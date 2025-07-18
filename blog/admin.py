from django.contrib import admin
from .models import Article, MessageContact

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_creation', 'categorie')
    search_fields = ('titre', 'auteur', 'categorie')
    list_filter = ('categorie', 'date_creation')

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'postenom', 'prénom', 'email', 'téléphone', 'message_court', 'date_envoi')
    search_fields = ('nom', 'postenom', 'prénom', 'email', 'message')
    list_filter = ('date_envoi',)

    # ✅ méthode personnalisée pour afficher un extrait du message
    def message_court(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_court.short_description = 'Message'
