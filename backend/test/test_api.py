import requests
import pytest

import db


API_URL = "http://127.0.0.1:8000/api/offer/"


@pytest.fixture(scope="session")
def create_mortgage_offer():
    for data in [i for i in db.offers.values()]:
        res = requests.post(API_URL, json=data)
        assert res.status_code == 201
        data["id"] = res.json()["id"]
    yield
    for offer_id in [i["id"] for i in db.offers.values()]:
        res = requests.delete(API_URL + str(offer_id))
        assert res.status_code == 204


@pytest.mark.usefixtures('create_mortgage_offer')
class TestOffer:
    def test_get_offers(self):
        res = requests.get(API_URL)
        assert res.status_code == 200
        assert res.json() == [i for i in db.offers.values()]

    @pytest.mark.parametrize("offer, change_offer",
                             list(zip([i for i in db.offers.values()], [i for i in db.change_offers.values()]))
                             )
    def test_change_offers(self, offer, change_offer):
        res = requests.patch(API_URL + str(offer["id"]), json=change_offer)
        assert res.status_code == 200
        change_offer["id"] = offer["id"]
        assert res.json() == change_offer

    @pytest.mark.parametrize("wrong_offer", [i for i in db.wrong_offer.values()])
    def test_create_wrong_offers(self, wrong_offer):
        res = requests.post(API_URL, json=wrong_offer)
        assert res.status_code == 400
