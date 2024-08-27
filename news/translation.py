from .models import Post, Categories
from modeltranslation.translator import TranslationOptions, register


class FieldTranslationOptions(TranslationOptions):
    fields = ('value',)


@register(Categories)
class CategoriesTranslation(TranslationOptions):
    fields = ('name',)


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ('title', 'content')
