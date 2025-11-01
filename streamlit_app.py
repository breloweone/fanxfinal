\
import streamlit as st
from core.economy_core import (
    compute_xp,
    quality_adjusted_xp,
    xp_to_credit,
    burn_and_buyback,
    value_per_credit,
)
from core.reward_system import compute_ccs, distribute_reward
from core.dao_engine import vote_power, dao_decision_example

st.set_page_config(
    page_title="FANX Closed-Loop Economy Simulator",
    layout="wide"
)

st.title("💠 FANX Closed-Loop Economy Simulator")
st.caption("XP → Credit → Burn → Value → NEV → Reward → DAO • 'Power to the Time, Value to the People.'")

# Sidebar global params
st.sidebar.header("GLOBAL PARAMETRELER")

supply_t = st.sidebar.number_input(
    "Mevcut Toplam Arz (Supply_t) [₣]",
    min_value=1_000_000, max_value=2_000_000_000,
    value=1_000_000_000, step=1_000_000
)

dao_reserve = st.sidebar.number_input(
    "DAO Rezervi (₣)",
    min_value=0, max_value=500_000_000,
    value=200_000_000, step=1_000_000
)

r_conv = st.sidebar.slider(
    "XP→Credit Dönüşüm Katsayısı (R_conv) [DAO belirler]",
    min_value=0.01, max_value=1.0, value=0.1, step=0.01
)

fan_pool_ratio = st.sidebar.slider(
    "Fan Pool Oranı (s_fan ~ %40)",
    min_value=0.10, max_value=0.80, value=0.40, step=0.01
)

st.sidebar.markdown("---")
st.sidebar.markdown("**UYARI (Hukuki):**")
st.sidebar.markdown("- Bu ekran yatırım getirisi taahhüdü değildir.")
st.sidebar.markdown("- Cashout, TBK m.393 kapsamında ifa bedeli ödemesidir.")
st.sidebar.markdown("- Sistem kapalı devredir; dış borsa yoktur.")

st.header("1️⃣ Kullanıcı Katkısı → XP Üretimi")

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    watch_min = st.number_input("🎥 İzleme (dakika)", min_value=0, value=30, step=1)
with c2:
    shares = st.number_input("🔗 Paylaşım (adet)", min_value=0, value=5, step=1)
with c3:
    messages = st.number_input("💬 Mesajlaşma (adet)", min_value=0, value=10, step=1)
with c4:
    content_creations = st.number_input("🧠 İçerik Üretimi (adet)", min_value=0, value=2, step=1)
with c5:
    ai_quality_score = st.slider("AI Kalite Skoru (0-1)", min_value=0.0, max_value=1.0, value=0.9, step=0.05)

xp_raw = compute_xp(
    watch_min=watch_min,
    shares=shares,
    messages=messages,
    content_creations=content_creations,
    k_watch=1.0,
    k_share=2.0,
    k_msg=1.2,
    k_content=5.0,
)
xp_real = quality_adjusted_xp(xp_raw, ai_quality_score)
credit_gained = xp_to_credit(xp_real, r_conv=r_conv)

st.markdown(f"**Ham XP:** `{xp_raw:.2f}`")
st.markdown(f"**AI Düzeltilmiş XP (XP_real):** `{xp_real:.2f}`")
st.markdown(f"**Kazanılan Credit (₣):** `{credit_gained:.4f}`")
st.caption("📜 TBK m.393-394: Bu kazanım yatırım değil; ifa edilmiş dijital hizmetin karşılığıdır.")

st.header("2️⃣ Fan Pool → Katkıya Dayalı Reward (Temettü Değil)")

nev_current_usd = st.number_input(
    "Ekosistem NEV (USD)",
    min_value=0, max_value=1_000_000_000,
    value=100_000, step=10_000
)

active_users = st.number_input(
    "Aktif Kullanıcı Sayısı",
    min_value=1, max_value=200_000_000,
    value=100_000, step=1_000
)

fan_pool_amount = nev_current_usd * fan_pool_ratio
avg_reward_per_user = fan_pool_amount / active_users if active_users > 0 else 0

st.markdown(f"**Fan Pool (USD):** `{fan_pool_amount:,.2f}`")
st.markdown(f"**Kullanıcı Başına Teorik Pay (USD/yıl):** `{avg_reward_per_user:,.4f}`")
st.caption("Bu ödeme temettü değildir. Sermaye pasif durmaz; katkı zorunludur.")

st.header("3️⃣ Burn + Buyback → Arzın Deflasyonist Daralması")

cA, cB = st.columns(2)
with cA:
    burn_rate_alpha = st.slider(
        "Yakım Oranı αₜ (0 - 5%)",
        min_value=0.0, max_value=0.05, value=0.02, step=0.005
    )
with cB:
    buyback_rho = st.slider(
        "Buyback Oranı ρₜ (DAO Rezerv Yüzdesi)",
        min_value=0.0, max_value=0.10, value=0.03, step=0.01
    )

volume_credit = st.number_input(
    "Dönemsel İşlem Hacmi (Credit cinsinden)",
    min_value=0.0, max_value=200_000_000.0,
    value=500_000.0, step=10_000.0
)

new_supply, burned, buyback_amt = burn_and_buyback(
    supply_t=supply_t,
    volume_credit=volume_credit,
    burn_rate_alpha=burn_rate_alpha,
    dao_reserve=dao_reserve,
    buyback_rho=buyback_rho
)

