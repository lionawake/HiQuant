import pickle

findat = pickle.load(open('fin_data.pkl', 'rb'))

def fa_eps_basic(stock):
    """00156,1,1"""
    return findat.at[stock, 'fa_eps_basic']

def fa_eps_diluted(stock):
    """00157,1,1"""
    return findat.at[stock, 'fa_eps_diluted']

def fa_bps(stock):
    """00158,1,1"""
    return findat.at[stock, 'fa_bps']


def fa_grps(stock):
    """00159,1,1"""
    return findat.at[stock, 'fa_grps']


def fa_orps(stock):
    """00160,1,1"""
    return findat.at[stock, 'fa_orps']


def fa_opps(stock):
    """00161,1,1"""
    return findat.at[stock, 'fa_opps']


def fa_capsurpps(stock):
    """00162,1,1"""
    return findat.at[stock, 'fa_capsurpps']


def fa_spps(stock):
    """00163,1,1"""
    return findat.at[stock, 'fa_spps']


def fa_undistributedps(stock):
    """00164,1,1"""
    return findat.at[stock, 'fa_undistributedps']


def fa_retainedps(stock):
    """00165,1,1"""
    return findat.at[stock, 'fa_retainedps']


def fa_fcffps(stock):
    """00166,1,1"""
    return findat.at[stock, 'fa_fcffps']


def fa_fcfeps(stock):
    """00167,1,1"""
    return findat.at[stock, 'fa_fcfeps']


def fa_cceps(stock):
    """00168,1,1"""
    return findat.at[stock, 'fa_cceps']


def fa_divcover_ttm(stock):
    """00169,1,1"""
    return findat.at[stock, 'fa_divcover_ttm']


def fa_retainedearn_ttm(stock):
    """00170,1,1"""
    return findat.at[stock, 'fa_retainedearn_ttm']


def fa_cfps_ttm(stock):
    """00171,1,1"""
    return findat.at[stock, 'fa_cfps_ttm']


def fa_ocfps_ttm(stock):
    """00172,1,1"""
    return findat.at[stock, 'fa_ocfps_ttm']


def fa_opps_ttm(stock):
    """00173,1,1"""
    return findat.at[stock, 'fa_opps_ttm']


def fa_roe_avg(stock):
    """00174,1,1"""
    return findat.at[stock, 'fa_roe_avg']


def fa_roe_wgt(stock):
    """00175,1,1"""
    return findat.at[stock, 'fa_roe_wgt']


def fa_roe_diluted(stock):
    """00176,1,1"""
    return findat.at[stock, 'fa_roe_diluted']


def fa_roe_exbasic(stock):
    """00177,1,1"""
    return findat.at[stock, 'fa_roe_exbasic']


def fa_roe_exdiluted(stock):
    """00178,1,1"""
    return findat.at[stock, 'fa_roe_exdiluted']


def fa_roenp_ttm(stock):
    """00179,1,1"""
    return findat.at[stock, 'fa_roenp_ttm']


def fa_roaebit_ttm(stock):
    """00180,1,1"""
    return findat.at[stock, 'fa_roaebit_ttm']


def fa_netprofittoassets_ttm(stock):
    """00181,1,1"""
    return findat.at[stock, 'fa_netprofittoassets_ttm']


def fa_roic_ttm(stock):
    """00182,1,1"""
    return findat.at[stock, 'fa_roic_ttm']


def fa_roicebit_ttm(stock):
    """00183,1,1"""
    return findat.at[stock, 'fa_roicebit_ttm']


def fa_roc_ttm(stock):
    """00184,1,1"""
    return findat.at[stock, 'fa_roc_ttm']


def fa_roa_ttm(stock):
    """00185,1,1"""
    return findat.at[stock, 'fa_roa_ttm']


def fa_roaavg5y(stock):
    """00186,1,1"""
    return findat.at[stock, 'fa_roaavg5y']


def fa_roe_ttm(stock):
    """00187,1,1"""
    return findat.at[stock, 'fa_roe_ttm']


def fa_roeavg5y(stock):
    """00188,1,1"""
    return findat.at[stock, 'fa_roeavg5y']


def fa_protocost_ttm(stock):
    """00189,1,1"""
    return findat.at[stock, 'fa_protocost_ttm']


