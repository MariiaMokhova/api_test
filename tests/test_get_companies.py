import pytest
from pprint import pprint
from Src.my_requests import MyRequests
from data.data_files import StatusCompanies

class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()
    @pytest.mark.parametrize("status", status_list)
    def test_get_statuses_companies(self, status):
        response = self.request.get(f"""/?status={status}&limit=3&offset=0""")
        # print()
        # pprint(response.json())
        assert response.status_code == 200, f'Status code is not 200, status code is {response.status_code}'

    @pytest.mark.parametrize("status", status_list)
    def test_get_closed_companies(self, status):
        response = self.request.get(f"""/?status={status}&limit=3&offset=0""")
        items_list = response.json()["data"]
        for item in items_list:
            assert item["company_status"] == status

    # def  test_get_closed_companies():
    #     response = requests.get(f"""{base_url}/?status=CLOSED&limit=3&offset=0""")
    #     print()
    #     pprint(response.json())
    #     assert response.status_code == 200, f'Status code is not 200, status code is {response.status_code}'
    #
    # def  test_get_bankrupt_companies():
    #     response = requests.get(f"""{base_url}/?status=BANKRUPT&limit=3&offset=0""")
    #     print()
    #     pprint(response.json())
    #     assert response.status_code == 200, f'Status code is not 200, status code is {response.status_code}'