from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # ユーザーネームとパスワードはAbstractUserを継承しているので、
    # デフォルトで用意されています。

    # 誕生日フィールド
    birth_date = models.DateField(null=True, blank=True)

    # 年齢フィールド
    age = models.PositiveIntegerField(null=True, blank=True)

    # stage_cleartフィールド
    stage_cleart = models.IntegerField(default=0)


class Comment(models.Model):
    # authorフィールドをForeignKeyに変更
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='投稿者')
    text = models.TextField('投稿内容')
    date = models.DateField('投稿日時', auto_now_add=True)

    def __str__(self):
        return self.text