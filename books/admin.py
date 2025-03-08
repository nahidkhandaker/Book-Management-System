from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Book


# Change the top blue bar text "Django administration"
admin.site.site_header = "Book Library Management"

# Change the "Site administration" text
admin.site.index_title = "Library Dashboard"

# Also changes the browser tab title
admin.site.site_title = "Book Library Admin"

# Register your models here.
    
admin.site.register(Book)