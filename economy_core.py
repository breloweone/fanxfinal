import numpy as np

def compute_xp(watch_min, shares, messages, content_creations,
               k_watch=1.0, k_share=2.0, k_msg=1.2, k_content=5.0):
    """Toplam XP hesaplar (ham XP)."""
    xp = (
        watch_min * k_watch +
        shares * k_share +
        messages * k_msg +
        content_creations * k_content
    )
    return xp

def quality_adjusted_xp(xp_raw, ai_quality_score):
    """AI kalite katsayısı uygular (0-1)."""
    return xp_raw * ai_quality_score

def xp_to_credit(xp_real, r_conv):
    """XP -> Credit dönüşümü (DAO tarafından belirlenen katsayı)."""
    return xp_real * r_conv

def burn_and_buyback(supply_t,
                     volume_credit,
                     burn_rate_alpha,
                     dao_reserve,
                     buyback_rho):
    """supply_{t+1} = supply_t - burn_t - buyback_t"""
    burn_t = burn_rate_alpha * volume_credit
    buyback_t = dao_reserve * buyback_rho
    new_supply = max(supply_t - burn_t - buyback_t, 0)
    return new_supply, burn_t, buyback_t

def compute_nev(revenue_xp,
                revenue_content,
                revenue_sponsor,
                revenue_premium,
                revenue_msg,
                cost_server,
                cost_ops,
                cost_rewards,
                cost_cashout,
                cost_buyback):
    """NEV = gelirler - giderler"""
    gross = (revenue_xp + revenue_content +
             revenue_sponsor + revenue_premium + revenue_msg)
    costs = (cost_server + cost_ops +
             cost_rewards + cost_cashout + cost_buyback)
    nev = gross - costs
    return max(nev, 0), gross, costs

def value_per_credit(nev_t, supply_t1):
    """Credit başına teorik değer = NEV / arz"""
    if supply_t1 <= 0:
        return 0.0
    return nev_t / supply_t1
