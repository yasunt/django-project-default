from django.contrib import admin

from something.models import Something, Tag


class SomethingAdmin(admin.ModelAdmin):

    list_display = ('name', 'user', 'created', 'updated')
    readonly_fields = ('user', 'created', 'updated')
    date_hierarchy = 'created'


class TagAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'


admin.site.register(Something, SomethingAdmin)
admin.site.register(Tag, TagAdmin)
