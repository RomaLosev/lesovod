from django.contrib import admin

from .models import Employers


class EmployersAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('position', 'name') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('work_since',) 

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Employers, EmployersAdmin) 