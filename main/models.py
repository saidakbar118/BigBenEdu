from django.db import models


class About(models.Model):
    name = models.CharField(max_length=120)
    text = models.TextField()

    name1 = models.CharField(max_length=120)
    text1 = models.TextField()

    name2 = models.CharField(max_length=120)
    text2 = models.TextField()

    def __str__(self):
        return self.name


class Images(models.Model):
    image1 = models.ImageField(upload_to="images/")
    image2 = models.ImageField(upload_to="images/")
    image3 = models.ImageField(upload_to="images/")
    image4 = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"Images {self.id}"


class Text(models.Model):
    name = models.CharField(max_length=90)
    text = models.TextField()
    image = models.ImageField(upload_to="text/")

    name1 = models.CharField(max_length=90)
    text1 = models.TextField()
    image1 = models.ImageField(upload_to="text/")

    name2 = models.CharField(max_length=90)
    text2 = models.TextField()
    image2 = models.ImageField(upload_to="text/")

    name3 = models.CharField(max_length=90)
    text3 = models.TextField()
    image3 = models.ImageField(upload_to="text/")

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="album/")

    def __str__(self):
        return self.title


class Photo(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="photos",
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="album/")

    def __str__(self):
        return f"Photo {self.id} - {self.category.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class NotificationSettings(models.Model):
    """Telegram va email bildirishnomalari uchun yagona admin sozlamasi."""

    telegram_bot_token = models.CharField("Telegram bot tokeni", max_length=255, blank=True)
    telegram_chat_id = models.CharField("Telegram chat ID", max_length=100, blank=True)

    email_host = models.CharField("Email host", max_length=255, default="smtp.gmail.com")
    email_port = models.PositiveIntegerField("Email port", default=587)
    email_use_tls = models.BooleanField("TLS ishlatilsin", default=True)
    email_host_user = models.EmailField("Email manzili", blank=True)
    email_host_password = models.CharField("Email paroli (App Password)", max_length=255, blank=True)
    default_from_email = models.EmailField("Jo'natuvchi email", blank=True)
    contact_email = models.EmailField("Xabar qabul qiluvchi email", blank=True)

    class Meta:
        verbose_name = "Bildirishnoma sozlamasi"
        verbose_name_plural = "Bildirishnoma sozlamalari"

    def __str__(self):
        return "Telegram va email sozlamalari"