def fa_profittogr_ttm(stock):
    """00190,1,1"""
    return findat.at[stock, 'fa_profittogr_ttm']


def fa_optoor_ttm(stock):
    """00191,1,1"""
    return findat.at[stock, 'fa_optoor_ttm']


def fa_optogr_ttm(stock):
    """00192,1,1"""
    return findat.at[stock, 'fa_optogr_ttm']


def fa_ebittogr_ttm(stock):
    """00193,1,1"""
    return findat.at[stock, 'fa_ebittogr_ttm']


def fa_sellexpensetogr_ttm(stock):
    """00194,1,1"""
    return findat.at[stock, 'fa_sellexpensetogr_ttm']


def fa_adminexpensetogr_ttm(stock):
    """00195,1,1"""
    return findat.at[stock, 'fa_adminexpensetogr_ttm']


def fa_finaexpensetogr_ttm(stock):
    """00196,1,1"""
    return findat.at[stock, 'fa_finaexpensetogr_ttm']


def fa_impairtogr_ttm(stock):
    """00197,1,1"""
    return findat.at[stock, 'fa_impairtogr_ttm']


def fa_octogr_ttm(stock):
    """00198,1,1"""
    return findat.at[stock, 'fa_octogr_ttm']


def fa_netprofittoor_ttm(stock):
    """00199,1,1"""
    return findat.at[stock, 'fa_netprofittoor_ttm']


def fa_taxtoprofitbt_ttm(stock):
    """00200,1,1"""
    return findat.at[stock, 'fa_taxtoprofitbt_ttm']


def fa_netprofitmargin_ttm(stock):
    """00201,1,1"""
    return findat.at[stock, 'fa_netprofitmargin_ttm']


def fa_grossprofitmargin_ttm(stock):
    """00202,1,1"""
    return findat.at[stock, 'fa_grossprofitmargin_ttm']


def fa_expensetosales_ttm(stock):
    """00203,1,1"""
    return findat.at[stock, 'fa_expensetosales_ttm']


def fa_salestocost_ttm(stock):
    """00204,1,1"""
    return findat.at[stock, 'fa_salestocost_ttm']


def fa_taxratio_ttm(stock):
    """00205,1,1"""
    return findat.at[stock, 'fa_taxratio_ttm']


def fa_acca_ttm(stock):
    """00206,1,1"""
    return findat.at[stock, 'fa_acca_ttm']


def fa_berryratio_ttm(stock):
    """00207,1,1"""
    return findat.at[stock, 'fa_berryratio_ttm']


def fa_operincometopbt(stock):
    """00208,1,1"""
    return findat.at[stock, 'fa_operincometopbt']


def fa_operincometopbt_ttm(stock):
    """00209,1,1"""
    return findat.at[stock, 'fa_operincometopbt_ttm']


def fa_chgvaluetopbt_ttm(stock):
    """00210,1,1"""
    return findat.at[stock, 'fa_chgvaluetopbt_ttm']


def fa_nonoperprofittopbt_ttm(stock):
    """00211,1,1"""
    return findat.at[stock, 'fa_nonoperprofittopbt_ttm']


def fa_optopbt_ttm(stock):
    """00212,1,1"""
    return findat.at[stock, 'fa_optopbt_ttm']


def fa_pbttoor_ttm(stock):
    """00213,1,1"""
    return findat.at[stock, 'fa_pbttoor_ttm']


def fa_profittomv_ttm(stock):
    """00214,1,1"""
    return findat.at[stock, 'fa_profittomv_ttm']


def fa_pttomvavg5y(stock):
    """00215,1,1"""
    return findat.at[stock, 'fa_pttomvavg5y']


def fa_salescashtoor(stock):
    """00216,1,1"""
    return findat.at[stock, 'fa_salescashtoor']


def fa_salescashtoor_ttm(stock):
    """00217,1,1"""
    return findat.at[stock, 'fa_salescashtoor_ttm']


def fa_ocftoor(stock):
    """00218,1,1"""
    return findat.at[stock, 'fa_ocftoor']


def fa_ocftoor_ttm(stock):
    """00219,1,1"""
    return findat.at[stock, 'fa_ocftoor_ttm']


def fa_ocftooai_ttm(stock):
    """00220,1,1"""
    return findat.at[stock, 'fa_ocftooai_ttm']


