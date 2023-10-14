from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    url =  models.CharField(max_length=512)
    parent = models.ForeignKey("self",
                               null=True, 
                               blank=True,
                               default=None,
                               related_name='children',
                               on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return str(self.name)

    def get_children(self):
        return self.children.all()
