from django.contrib import admin

# Register your models here.
from .models import Post, Stock, Category, Member, Media_Group, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    pass

@admin.register(Media_Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
