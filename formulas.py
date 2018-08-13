

def calc_liquidity_metric(current_assets, current_liability):
    liquidity_metric = 1.0 * current_assets / current_liability
    return liquidity_metric


def calc_return_on_capital(company_earnings, total_capital):
    return_on_capital = 1.0 * company_earnings / total_capital
    return return_on_capital


def calc_free_cash_flow(operating_cash_flow, capital_expense):
    free_cash_flow = operating_cash_flow - capital_expense
    return free_cash_flow


def calc_price_earnings_ratio(price_per_share, earnings_per_share):
    price_earnings_ratio = 1.0 * price_per_share / earnings_per_share
    return price_earnings_ratio


def calc_expected_price_earnings_ratio(current_price_earnings_ratio, current_growth_rate, number_of_years):
    expected_price_earnings_ratio = 1.0 * current_price_earnings_ratio * current_growth_rate ** number_of_years
    return expected_price_earnings_ratio


def calc_expected_share_price(current_price_earnings_ratio, expected_price_earnings_ratio):
    expected_share_price = 1.0 * current_price_earnings_ratio * expected_price_earnings_ratio
    return expected_share_price


def calc_sticker_price(expected_share_price, minimal_acceptable_rate_of_return, number_of_years):
    sticker_price = 1.0 * expected_share_price * (1+minimal_acceptable_rate_of_return) ** -number_of_years
    return sticker_price


def calc_margin_of_safety_price(sticker_price, margin_of_safety):
    discount_price = sticker_price * margin_of_safety
    return discount_price


