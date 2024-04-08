from django.db import models

NULLABLE = {"null": True, "blank": True}


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание", **NULLABLE)
    preview = models.ImageField(
        upload_to="catalog/blog", verbose_name="Изображение", **NULLABLE
    )
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"""Публикация с заголовком {self.title}\n создана {self.created_at}\n"""

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"
        ordering = (
            "title",
            "created_at",
            "view_count",
        )
