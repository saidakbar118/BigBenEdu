from modeltranslation.translator import TranslationOptions,translator,register
from .models import *

    
@register(Text)
class TextTranslationOptions(TranslationOptions):
    fields = ('name','text','name1','text1','name2','text2','name3','text3')