from django.db import models

from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null = True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length = 50)
    description = models.TextField(_('description'), blank=True)
    enable = models.BooleanField(_('enable'), default = True)
    created_time = models.DateTimeField(_('created time'), auto_now_add = True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Categort')
        verbose_name_plural = _('categories')