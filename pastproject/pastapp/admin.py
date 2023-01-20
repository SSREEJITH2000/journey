from django.contrib import admin
from . models import venue
from .models import doc
from . models import team

# Register your models here.
admin.site.register(venue)
admin.site.register(doc)
admin.site.register(team)