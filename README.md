# FANX – Digital Service Economy (Closed-Loop Simulator)

**Power to the Time, Value to the People.**  
Bu depo; FANX kapalı devre dijital hizmet ekonomisinin çalışan bir simülasyonunu içerir.

---

## 🔁 Temel Döngü
`XP → Credit → Burn → Value → NEV → Reward → Adoption`

1. Kullanıcı platformda görev yapar → **XP** kazanır  
2. XP, DAO'nun tanımladığı katsayıyla **Credit**'e dönüşür  
3. Her işlemde mikro **Burn** yapılır → arz düşer  
4. Arz düştükçe kalan Credit'in **Value**'su yükselir  
5. Ekosistemin toplam değeri (**NEV**) büyür  
6. NEV'ten pay alan **Reward**, katkıya göre dağıtılır (temettü değil, TBK m.393'e göre hizmet karşılığıdır)  
7. Bu ödül motivasyonu artırır → sistem genişler

Bu yapı dış borsa veya spekülasyona değil,
katılım / üretim / lisanslı içerik ekonomisine dayanır.

---

## ⚖ Hukuki Çerçeve (Özet)
- **TBK m.393-394:** XP, dijital hizmet ifasıdır; Cashout hizmet bedeli iadesidir → yatırım getirisi değildir.
- **FSEK m.52:** Fan içerik satın aldığında mülkiyet almaz; sadece kullanım lisansı alır.
- **MiCA 2023/1114:** Credit transfer edilemez ve dış borsaya çıkmaz → "kripto varlık" lisansı gerekmez.
- **6493 sayılı Kanun:** FANX Credit, dış dünyada ödeme aracı olmadığı için elektronik para değildir.
- **MASAK / FATF:** Kapalı devre + KYC → AML uyumlu.

> Regülatör mesajı: FANX bir yatırım ürünü değildir; kapalı devre dijital hizmet altyapısıdır.

---

## 📂 Klasörler
- `streamlit_app.py`  
  Tek sayfalık tam simülasyon arayüzü (XP, Credit, Burn, NEV, Reward, DAO, Cashout).

- `core/`  
  - `economy_core.py` – Ekonomik hesap motoru  
  - `reward_system.py` – CCS / Reward dağıtımı  
  - `dao_engine.py` – DAO oy gücü, buyback mantığı

- `data/`  
  Örnek yaratıcı, fan ve sponsor verileri (CSV).

- `SECURITY_REGULATORY.md`  
  SPK / MASAK / MiCA / VARA / FSEK uyum özeti.

---

## ▶️ Lokal Çalıştırma
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## ☁ Streamlit Cloud
- Bu repoyu GitHub'a yükle.
- Streamlit Cloud → "New app"
  - Repo: `FANX-DigitalServiceEconomy`
  - Branch: `main`
  - Main file: `streamlit_app.py`
- Deploy.

---

### ⚠ Uyarı
Bu proje; ekonomik davranış modelini, kapalı devre arz dengesini ve hukuki uyumluluk mantığını göstermek için hazırlanmış bir simülasyondur.  
Hiçbir bölüm "getiri garantisi", "yatırım tavsiyesi", "menkul kıymet ihracı" niteliği taşımaz.

---

© 2025 FANX • Deflasyonist Kapalı Devre Dijital Hizmet Ekonomisi
