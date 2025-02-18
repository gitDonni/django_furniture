from django.db import models


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.CharField(verbose_name='Заголовок текста')
    text_on_page = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def trim(self):
        return f'{self.text_on_page[:130]}...'

    def __str__(self):
        return self.content


class Payment(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.CharField(verbose_name='Заголовок текста')
    text_on_page = models.TextField(verbose_name='Текст')

    def trim(self):
        return f'{self.text_on_page[:130]}...'

    class Meta:
        verbose_name = 'Доставка и оплата'
        verbose_name_plural = 'Доставка и оплата'

    def __str__(self):
        return self.content


class ContactInfo(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.CharField(verbose_name='Заголовок текста')
    text_on_page = models.TextField(verbose_name='Текст')
    phone = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    facebook = models.URLField(verbose_name='Facebook', blank=True, null=True)
    instagram = models.URLField(verbose_name='Instagram', blank=True, null=True)
    vk = models.URLField(verbose_name='Vkontakte', blank=True, null=True)


    def trim(self):
        return f'{self.text_on_page[:130]}...'

    class Meta:
        verbose_name = 'контактная информация'
        verbose_name_plural = 'Контактные информации'

    def __str__(self):
        return self.content