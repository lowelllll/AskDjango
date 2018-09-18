from iamport import Iamport
from uuid import uuid4
from django.conf import settings
from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    amount = models.PositiveIntegerField()
    photo = models.ImageField()
    is_public = models.BooleanField(default=False,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    item = models.ForeignKey(Item)
    name = models.CharField(max_length=100, verbose_name='상품명')
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    merchant_uid = models.UUIDField(default=uuid4, editable=False) # 수정할 수 없음.
    imp_uid = models.CharField(max_length=100, blank=True) # 아임포트에서 주는 id
    status = models.CharField(
        max_length=9,
        choices=(
            ('ready','미결제'),
            ('paid','결제완료'),
            ('cancelled','결제취소'),
            ('failed','결제실패'),
        ),
        default='ready',
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    @property
    def api(self):
        # iamport client 인스턴스
        return Iamport(settings.IAMPORT_API_KEY,settings.IAMPORT_API_SECRET)

    def update(self,commit=True,meta=None):
        # 결제내역 갱신
        if self.imp_uid:
            self.meta = meta or self.api.find(imp_uid=self.imp_uid) # API 요청해서 결제내역 받아옴
            assert str(self.merchant_uid) == self.meta['merchant_uid'] # merchant_uid는  반드시 일치해야함! 일치하지 않으면 assert 에러 ! 
            self.status = self.meta['status']
        if commit == True:
            self.save()

