from django.contrib import admin
from .models import Post

#CREIAMO IL MODELLO DI VISUALIZZAZIONE DEI POSTS, DEL FILTRO E DELLA RICERCA PER I POST
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'status', 'created_on', 'author',)
    list_filter=("status",)
    search_fields=['title', 'content']
    prepopulated_fields={'slug':('title',)}


# Register your models here.
admin.site.register(Post,PostAdmin)

