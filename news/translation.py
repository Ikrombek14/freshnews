from .models import Post, Categories
from modeltranslation.translator import TranslationOptions, register



@register(Categories)
class CategoriesTranslation(TranslationOptions):
    fields = ('name',)


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ('title', 'content')
