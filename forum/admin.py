from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','title','description', 'file', 'owner', 'date_created', 'hidden')  # Поля для поиска
    filter_horizontal = ('tags',)   

admin.site.register(TagsModel)
admin.site.register(PostModel, PostAdmin)
admin.site.register(CommentModel)
admin.site.register(SubcommentModel)
