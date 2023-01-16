# import pytube
# link = input("Silahkan Paste link disini : ")
# dn = pytube.YouTube(link)
# dn.streams.first(),download()
# print("file anda sudah didownload", link)

# cara ke 2
#Awal program

# Download Youtube Videos Directly From Python Script
import pytube

#isikan dengan url youtube yang akan di unduh
url = input("silahkan input linknya: ") 

video = pytube.YouTube(url)
youtube = video.streams.first()
youtube.download(r'C:\Users')
#sesuaikan dengan lokasi penyimpanan hasil download
#akhir program