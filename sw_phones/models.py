from django.db import models

class Arp(models.Model):
    ip = models.CharField(max_length=200, blank=True, null=True)
    mac_huaweii = models.CharField(max_length=200, blank=True, null=True)
    port = models.CharField(max_length=200, blank=True, null=True)
    localidade = models.CharField(max_length=200, blank=True, null=True)
    switch_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True)
    up_to = models.DateTimeField(blank=True, null=True)
    aparelho_id = models.BigIntegerField(blank=True, null=True)
    mac = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = 'arp'


class Telefones(models.Model):
    ip = models.CharField(max_length=200, blank=True, null=True)
    port = models.CharField(max_length=200, blank=True, null=True)
    mac = models.CharField(max_length=200, blank=True, null=True)
    switch_status = models.CharField(max_length=200, blank=True, null=True)
    switch_up_to = models.DateTimeField(blank=True, null=True)
    ramal = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    tombo = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    setor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'telefones'
