from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر")
    price = models.PositiveIntegerField(verbose_name="قیمت")
    discount_price = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="قیمت با تخفیف"
    )
    description = models.TextField(verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    count = models.IntegerField(verbose_name="تعداد")
    Category = models.CharField(max_length=32, verbose_name="دسته‌بندی")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_final_price(self):
        """قیمت نهایی بعد از تخفیف"""
        if self.discount_price is not None:
            return self.discount_price
        return self.price
