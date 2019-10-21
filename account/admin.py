from django.contrib import admin
from .models import Student,Mentor,Judge,ProblemCreator,User

admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Judge)
admin.site.register(ProblemCreator)
admin.site.register(User)