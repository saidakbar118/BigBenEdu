from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_alter_text_image_alter_text_image1_alter_text_image2_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationSettings",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("telegram_bot_token", models.CharField(blank=True, max_length=255, verbose_name="Telegram bot tokeni")),
                ("telegram_chat_id", models.CharField(blank=True, max_length=100, verbose_name="Telegram chat ID")),
                ("email_host", models.CharField(default="smtp.gmail.com", max_length=255, verbose_name="Email host")),
                ("email_port", models.PositiveIntegerField(default=587, verbose_name="Email port")),
                ("email_use_tls", models.BooleanField(default=True, verbose_name="TLS ishlatilsin")),
                ("email_host_user", models.EmailField(blank=True, max_length=254, verbose_name="Email manzili")),
                ("email_host_password", models.CharField(blank=True, max_length=255, verbose_name="Email paroli (App Password)")),
                ("default_from_email", models.EmailField(blank=True, max_length=254, verbose_name="Jo'natuvchi email")),
                ("contact_email", models.EmailField(blank=True, max_length=254, verbose_name="Xabar qabul qiluvchi email")),
            ],
            options={
                "verbose_name": "Bildirishnoma sozlamasi",
                "verbose_name_plural": "Bildirishnoma sozlamalari",
            },
        ),
    ]
