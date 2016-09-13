from django.contrib import admin
from breakdown_search.models import Node, InstructionStep


class NodeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'node_text')

admin.site.register(Node, NodeAdmin)
admin.site.register(InstructionStep)
# Register your models here.
