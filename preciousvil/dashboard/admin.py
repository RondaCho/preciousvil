from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Progress, Tag, House, House_Tag


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    actions = ['make_published', 'make_draft']
    list_display = ['id', 'title', 'tag_list', 'created_at', 'status']

    def tag_list(self, progress):
        return ', '.join(tag.name for tag in progress.tag_set.all())

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{} 포스팅이 성공적으로 발행되었습니다.'.format(updated_count))

    make_published.short_description = '선택된 포스팅을 발행 상태로 변경합니다.'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}개 변경 성공적'.format(updated_count))

    make_draft.short_description = '선택된 포스팅을 Draft 상태로 변경합니다.'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['type', 'address', 'total_land', 'your_land', 'price', 'house_tag_list']

    def house_tag_list(self, house):
        return ', '.join(house_tag.name for house_tag in house.house_tag_set.all())


@admin.register(House_Tag)
class HouseTagAdmin(admin.ModelAdmin):
    list_display = ['name']

