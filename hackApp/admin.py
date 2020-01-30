from django.contrib import admin
from .models import Problem,Idea



class IdeaAdmin(admin.ModelAdmin):
    list_display = ('branch', 'semester', 'problem_code',)
    search_fields = ('=user__branch','=user__semester', '=problem__code',)

    def problem_code(self, instance):
        return instance.problem.code

    def semester(self, instance):
        return instance.user.semester

    def branch(self, instance):
        return instance.user.branch


admin.site.register(Idea, IdeaAdmin)
admin.site.register(Problem)
