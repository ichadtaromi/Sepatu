"""
URL configuration for Sepatu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from transaksi.views import laporan_sepatu_terlaris_view, home, contact, about, sepatu_pendapatan_view, pelanggan_terbanyak_view, pelanggan_pengeluaran_view, total_pendapatan_view

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('sepatu-terlaris/', laporan_sepatu_terlaris_view, name='laporan_sepatu_terlaris_view'),
    path('laporan/sepatu-pendapatan/', sepatu_pendapatan_view, name='laporan_sepatu_pendapatan_view'),
    path('laporan/pelanggan-terbanyak/', pelanggan_terbanyak_view, name='laporan_pelanggan_terbanyak_view'),
    path('laporan/pelanggan-pengeluaran/', pelanggan_pengeluaran_view, name='laporan_pelanggan_pengeluaran_view'),
    path('laporan/total-pendapatan/', total_pendapatan_view, name='laporan_total_pendapatan_view'),
    path('contact/', contact, name='contact'),  # Contact page URL
    path('about/', about, name='about'), 
]
