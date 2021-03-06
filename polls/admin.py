from django.contrib import admin

# Register your models here.
from polls.models import Poll,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    #extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
	# list_display = ('question', 'pub_date')
	# ERR IndentationError: unexpected indent
    inlines = [ChoiceInline] 

admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)
