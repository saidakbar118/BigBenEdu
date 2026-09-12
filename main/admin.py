from django.contrib import admin

from .models import (
    About,
    Images,
    Text,
    Category,
    Photo,
    ContactMessage,
    NotificationSettings,
)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ("id",)


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class PhotoInline(admin.TabularInline):

    model = Photo

    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
    )

    inlines = [
        PhotoInline
    ]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "category",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "created_at",
    )

    list_display_links = (
        "id",
        "name",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "message",
    )

    list_filter = (
        "created_at",
    )

    readonly_fields = (
        "created_at",
    )


@admin.register(NotificationSettings)
class NotificationSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Telegram", {
            "fields": ("telegram_bot_token", "telegram_chat_id"),
        }),
        ("Email (SMTP)", {
            "fields": (
                "email_host",
                "email_port",
                "email_use_tls",
                "email_host_user",
                "email_host_password",
                "default_from_email",
                "contact_email",
            ),
        }),
    )

    def has_add_permission(self, request):
        return not NotificationSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
