from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    surname = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=200, blank=True, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} {self.surname} - {self.subject or "بدون موضوع"}'