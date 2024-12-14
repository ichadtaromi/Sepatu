from django.db import models

class Pelanggan(models.Model):
    idPel = models.AutoField(primary_key=True)
    namaDepan = models.CharField(max_length=50)
    namaBlkng = models.CharField(max_length=50)
    alamatPel = models.TextField()
    emailPel = models.EmailField(unique=True)
    tglLahirPel = models.DateField()

    def __str__(self):
        return f"{self.namaDepan} {self.namaBlkng}"


class NomorTelepon(models.Model):
    idNoTlpPel = models.AutoField(primary_key=True)
    nomorTelepon = models.CharField(max_length=20)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, related_name='nomor_telepon')

    def __str__(self):
        return self.nomorTelepon


class Sepatu(models.Model):
    idSepatu = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    merek = models.CharField(max_length=50)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()

    def __str__(self):
        return f"{self.merek} - {self.harga}"


class Pesan(models.Model):
    idPesan = models.AutoField(primary_key=True)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, related_name='pesanan')
    jumlahBarang = models.IntegerField()

    def __str__(self):
        return f"Pesanan {self.idPesan} oleh {self.pelanggan}"


class DetailPesanan(models.Model):
    idDetailPesanan = models.AutoField(primary_key=True)
    pesan = models.ForeignKey(Pesan, on_delete=models.CASCADE, related_name='detail_pesanan')
    sepatu = models.ForeignKey(Sepatu, on_delete=models.CASCADE, related_name='detail_pesanan')
    tglPesan = models.DateField()
    tglPembayaran = models.DateField()
    totalHarga = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Detail Pesanan {self.idDetailPesanan} - Pesan {self.pesan.idPesan}"
