from django.contrib import admin

from karpeles.content.models import HomeText, PracticeArea, AboutText, Attorney, AttorneyText, PracticeText, ResourceText, ContactText, DisclaimerText, SubArea

class HomeTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(HomeText, HomeTextAdmin)

class PracticeAreaAdmin(admin.ModelAdmin):
    pass
admin.site.register(PracticeArea, PracticeAreaAdmin)

class SubAreaAdmin(admin.ModelAdmin):
    pass
admin.site.register(SubArea, SubAreaAdmin)

class AboutTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(AboutText, AboutTextAdmin)

class AttorneyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attorney, AttorneyAdmin)

class AttorneyTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(AttorneyText, AttorneyTextAdmin)

class PracticeTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(PracticeText, PracticeTextAdmin)

class ResourceTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(ResourceText, ResourceTextAdmin)

class ContactTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(ContactText, ContactTextAdmin)

class DisclaimerTextAdmin(admin.ModelAdmin):
    pass
admin.site.register(DisclaimerText, DisclaimerTextAdmin)
