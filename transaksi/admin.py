from django.contrib import admin
from .models import Pelanggan, NomorTelepon, Sepatu, Pesan, DetailPesanan

# Konfigurasi untuk model Pelanggan
class NomorTeleponInline(admin.TabularInline):  # Inline untuk nomor telepon
    model = NomorTelepon
    extra = 1  # Menentukan jumlah form kosong saat menambahkan data baru

class PelangganAdmin(admin.ModelAdmin):
    list_display = ('idPel', 'namaDepan', 'namaBlkng', 'emailPel', 'tglLahirPel')  # Kolom yang ditampilkan
    search_fields = ('namaDepan', 'namaBlkng', 'emailPel')  # Kolom yang dapat dicari
    inlines = [NomorTeleponInline]  # Menampilkan nomor telepon langsung di halaman pelanggan

# Konfigurasi untuk model Sepatu
class SepatuAdmin(admin.ModelAdmin):
    list_display = ('idSepatu', 'merek', 'harga', 'stok')
    search_fields = ('merek',)
    list_filter = ('merek',)  # Filter berdasarkan merek

# Konfigurasi untuk model Pesan
class PesanAdmin(admin.ModelAdmin):
    list_display = ('idPesan', 'pelanggan', 'jumlahBarang')
    search_fields = ('idPesan',)
    list_filter = ('pelanggan',)  # Filter berdasarkan pelanggan

# Konfigurasi untuk model DetailPesanan
class DetailPesananAdmin(admin.ModelAdmin):
    list_display = ('idDetailPesanan', 'pesan', 'sepatu', 'tglPesan', 'tglPembayaran', 'totalHarga')
    search_fields = ('idDetailPesanan',)
    list_filter = ('tglPesan', 'tglPembayaran')

# Pendaftaran model ke admin panel
admin.site.register(Pelanggan, PelangganAdmin)
admin.site.register(Sepatu, SepatuAdmin)
admin.site.register(Pesan, PesanAdmin)
admin.site.register(DetailPesanan, DetailPesananAdmin)
