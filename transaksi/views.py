from django.shortcuts import render
from django.db.models import Sum, Count


from .models import Pelanggan, Sepatu, DetailPesanan

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def laporan_sepatu_terlaris_view(request):
    # Ambil sepatu terlaris dengan jumlah total terjual
    sepatu_terlaris = Sepatu.objects.annotate(
        total_terjual=Sum('detail_pesanan__pesan__jumlahBarang')
    ).order_by('-total_terjual')

    # Siapkan data untuk dikirim ke template
    laporan = [
        {
            "nama_sepatu": sepatu.nama,
            "merek": sepatu.merek,
            "total_terjual": sepatu.total_terjual or 0
        }
        for sepatu in sepatu_terlaris
    ]
    
    # Debugging: Print the laporan data to console
    print(laporan)

    # Kirim data laporan ke template
    return render(request, 'laporan_sepatu_terlaris.html', {'laporan': laporan})


def sepatu_pendapatan_view(request):
    # Query Sepatu and annotate total pendapatan (revenue)
    sepatu_pendapatan = Sepatu.objects.annotate(
        total_pendapatan=Sum('detail_pesanan__totalHarga')
    ).order_by('-total_pendapatan')  # Sort by total pendapatan

    # Prepare data for the template
    laporan = [
        {
            "nama_sepatu": sepatu.nama,
            "merek": sepatu.merek,
            "total_pendapatan": sepatu.total_pendapatan or 0  # Default to 0 if None
        }
        for sepatu in sepatu_pendapatan
    ]

    # Return the data to the template
    return render(request, 'laporan_sepatu_pendapatan.html', {'laporan': laporan})


# View for pelanggan with the most orders
def pelanggan_terbanyak_view(request):
    # Query Pelanggan and annotate with the number of orders
    pelanggan_terbanyak = Pelanggan.objects.annotate(
        jumlah_pesanan=Count('pesanan')
    ).order_by('-jumlah_pesanan')

    # Prepare data for the template
    laporan = [
        {
            "nama_pelanggan": f"{pelanggan.namaDepan} {pelanggan.namaBlkng}",
            "jumlah_pesanan": pelanggan.jumlah_pesanan
        }
        for pelanggan in pelanggan_terbanyak
    ]
    
    return render(request, 'laporan_pelanggan_terbanyak.html', {'laporan': laporan})

# View for pelanggan with the highest total spending
def pelanggan_pengeluaran_view(request):
    # Query Pelanggan and annotate with the total spending
    pelanggan_pengeluaran = Pelanggan.objects.annotate(
        total_pengeluaran=Sum('pesanan__detail_pesanan__totalHarga')
    ).order_by('-total_pengeluaran')

    # Prepare data for the template
    laporan = [
        {
            "nama_pelanggan": f"{pelanggan.namaDepan} {pelanggan.namaBlkng}",
            "total_pengeluaran": pelanggan.total_pengeluaran or 0  # Default to 0 if None
        }
        for pelanggan in pelanggan_pengeluaran
    ]
    
    return render(request, 'laporan_pelanggan_pengeluaran.html', {'laporan': laporan})


# View for total revenue (Total Pendapatan)
def total_pendapatan_view(request):
    # Calculate the total revenue from all DetailPesanan objects
    total_pendapatan = DetailPesanan.objects.aggregate(total=Sum('totalHarga'))['total']

    # Prepare data for the template
    context = {
        'total_pendapatan': total_pendapatan or 0  # Default to 0 if None
    }
    
    return render(request, 'laporan_total_pendapatan.html', context)

