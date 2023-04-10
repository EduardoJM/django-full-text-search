from django.contrib import admin
from .models import Music, Singer, Feat

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    pass

class FeatInlineAdmin(admin.StackedInline):
    model = Feat
    extra = 0

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    inlines = [FeatInlineAdmin]
