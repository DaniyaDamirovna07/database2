from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if self.deleted_forms and self._should_delete_form(form):
                continue
            elif form.cleaned_data.get('is_main'):
                count += 1
            if count > 1:
                raise ValidationError('Основным может быть только один раздел')
            elif count == 0:
                raise ValidationError('Укажите основной раздел')
            else:
                pass
        
        return super().clean()
    
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass
