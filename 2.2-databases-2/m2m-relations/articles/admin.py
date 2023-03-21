from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, TagsArticle, Tags


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        check_main = 0
        for form in self.forms:
            if form.cleaned_data:
                if not form.cleaned_data['is_main']:
                    continue
                elif check_main > 0:
                    raise ValidationError('Основной раздел всегда один')
                else:
                    check_main += 1
            elif check_main == 0:
                raise ValidationError('Заполните основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = TagsArticle
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass

