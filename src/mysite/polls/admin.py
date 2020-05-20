from django.contrib import admin
from .models import Question,Choice

# 在管理界面添加数据类型
admin.site.register(Question)
admin.site.register(Choice)

