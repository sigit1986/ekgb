from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PegawaiModel(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.BigIntegerField(null=True)
    nip = models.CharField(max_length=100, null=True)
    opd = models.BigIntegerField(blank=True, null=True)
    pangkat = models.BigIntegerField(null=True)
    pengguna = models.BigIntegerField(blank=True, null=True)
    alamat  = models.CharField(max_length=255)
    telpon  = models.CharField(max_length=30)
    gaji_skrg = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nama

class PangkatModel(models.Model):
    nama = models.CharField(max_length=50)
    nilai = models.IntegerField()
    simbol =models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nama

class OpdModel(models.Model):
    nama = models.CharField(max_length=255)
    kepala_opd = models.IntegerField(null=True)

    def __str__(self):
        return self.nama

class JabatanModel(models.Model):
    nama = models.CharField(max_length=100)
    jenis = models.CharField(max_length=15)
    bup = models.IntegerField()
    jenjang = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

class GajiModel(models.Model):
    masa_kerja = models.IntegerField()
    golongan = models.CharField(max_length=5)
    tbgaji_currency = models.CharField(blank=True, null=True, max_length=255)
    terbilang = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.golongan

class BerkalaHistoryModel(models.Model):
    username    = models.CharField(max_length=255, blank=False, null=False)
    kgb_nomor = models.CharField(max_length=255, blank=False, null=False)
    kgb_tanggal = models.DateField(auto_now=True, blank=False, null=False)
    tmt         = models.DateField(blank=True, null=True)
    tmt_baru    = models.DateField(blank=True, null=True)
    golongan    = models.CharField(max_length=5)
    pejabat_ttd = models.CharField(max_length=255, default='GUBERNUR JAMBI')
    masa_kerja_tahun  = models.IntegerField(blank=True, null=True)
    masa_kerja_bulan  = models.IntegerField(blank=True, null=True)
    kgb_image = models.FileField(blank=True, null=True, upload_to = 'media')
    masa_kerjabaru_tahun  = models.IntegerField(blank=True, null=True)
    masa_kerjabaru_bulan  = models.IntegerField(blank=True, null=True)
    nilai= models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.golongan

class AkunModel(models.Model):
    JENIS_AKUN_CHOICES = (
        ('pegawai','Pegawai'),
        ('operator', 'Operator'),
        ('admin', 'Administrator'),
    )
    akun = models.BigIntegerField(blank=True, null=True)
    pegawai = models.BigIntegerField(blank=True, null=True)
    jenis_akun = models.CharField(max_length=20, choices=JENIS_AKUN_CHOICES)

    def __unicode__(self):
        return self.akun