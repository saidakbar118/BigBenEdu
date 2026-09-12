import logging

import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

from .models import (
    About,
    Images,
    Text,
    Category,
    NotificationSettings,
)

from .forms import ContactForm

logger = logging.getLogger(__name__)


def get_notification_settings():
    """Admin sozlamasini, u bo'lmasa .env qiymatlarini qaytaradi."""
    notification_settings = NotificationSettings.objects.first()
    if notification_settings:
        return notification_settings

    class EnvironmentSettings:
        telegram_bot_token = getattr(settings, "TELEGRAM_BOT_TOKEN", "")
        telegram_chat_id = getattr(settings, "TELEGRAM_CHAT_ID", "")
        email_host = getattr(settings, "EMAIL_HOST", "smtp.gmail.com")
        email_port = getattr(settings, "EMAIL_PORT", 587)
        email_use_tls = getattr(settings, "EMAIL_USE_TLS", True)
        email_host_user = getattr(settings, "EMAIL_HOST_USER", "")
        email_host_password = getattr(settings, "EMAIL_HOST_PASSWORD", "")
        default_from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "")
        contact_email = getattr(settings, "CONTACT_EMAIL", "")

    return EnvironmentSettings()


def send_telegram_notification(contact, notification_settings):
    """Yangi contact xabari kelganda Telegram botga xabar yuboradi."""

    token = notification_settings.telegram_bot_token
    chat_id = notification_settings.telegram_chat_id

    if not token or not chat_id:
        logger.warning(
            "TELEGRAM_BOT_TOKEN yoki TELEGRAM_CHAT_ID sozlanmagan, "
            "Telegram xabari yuborilmadi."
        )
        return

    text = (
        "🔔 <b>Big Ben saytida yangi xabar!</b>\n\n"
        f"👤 <b>Ism:</b> {contact.name}\n"
        f"📧 <b>Email:</b> {contact.email}\n"
        f"📞 <b>Telefon:</b> {contact.phone or '-'}\n\n"
        f"💬 <b>Xabar:</b>\n{contact.message}"
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        response = requests.post(
            url,
            data={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML",
            },
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        logger.exception("Telegram xabarini yuborishda xatolik yuz berdi.")


def index_view(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save()
            notification_settings = get_notification_settings()

            email_connection = get_connection(
                host=notification_settings.email_host,
                port=notification_settings.email_port,
                username=notification_settings.email_host_user,
                password=notification_settings.email_host_password,
                use_tls=notification_settings.email_use_tls,
            )

            email = EmailMessage(
                subject=f"Big Ben saytida yangi xabar: {contact.name}",
                body=(
                    f"Ism: {contact.name}\n"
                    f"Email: {contact.email}\n"
                    f"Telefon: {contact.phone}\n\n"
                    f"Xabar:\n"
                    f"{contact.message}"
                ),
                from_email=(
                    notification_settings.default_from_email
                    or notification_settings.email_host_user
                ),
                to=[
                    notification_settings.contact_email
                ],
                reply_to=[
                    contact.email
                ],
                connection=email_connection,
            )
            email.send(fail_silently=False)

            send_telegram_notification(contact, notification_settings)

            messages.success(
                request,
                "Xabaringiz muvaffaqiyatli yuborildi!"
            )

            return redirect("index")

    context = {
        "about": About.objects.first(),
        "images": Images.objects.first(),
        "text": Text.objects.first(),
        "contact_form": contact_form,
    }

    return render(
        request,
        "index.html",
        context
    )


def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        "album.html",
        {
            "categories": categories
        }
    )


def category_detail(request, pk):
    category = get_object_or_404(
        Category,
        pk=pk
    )

    photos = category.photos.all()

    return render(
        request,
        "photo_album.html",
        {
            "category": category,
            "photos": photos
        }
    )
