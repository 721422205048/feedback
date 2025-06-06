from django.contrib import admin

# Register your models here.
from.models import Reviews
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields=("review_text",)
    list_filter=("rating",)

admin.site.register(Reviews,ReviewAdmin)