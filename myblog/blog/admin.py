from django.contrib import admin
from .models import Post, Comment

@admin.register(Post) # @는 함수나 클래스를 꾸며주는 데코레이터!!!
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'writer',
        'content',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'title',
        'writer',
        'content',
        'created_at',
        'updated_at',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'writer',
        'content',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'writer',
        'content',
        'created_at',
        'updated_at',
    )