from lifetimes import BetaGeoFitter, GammaGammaFitter

def fit_clv_models(summary_df):
    bgf = BetaGeoFitter(penalizer_coef=0.01)
    bgf.fit(summary_df["frequency"], summary_df["recency"], summary_df["T"])

    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(summary_df["frequency"], summary_df["monetary_value"])

    return bgf, ggf
