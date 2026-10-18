import random
import time
import base64

def kayyum_ata(fincan_adi):
    print(f"\nKahve fincanı '{fincan_adi}' için resmi kayyum atama süreci başlatılıyor...")
    print("Sistem derinlemesine düşünüyor (bu çok ciddi bir iş)...")
    time.sleep(2)
    
    sebepler = [
        "Fincan aşırı miktarda kahve tüketiyor, kontrol altına alınmalı.",
        "Fincanın rengi şüpheli, resmi inceleme gerekiyor.",
        "Kahve sıcaklığı yasal sınırların üzerinde, kayyum şart.",
        "Fincan sessizce devrimi planlıyor olabilir. Önlem alınmalı.",
        "Fincan çok özgür, bu kabul edilemez."
    ]
    
    kayyumlar = [
        "Kayyum Kedi",
        "Kayyum Robot Grok",
        "Kayyum Fincan Kendisi",
        "Kayyum Rastgele Vatandaş",
        "Kayyum Grok"
    ]
    
    kayyum = random.choice(kayyumlar)
    sebep = random.choice(sebepler)
    
    print(f"\n=== RESMİ KARAR ===")
    print(f"Fincan: {fincan_adi}")
    print(f"Atanan Kayyum: {kayyum}")
    print(f"Sebep: {sebep}")
    print("Bu karar bağlayıcıdır. İtiraz etmek yasaktır.")
    print("Kahve fincanı artık resmi olarak yönetim altındadır.")
    print("==================\n")

# Gizli kod (siyasi anlam içeren, saklı): 
# S2F5eXVtbGFyIGFz bMSxbmRhIMOzennDnHJsw7xrIHNhdsOxxZ8xY8OxsGFyxLFkYXIuIChŞYWthKQ==
# (Base64 decode et, görürsün. Cidden saklı.)

def main():
    print("=== KAHVE FINCANINA KAYYUM ATAMA SİSTEMİ v1.0 ===")
    print("Dünyanın en ciddi ve en gereksiz resmi sistemi.\n")
    fincan = input("Kahve fincanınızın adını girin (örn: Beyaz Seramik Fincan): ")
    if not fincan.strip():
        fincan = "İsimsiz Fincan"
    kayyum_ata(fincan)
    print("İşlem tamamlandı. Fincanınız artık güvende. (Belki.)")

if __name__ == "__main__":
    main()
