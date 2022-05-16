import requests


def get_offers(price: int, deposit: int, term: int) -> str:
    """
    Get offers from banks

    :param price: Real estate value, int
    :param deposit: An initial fee, int
    :param term: Mortgage term, int
    :return:
    JSON or error status code
    """
    query_params = {"price": price, "deposit": deposit, "term": term}
    response = requests.get("http://127.0.0.1:8000/api/offer/", params=query_params)
    if response.status_code == 200:
        data = response.json()
        return data
    return response.status_code

def get_monthly_payment(amount: int, loan_rate:float, years:int) -> float:
    """
    Monthly payment calculation

    :param amount: Amount of credit, int
    :param loan_rate: Interest rate, int
    :param years: Mortgage term, int
    :return:
    Monthly payment, float
    """
    mounts_count = 12 * years
    monthly_rate = loan_rate / 1200
    k = (monthly_rate * (1 + monthly_rate) ** mounts_count) / (((1 + monthly_rate) ** mounts_count) - 1)
    m_payment = amount * k
    return m_payment