def fa_ocftoop_ttm(stock):
    """00221,1,1"""
    return findat.at[stock, 'fa_ocftoop_ttm']


def fa_cashdivcover_ttm(stock):
    """00222,1,1"""
    return findat.at[stock, 'fa_cashdivcover_ttm']


def fa_cashrecovratio_ttm(stock):
    """00223,1,1"""
    return findat.at[stock, 'fa_cashrecovratio_ttm']


def fa_noncurassetsratio(stock):
    """00224,1,1"""
    return findat.at[stock, 'fa_noncurassetsratio']


def fa_curassetsratio(stock):
    """00225,1,1"""
    return findat.at[stock, 'fa_curassetsratio']


def fa_equitytointerestdebt(stock):
    """00226,1,1"""
    return findat.at[stock, 'fa_equitytointerestdebt']


def fa_equitytocapital(stock):
    """00227,1,1"""
    return findat.at[stock, 'fa_equitytocapital']


def fa_current(stock):
    """00228,1,1"""
    return findat.at[stock, 'fa_current']


def fa_quick(stock):
    """00229,1,1"""
    return findat.at[stock, 'fa_quick']


def fa_superquick(stock):
    """00230,1,1"""
    return findat.at[stock, 'fa_superquick']


def fa_tangibleatointerestdebt(stock):
    """00231,1,1"""
    return findat.at[stock, 'fa_tangibleatointerestdebt']


def fa_tangibleassettonetdebt(stock):
    """00232,1,1"""
    return findat.at[stock, 'fa_tangibleassettonetdebt']


def fa_debttotangibleafybl(stock):
    """00233,1,1"""
    return findat.at[stock, 'fa_debttotangibleafybl']


def fa_ocftodebt(stock):
    """00234,1,1"""
    return findat.at[stock, 'fa_ocftodebt']


def fa_ocftointerestdebt_ttm(stock):
    """00235,1,1"""
    return findat.at[stock, 'fa_ocftointerestdebt_ttm']


def fa_ocftonetdebt_ttm(stock):
    """00236,1,1"""
    return findat.at[stock, 'fa_ocftonetdebt_ttm']


def fa_interestdebttocapital(stock):
    """00237,1,1"""
    return findat.at[stock, 'fa_interestdebttocapital']


def fa_debttoequity(stock):
    """00238,1,1"""
    return findat.at[stock, 'fa_debttoequity']


def fa_ebittointerest(stock):
    """00239,1,1"""
    return findat.at[stock, 'fa_ebittointerest']


def fa_uncurdebttoworkcap(stock):
    """00240,1,1"""
    return findat.at[stock, 'fa_uncurdebttoworkcap']


def fa_blev(stock):
    """00241,1,1"""
    return findat.at[stock, 'fa_blev']


def fa_cfotocurliabs_ttm(stock):
    """00242,1,1"""
    return findat.at[stock, 'fa_cfotocurliabs_ttm']


def fa_cashtocurliabs(stock):
    """00243,1,1"""
    return findat.at[stock, 'fa_cashtocurliabs']


def fa_arturn_ttm(stock):
    """00244,1,1"""
    return findat.at[stock, 'fa_arturn_ttm']


def fa_apturn_ttm(stock):
    """00245,1,1"""
    return findat.at[stock, 'fa_apturn_ttm']


def fa_faturn_ttm(stock):
    """00246,1,1"""
    return findat.at[stock, 'fa_faturn_ttm']


def fa_taturn_ttm(stock):
    """00247,1,1"""
    return findat.at[stock, 'fa_taturn_ttm']


def fa_turndays_ttm(stock):
    """00248,1,1"""
    return findat.at[stock, 'fa_turndays_ttm']


def fa_invturndays_ttm(stock):
    """00249,1,1"""
    return findat.at[stock, 'fa_invturndays_ttm']


def fa_arturndays_ttm(stock):
    """00250,1,1"""
    return findat.at[stock, 'fa_arturndays_ttm']


def fa_apturndays_ttm(stock):
    """00251,1,1"""
    return findat.at[stock, 'fa_apturndays_ttm']


def fa_invturn_ttm(stock):
    """00252,1,1"""
    return findat.at[stock, 'fa_invturn_ttm']


