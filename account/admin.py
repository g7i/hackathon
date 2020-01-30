from django.contrib import admin
from .models import Student,Mentor,Judge,ProblemCreator,User


class StudentAdmin(admin.ModelAdmin):
    list_display = ('username','branch', 'semester',)
    search_fields = ('=branch', '=semester','user__username')

    def username(self,obj):
        return obj.user.username

admin.site.register(Student, StudentAdmin)
admin.site.register(Mentor)
admin.site.register(Judge)
admin.site.register(ProblemCreator)
admin.site.register(User)
