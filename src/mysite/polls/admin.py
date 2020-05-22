from django.contrib import admin
from .models import Question,Choice

# 在管理界面添加数据类型

admin.site.register(Choice)
# admin.site.register(Question)

class QuestionAdminEx(admin.ModelAdmin):
    fields =['pub_date','question_text']


class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ('问题内容',{'fields':['question_text']}),
        ('日期信息',{'fields':['pub_date']}),
    ]

# admin.site.register(Question,QuestionAdmin)
admin.site.register(Question,QuestionAdmin)