st.markdown(f"**Yakılan Credit (Burn_t):** `{burned:,.2f} ₣`")
st.markdown(f"**DAO Buyback ile Çekilen:** `{buyback_amt:,.2f} ₣`")
st.markdown(f"**Yeni Arz (Supply_t+1):** `{new_supply:,.2f} ₣`")
st.caption("Burn finansal işlem değildir; arzın dijital olarak azaltılmasıdır. MiCA / VARA kapsamı dışındadır.")

st.header("4️⃣ NEV / Supply → Credit Başına Değer (Valueₜ₊₁)")

value_next = value_per_credit(nev_current_usd, new_supply)
st.markdown(f"**Yeni Değer (USD / ₣):** `{value_next:.8f}`")
st.caption("Bu fiyat spekülasyonu değildir; ekonomik verimlilik oranıdır (NEV / Supply).")

st.header("5️⃣ DAO Yönetimi ve Şeffaflık")

cD1, cD2, cD3 = st.columns(3)
with cD1:
    FTX_i = st.number_input("FTX_i (devredilemez güven puanı)", min_value=0.0, value=50.0, step=1.0)
with cD2:
    RS_i = st.number_input("RS_i (itibar / CCS tabanlı skor)", min_value=0.0, value=30.0, step=1.0)
with cD3:
    weight_cap = st.slider("Weight (balina kilidi)", min_value=0.1, max_value=1.0, value=0.3, step=0.1)

vp = vote_power(FTX_i, RS_i, weight_cap)
st.markdown(f"**VotePower_i:** `{vp:.2f}`")
st.caption("FTX_i ve RS_i satılamaz → Oy hakkı satın alınamaz → Balina kontrolü engellenir.")

dao_params = dao_decision_example(
    alpha_burn=burn_rate_alpha,
    rho_buyback=buyback_rho,
    r_conv=r_conv
)
st.subheader("DAO Parametreleri")
st.json(dao_params)
st.caption("DAO finansal getiri dağıtmaz; yalnızca sistem dengesini yönetir. Bu yüzden SPK/SEC tipi 'yatırım komitesi' değildir.")

st.header("6️⃣ Cashout Modeli (Hizmet Bedeli İadesi)")

user_cashout_request = st.number_input(
    "Kullanıcının talep ettiği Cashout (₣)",
    min_value=0.0, max_value=1_000_000.0,
    value=200.0, step=10.0
)
cashout_limit_weekly = 500.0
cashout_allowed = user_cashout_request <= cashout_limit_weekly

st.markdown(f"**Haftalık Limit:** `{cashout_limit_weekly} ₣`")
st.markdown(f"**Talep:** `{user_cashout_request} ₣`")
st.markdown(f"**Durum:** {'✅ Onaylanabilir' if cashout_allowed else '⛔ Limit Aşıldı'}")
st.caption("Cashout = dijital hizmet karşılığı ödeme. Kumar/bahis değildir; TBK m.393 kapsamında hizmet bedeli ödemesidir.")

st.header("7️⃣ CCS (Composite Contribution Score) ve Reward Dağıtımı")

cC1, cC2, cC3 = st.columns(3)
with cC1:
    active_score = st.slider("Aktiflik Skoru", 0.0, 100.0, 70.0, 1.0)
with cC2:
    quality_score = st.slider("Kalite Skoru", 0.0, 100.0, 90.0, 1.0)
with cC3:
    network_score = st.slider("Ağ Etkisi Skoru", 0.0, 100.0, 30.0, 1.0)

ccs_me = compute_ccs(active_score, quality_score, network_score)
ccs_others = [55, 40, 25]
dist_list = distribute_reward(fan_pool_amount, [ccs_me] + ccs_others)
my_reward_usd = dist_list[0] if dist_list else 0

st.markdown(f"**Benim CCS:** `{ccs_me:.2f}`")
st.markdown(f"**Benim Reward Payım (USD):** `{my_reward_usd:,.4f}`")
st.caption("Bu, pasif gelir değildir. Bu, benim fiilen sağladığım katkının bedelidir.")

st.header("8️⃣ Ekonomik Toplam Özet")

summary_payload = {
    "Toplam XP (AI sonrası)": xp_real,
    "Toplam Credit": credit_gained,
    "Yakım (Burn_t)": burned,
    "Buyback_t": buyback_amt,
    "Yeni Arz (Supply_t+1)": new_supply,
    "NEV (USD)": nev_current_usd,
    "Credit Başına Değer (USD/₣)": value_next,
    "Fan Pool (USD)": fan_pool_amount,
    "Kullanıcı Başına Teorik Pay (USD/yıl)": avg_reward_per_user,
    "CCS Skorum": ccs_me,
    "Reward Payım (USD)": my_reward_usd,
    "Cashout Limit İçinde mi?": cashout_allowed,
}

st.json(summary_payload)

st.success("Sistem kapalı devredir. Değer üretimi emek-temelli, arz deflasyonist, DAO şeffaf; cashout ise hizmet bedeli iadesidir.")

st.markdown("---")
st.markdown("© 2025 FANX • Dijital Hizmet Ekonomisi • Bu simülasyon yatırım tavsiyesi değildir.\nTBK 393, FSEK 52, MiCA 4(3), VARA 2023 uyum mantığı gözetilmiştir.")
