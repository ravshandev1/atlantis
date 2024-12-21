from django.contrib import admin
from .translations import CustomAdmin
from .models import Contact, Carousel, About, Application, Partner, Step, OurSolve


@admin.register(Contact)
class ContactAdmin(CustomAdmin):
    pass


@admin.register(Carousel)
class CarouselAdmin(CustomAdmin):
    pass


@admin.register(About)
class AboutAdmin(CustomAdmin):
    pass


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Step)
class StepAdmin(CustomAdmin):
    pass


@admin.register(OurSolve)
class OurSolveAdmin(CustomAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