def fa_cashcnvcycle_ttm(stock):
    """00253,1,1"""
    return findat.at[stock, 'fa_cashcnvcycle_ttm']


def fa_currtassetstrate_ttm(stock):
    """00254,1,1"""
    return findat.at[stock, 'fa_currtassetstrate_ttm']


def fa_naturn_ttm(stock):
    """00255,1,1"""
    return findat.at[stock, 'fa_naturn_ttm']


def fa_orgr_ttm(stock):
    """00256,1,1"""
    return findat.at[stock, 'fa_orgr_ttm']


def fa_ncgr_ttm(stock):
    """00257,1,1"""
    return findat.at[stock, 'fa_ncgr_ttm']


def fa_tpgr_ttm(stock):
    """00258,1,1"""
    return findat.at[stock, 'fa_tpgr_ttm']


def fa_oigr_ttm(stock):
    """00259,1,1"""
    return findat.at[stock, 'fa_oigr_ttm']


def fa_npgr_ttm(stock):
    """00260,1,1"""
    return findat.at[stock, 'fa_npgr_ttm']


def fa_nppcgr_ttm(stock):
    """00261,1,1"""
    return findat.at[stock, 'fa_nppcgr_ttm']


def fa_cfogr_ttm(stock):
    """00262,1,1"""
    return findat.at[stock, 'fa_cfogr_ttm']


def fa_cffgr_ttm(stock):
    """00263,1,1"""
    return findat.at[stock, 'fa_cffgr_ttm']


def fa_cfigr_ttm(stock):
    """00264,1,1"""
    return findat.at[stock, 'fa_cfigr_ttm']


def fa_gpmgr_ttm(stock):
    """00265,1,1"""
    return findat.at[stock, 'fa_gpmgr_ttm']


def fa_tagr(stock):
    """00266,1,1"""
    return findat.at[stock, 'fa_tagr']


def fa_nagr(stock):
    """00267,1,1"""
    return findat.at[stock, 'fa_nagr']


def fa_earnmom8qtr(stock):
    """00268,1,1"""
    return findat.at[stock, 'fa_earnmom8qtr']


def fa_fcff(stock):
    """00269,1,1"""
    return findat.at[stock, 'fa_fcff']


def fa_fcfe(stock):
    """00270,1,1"""
    return findat.at[stock, 'fa_fcfe']


def fa_nrgl(stock):
    """00271,1,1"""
    return findat.at[stock, 'fa_nrgl']


def fa_oaincome(stock):
    """00272,1,1"""
    return findat.at[stock, 'fa_oaincome']


def fa_workcapital(stock):
    """00273,1,1"""
    return findat.at[stock, 'fa_workcapital']


def fa_tangibleasset(stock):
    """00274,1,1"""
    return findat.at[stock, 'fa_tangibleasset']


def fa_retainearn(stock):
    """00275,1,1"""
    return findat.at[stock, 'fa_retainearn']


def fa_interestdebt(stock):
    """00276,1,1"""
    return findat.at[stock, 'fa_interestdebt']


def fa_netdebt(stock):
    """00277,1,1"""
    return findat.at[stock, 'fa_netdebt']


def fa_nicurdebt(stock):
    """00278,1,1"""
    return findat.at[stock, 'fa_nicurdebt']


def fa_ninocurdebt(stock):
    """00279,1,1"""
    return findat.at[stock, 'fa_ninocurdebt']


def fa_ebiat(stock):
    """00280,1,1"""
    return findat.at[stock, 'fa_ebiat']


def fa_da(stock):
    """00281,1,1"""
    return findat.at[stock, 'fa_da']


def fa_equity(stock):
    """00282,1,1"""
    return findat.at[stock, 'fa_equity']


def fa_investcapital(stock):
    """00283,1,1"""
    return findat.at[stock, 'fa_investcapital']


def fa_totassets(stock):
    """00284,1,1"""
    return findat.at[stock, 'fa_totassets']


def fa_fixassets(stock):
    """00285,1,1"""
    return findat.at[stock, 'fa_fixassets']


def fa_totliab(stock):
    """00286,1,1"""
    return findat.at[stock, 'fa_totliab']


def fa_totequity(stock):
    """00287,1,1"""
    return findat.at[stock, 'fa_totequity']


def fa_cce(stock):
    """00288,1,1"""
    return findat.at[stock, 'fa_cce']


