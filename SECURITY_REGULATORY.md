# FANX Regülasyon & Güvenlik Çerçevesi

Bu doküman; SPK, MASAK, MiCA, VARA, FSEK ve TBK perspektiflerinden FANX modelinin
neden "finansal ürün" değil "kapalı devre dijital hizmet altyapısı" olduğunu açıklar.

---

## 1. Türkiye (SPK / 6493 / MASAK / TBK / FSEK)
### SPK (Sermaye Piyasası Kanunu)
- Yatırım sözleşmeleri, pasif sermaye koyup getiri bekleyen kişiye yöneliktir.
- FANX'te kazanç **sermaye koymadan** değil, **katkı sağlayarak** (XP → Credit) doğar.
- Dolayısıyla SPK anlamında "yatırım aracı" değildir.

### 6493 Sayılı Kanun (Ödeme ve Elektronik Para)
- Elektronik para: dışarıda harcanabilir dijital değerdir.
- FANX Credit yalnızca platform içinde harcanabilir, dış dünyaya çıkmaz.
- Bu yüzden "elektronik para kuruluşu lisansı" gerekmez.

### MASAK / AML
- Tüm cashout işlemleri KYC'li kullanıcı adına, kayıtlı IBAN/ödeme hesabına yapılır.
- Limitlidir, DAO onaylıdır, kayıt altındadır.
- "Hizmet bedeli iadesi" açıklamasıyla muhasebeleştirilir.
- Kapalı devre olduğu için kara para aklama risk modeli düşüktür.

### TBK m.393-394 (Hizmet Sözleşmesi)
- Kullanıcı platforma zaman/emek/katılım sunar → bu ifa edilmiş hizmettir.
- Cashout = hizmet bedelinin ödenmesi.
- Bu yapı temettü (kâr payı) değildir.

### FSEK (5846)
- Creator mali haklarını korur (m.21-25).
- Fan, "basit kullanım lisansı" alır (m.52), mülkiyet devri yok.
- Platform sadece lisans dağıtımını kayda alan hizmet altyapısıdır.

---

## 2. AB (MiCA / PSD2 / GDPR)
### MiCA (EU 2023/1114)
- MiCA, transfer edilebilir kripto varlıkları düzenler.
- FANX Credit kapalıdır, devredilemez, borsaya çıkmaz → MiCA lisansı gerekmez.

### PSD2
- FANX Credit dış dünyada ödeme aracı değildir; üçüncü kişiye transfer edilemez.
- Bu nedenle ödeme kuruluşu lisansı tetiklenmez.

### GDPR
- Kullanıcı verileri sadece puanlama ve güvenlik için işlenir.
- CCS (Composite Contribution Score) ve anti-bot analizi anonimize edilmiş metrikler üstünden yürür.

---

## 3. Dubai / VARA / DIFC / CBUAE
- VARA, "Virtual Asset Service Provider" lisansını dışa açık, transfer edilebilir tokenlar için zorunlu kılar.
- FANX Credit dışarı çıkmaz, başka cüzdana gidemez, borsa/bridge yoktur.
- Bu nedenle VARA lisansı gerektirmez.
- DIFC veri kuralları ve CBUAE ödeme gözetimi açısından: faaliyet "kapalı devre dijital hizmet kredisi" olarak konumlanır.

---

## 4. FATF (AML Standartları)
- FATF "VASP" (Virtual Asset Service Provider) tanımı, sınır ötesi değerin aktarılmasını hedefler.
- FANX değer birimleri sınır ötesi aktarılamaz ve üçüncü kişiye devredilemez.
- Cashout KYC'li olarak yalnızca kullanıcıya yapılır.

---

## 5. DAO, Şeffaflık, Sorumluluk
- DAO "fiyat" yönetmez, "parametre" yönetir:
  - Yakım oranı (αₜ)
  - Buyback oranı (ρₜ)
  - XP katsayıları (wᵢ)
  - R_conv (XP→Credit dönüşüm oranı)
  - Havuz dağılımları (Fan / Creator / DAO / Platform)
- Bu kararların hash'i off-chain ledger'da tutulur → geriye dönük manipülasyon iddiasına karşı delildir.

---

## 6. Savunma Cümlesi
> FANX bir yatırım vaadi değildir.  
> Kullanıcı kazancı "dijital hizmet ifası" karşılığıdır, temettü değildir.  
> Arz deflasyonisttir; yakım matematiksel kıtlık yaratır; bu spekülasyon değil, ekonomik verim yönetimidir.

---

© 2025 FANX • Bu belge hukuki tavsiye değildir; projeyi teknik olarak konumlandıran açıklayıcı çerçevedir.
