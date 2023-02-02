from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, unique=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        abstract = True
