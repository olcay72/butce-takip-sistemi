from datetime import datetime

bugun = datetime.now().strftime("%d.%m.%Y")

print("--------HOŞ GELDİNİZ---------")
print(f"Tarih: {bugun}")

aylik_butce = float(input("Aylık bütçeniz:"))
gunluk_limit = float(input("Günlük harcama limitiniz:"))

harcamalar = []
kategoriler = ["Market","Yeme-İçme","Ulaşım","Eğlence","Eğitim","Fatura","Diğer"]

while True:
    print("\n=============================")
    print("          BÜTÇE TAKİP          ")
    print("===============================")
    print("1- Harcama Ekle")
    print("2- Harcamaları Listele")
    print("3- Harcama Sil")
    print("4- Kategoriye Göre Göster")
    print("5- Kategori özeti")
    print("6- Bugünkü Harcamalar")
    print("7- Bütçe Durumu")
    print("8- Kullanılan Kategoriler")
    print("9- Tasarruf Önerisi")
    print("0- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "0":
        print("Programdan çıkılıyor")
        break
    elif secim == "1":
        print("\n--- YENİ HARCAMA EKLE ---")
        isim = input("Harcama adı: ")
        tutar = float(input("Harcama tutarı (TL): "))

        print("\nKategoriler:")
        for sira, kat in enumerate(kategoriler, start=1):
            print(f"{sira} - {kat}")

        kat_secim = int(input("Kategori seçiniz (1-7): "))
        secilen_kategori = kategoriler[kat_secim - 1]
      
        an = datetime.now()
        tarih = an.strftime("%d.%m.%Y")
        saat = an.strftime("%H:%M")

        yeni_harcama = {
            "isim": isim,
            "tutar": tutar,
            "kategori": secilen_kategori,
            "tarih": tarih,
            "saat": saat
        }
        harcamalar.append(yeni_harcama)
        print(f"-> '{isim}' harcaması ({tutar} TL) başarıyla eklendi.")

    elif secim == "2":
        if not harcamalar:
            print("\nHenüz kayıtlı bir harcama bulunmuyor.")
        else:
            print("\n--- TÜM HARCAMALAR ---")
            for sira, h in enumerate(harcamalar, start = 1):
                print(f"\n{sira}. {h['isim']}")
                print(f"   Tutar: {h['tutar']} TL")
                print(f"   Kategori: {h['kategori']}")
                print(f"   Tarih: {h['tarih']} - {h['saat']}")
                print("-" * 25)


    elif secim == "3":
        if not harcamalar:
            print("\nSilinecek kayıtlı bir harcama bulunmuyor.")
        else:
            print("\n--- SİLİNECEK HARCAMAYI SEÇİN ---")
            for sira, h in enumerate(harcamalar, start=1):
                print(f"{sira} - {h['isim']} ({h['tutar']} TL)")
            sil_no = int(input("\nSilmek istediğiniz harcama numarası: "))
            silinecek_index = sil_no - 1

            if 0 <= silinecek_index < len(harcamalar):
                silinen = harcamalar[silinecek_index]
                onay = input(f"'{silinen['isim']} - {silinen['tutar']} TL' harcamasını silmek istediğinize emin misiniz? (E/H): ")

                if onay.upper() == "E":
                    harcamalar.pop(silinecek_index)
                    print("-> Harcama başarıyla silindi.")
                else:
                    print("-> Silme işlemi iptal edildi.")
            else:
                print("-> Geçersiz bir harcama numarası girdiniz.")
        
    elif secim == "4":
        print("Kategoriye Göre Gösterim: ")
    elif secim == "5":
        print("Kategori Özetiniz: ")
    elif secim == "6":
        print("Bugünkü Harcamalarınız: ")
    elif secim == "7":
        print("Bütçe Durumunuz: ")
    elif secim == "8":
        print("Kullandığınız kategoriler: ")
    elif secim == "9":
        print("Tasarruf Önerisi: ")
    else: 
        print("Geçersiz Bir Seçim Yaptınız. ")


