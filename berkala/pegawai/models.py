from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PegawaiModel(models.Model):
    nama = models.CharField(max_length=100)
    jabatan = models.IntegerField(null=True)
    nip = models.CharField(max_length=100, null=True)
    opd = models.ForeignKey('OpdModel', models.DO_NOTHING, default=1)
    pangkat = models.IntegerField(null=True)
    pengguna = models.ForeignKey(User,models.DO_NOTHING, default=0000000)
    alamat  = models.CharField(max_length=255)
    telpon  = models.CharField(max_length=15)
    gaji_skrg = models.ForeignKey('GajiModel', models.DO_NOTHING, blank=True, null=True )

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
