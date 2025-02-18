from django.contrib import admin

from .models import About, Payment, ContactInfo


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'short_text']
    list_editable = ['content']
    list_display_links = ['title']


    def short_text(self, obj):
        return obj.trim()

    short_text.short_description = 'Текст'

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'short_text']
    list_editable = ['content']
    list_display_links = ['title']

    def short_text(self, obj):
        return obj.trim()

    short_text.short_description = 'Текст'

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(ContactInfo)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'short_text']
    list_editable = ['content']
    list_display_links = ['title']

    def short_text(self, obj):
        return obj.trim()

    short_text.short_description = 'Текст'

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
