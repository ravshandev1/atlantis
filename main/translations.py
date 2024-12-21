from modeltranslation.translator import TranslationOptions, register
from .models import Contact, About, Step, OurSolve, Carousel
from modeltranslation.admin import TranslationAdmin


class CustomAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(About)
class AboutTranslation(TranslationOptions):
    fields = ['text', 'philosophy', 'mission']


@register(Carousel)
class CarouselTranslation(TranslationOptions):
    fields = ['title', 'text']


@register(OurSolve)
class OurSolveTranslation(TranslationOptions):
    fields = ['title', 'text']


@register(Step)
class StepTranslation(TranslationOptions):
    fields = ['text']


@register(Contact)
class StepTranslation(TranslationOptions):
    fields = ['address', 'working_time']
