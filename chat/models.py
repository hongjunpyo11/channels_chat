from django.db import models
from django.contrib.auth.models import User


class Drawing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()
    message = models.CharField(max_length=255)
    redis_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


# 이러한 방식은 Redis에 저장된 그림 데이터와 PostgreSQL에 저장된 메시지 데이터를 매핑할 필요가 있으므로, 어떤 Redis 키와 PostgreSQL 레코드가 매핑되는지에 대한 정보도 저장해야 합니다. 이를 위해 Drawing 모델에 Redis 키를 저장할 필드를 추가해줄 수 있습니다.