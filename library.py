import tkinter as tk


class Kütüphane:
    def __init__(self):
        self.dosya_adı = "books.txt"

        try:
            dosya = open(self.dosya_adı, "r")
        except FileNotFoundError:
            dosya = open(self.dosya_adı, "w")
        finally:
            dosya.close()

    def dosyayı_kapat(self):
        pass 

    def kitapları_listele(self):
        try:
            with open(self.dosya_adı, "r") as dosya: # Dosyayı okuma modunda açar
                kitaplar = dosya.readlines()
                if not kitaplar:
                    self.etiket.config(text="Listelenecek Kitap Bulunamamıştır. Lütfen Kitap Ekleyin!")
                else:
                    kitap_metni = ""
                    for kitap in kitaplar:
                        bilgiler = kitap.strip().split(",")
                        kitap_metni += f"Kitabın Adı: {bilgiler[0]} - Kitabın Yazarı: {bilgiler[1]}\n"
                    self.etiket.config(text=kitap_metni)
        except FileNotFoundError:
            self.etiket.config(text="Dosya bulunamadı.")

    def kitap_ekle(self):
        kitap_adı = self.kitap_adı_giriş.get()
        yazar = self.yazar_giriş.get()
        yayın_tarihi = self.yayın_tarihi_giriş.get()
        sayfa_sayısı = self.sayfa_sayısı_giriş.get()

        with open(self.dosya_adı, "r") as dosya:
            kitaplar = dosya.readlines()
            for kitap in kitaplar:
                if kitap_adı in kitap:
                    self.etiket.config(text="Bu kitap zaten kütüphanede bulunmaktadır.")
                    return

        with open(self.dosya_adı, "a") as dosya: # Dosyayı ekleme modunda açar
            dosya.write(f"{kitap_adı},{yazar},{yayın_tarihi},{sayfa_sayısı}\n")
        self.etiket.config(text="Kitap Başarılı bir şekilde eklendi.")

    def kitap_sil(self):
        silinecek_kitap = self.kitap_sil_giriş.get() 
        with open(self.dosya_adı, "r") as dosya:
            kitaplar = dosya.readlines()

        with open(self.dosya_adı, "w") as dosya: # Dosyayı yazma modunda açar
            kitap_silindi = False
            for kitap in kitaplar:
                if not kitap.startswith(silinecek_kitap + ','): 
                    dosya.write(kitap)
                else:
                    kitap_silindi = True

        if kitap_silindi:
            self.etiket.config(text="Kitap Başarılı bir şekilde silindi.")
        else:
            self.etiket.config(text="Silmek istediğiniz kitap bulunamadı.")

    def arayüz_oluştur(self):
        self.ana_pencere = tk.Tk()
        self.ana_pencere.title("Kütüphane Yönetim Sistemi")

        self.etiket = tk.Label(self.ana_pencere, text="Hoş Geldiniz!")
        self.etiket.pack()

        self.listele_buton = tk.Button(self.ana_pencere, text="Kitapları Listele", command=self.kitapları_listele)
        self.listele_buton.pack()

        self.kitap_adı_etiket = tk.Label(self.ana_pencere, text="Kitap Adı:")
        self.kitap_adı_etiket.pack()
        self.kitap_adı_giriş = tk.Entry(self.ana_pencere)
        self.kitap_adı_giriş.pack()

        self.yazar_etiket = tk.Label(self.ana_pencere, text="Yazar:")
        self.yazar_etiket.pack()
        self.yazar_giriş = tk.Entry(self.ana_pencere)
        self.yazar_giriş.pack()

        self.yayın_tarihi_etiket = tk.Label(self.ana_pencere, text="Yayın Tarihi:")
        self.yayın_tarihi_etiket.pack()
        self.yayın_tarihi_giriş = tk.Entry(self.ana_pencere)
        self.yayın_tarihi_giriş.pack()

        self.sayfa_sayısı_etiket = tk.Label(self.ana_pencere, text="Sayfa Sayısı:")
        self.sayfa_sayısı_etiket.pack()
        self.sayfa_sayısı_giriş = tk.Entry(self.ana_pencere)
        self.sayfa_sayısı_giriş.pack()

        self.ekle_buton = tk.Button(self.ana_pencere, text="Kitap Ekle", command=self.kitap_ekle)
        self.ekle_buton.pack()

        self.kitap_sil_giriş_etiket = tk.Label(self.ana_pencere, text="Silmek İstediğiniz Kitap:")
        self.kitap_sil_giriş_etiket.pack()
        self.kitap_sil_giriş = tk.Entry(self.ana_pencere) 
        self.kitap_sil_giriş.pack()

        self.sil_buton = tk.Button(self.ana_pencere, text="Kitap Sil", command=self.kitap_sil)
        self.sil_buton.pack()

        self.çıkış_buton = tk.Button(self.ana_pencere, text="Çıkış", command=self.ana_pencere.quit)
        self.çıkış_buton.pack()

        self.ana_pencere.mainloop()

lib = Kütüphane()
lib.arayüz_oluştur()