def fa_gr_ttm(stock):
    """00289,1,1"""
    return findat.at[stock, 'fa_gr_ttm']


def fa_gc_ttm(stock):
    """00290,1,1"""
    return findat.at[stock, 'fa_gc_ttm']


def fa_or_ttm(stock):
    """00291,1,1"""
    return findat.at[stock, 'fa_or_ttm']


def fa_ocnf_ttm(stock):
    """00292,1,1"""
    return findat.at[stock, 'fa_ocnf_ttm']


def fa_oef_ttm(stock):
    """00293,1,1"""
    return findat.at[stock, 'fa_oef_ttm']


def fa_gp_ttm(stock):
    """00294,1,1"""
    return findat.at[stock, 'fa_gp_ttm']


def fa_sellexpense_ttm(stock):
    """00295,1,1"""
    return findat.at[stock, 'fa_sellexpense_ttm']


def fa_adminexpense_ttm(stock):
    """00296,1,1"""
    return findat.at[stock, 'fa_adminexpense_ttm']


def fa_finaexpense_ttm(stock):
    """00297,1,1"""
    return findat.at[stock, 'fa_finaexpense_ttm']


def fa_perexpense_ttm(stock):
    """00298,1,1"""
    return findat.at[stock, 'fa_perexpense_ttm']


def fa_interestexpense_ttm(stock):
    """00299,1,1"""
    return findat.at[stock, 'fa_interestexpense_ttm']


def fa_mininterest_ttm(stock):
    """00300,1,1"""
    return findat.at[stock, 'fa_mininterest_ttm']


def fa_impairloss_ttm(stock):
    """00301,1,1"""
    return findat.at[stock, 'fa_impairloss_ttm']


def fa_operactincome_ttm(stock):
    """00302,1,1"""
    return findat.at[stock, 'fa_operactincome_ttm']


def fa_chavalincome_ttm(stock):
    """00303,1,1"""
    return findat.at[stock, 'fa_chavalincome_ttm']


def fa_op_ttm(stock):
    """00304,1,1"""
    return findat.at[stock, 'fa_op_ttm']


def fa_nooperprofit_ttm(stock):
    """00305,1,1"""
    return findat.at[stock, 'fa_nooperprofit_ttm']


def fa_ebitunver_ttm(stock):
    """00306,1,1"""
    return findat.at[stock, 'fa_ebitunver_ttm']


def fa_tax_ttm(stock):
    """00307,1,1"""
    return findat.at[stock, 'fa_tax_ttm']


def fa_ebt_ttm(stock):
    """00308,1,1"""
    return findat.at[stock, 'fa_ebt_ttm']


def fa_profit_ttm(stock):
    """00309,1,1"""
    return findat.at[stock, 'fa_profit_ttm']


def fa_netprofit_ttm(stock):
    """00310,1,1"""
    return findat.at[stock, 'fa_netprofit_ttm']


def fa_deductprofit_ttm(stock):
    """00311,1,1"""
    return findat.at[stock, 'fa_deductprofit_ttm']


def fa_ebit_ttm(stock):
    """00312,1,1"""
    return findat.at[stock, 'fa_ebit_ttm']


def fa_ebitdainver_ttm(stock):
    """00313,1,1"""
    return findat.at[stock, 'fa_ebitdainver_ttm']


def fa_ebitda_ttm(stock):
    """00314,1,1"""
    return findat.at[stock, 'fa_ebitda_ttm']


def fa_salescash_ttm(stock):
    """00315,1,1"""
    return findat.at[stock, 'fa_salescash_ttm']


def fa_operactcashflow_ttm(stock):
    """00316,1,1"""
    return findat.at[stock, 'fa_operactcashflow_ttm']


def fa_inveactcashflow_ttm(stock):
    """00317,1,1"""
    return findat.at[stock, 'fa_inveactcashflow_ttm']


def fa_finaactcashflow_ttm(stock):
    """00318,1,1"""
    return findat.at[stock, 'fa_finaactcashflow_ttm']


def fa_cashflow_ttm(stock):
    """00319,1,1"""
    return findat.at[stock, 'fa_cashflow_ttm']


def fa_opertax_ttm(stock):
    """00320,1,1"""
    return findat.at[stock, 'fa_opertax_ttm']
