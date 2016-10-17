from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    list_display_links = ["updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
