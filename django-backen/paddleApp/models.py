from django.db import models
from django.utils import timezone


# Create your models here.

# 扩展django用户信息
class UserProfile(models.Model):
  user_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
  pass_word = models.CharField(max_length=30, null=True, blank=True, verbose_name="密码")
  create_at = models.DateTimeField("生成日期", default=timezone.now)
  update_at = models.DateTimeField("更新日期", auto_now=True)


# ocr 记录
class Ocr_record(models.Model):
  image = models.TextField(null=True, blank=True, verbose_name="检测图片base64")
  text = models.TextField(verbose_name="检测文本", null=True)
  is_sen = models.CharField(max_length=20, verbose_name="是否有敏感词汇", default="否")
  sen_txt = models.TextField(verbose_name="敏感词汇", null=True)
  after_txt = models.TextField(verbose_name="检测之后的敏感词汇", null=True)
  create_at = models.DateTimeField("生成日期", default=timezone.now)
  update_at = models.DateTimeField("更新日期", auto_now=True)
