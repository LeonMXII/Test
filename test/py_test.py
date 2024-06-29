import pytest
import os
import requests

token = os.getenv("token")

class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            "Authorization": f"OAuth {token}"
        }

    @pytest.mark.parametrize(
        "key,value,statuscode",
        (
            ["pat", "Test", 400],
            ["path", "Test", 201],
            ["path", "Test", 409]
        )
    )

    def test_create_folder(self, key, value, statuscode):
        params = {key: value}
        resource = requests.put("https://cloud-api.yandex.net/v1/disk/resources",
                                headers=self.headers,
                                params=params)
        assert resource.status_code == statuscode

# Тест с ошибкой
    def setup_method_1(self):
        self.headers = {
                "Authorization": f"OAuth {token}"
        }

    @pytest.mark.parametrize(
        "key,value,statuscode",
        (
                ["pat", "Python", 401],
                ["path", "Python", 202],
                ["path", "Python", 404]
        )
    )
    def test_create_folder_1(self, key, value, statuscode):
        params = {key: value}
        resource = requests.put("https://cloud-api.yandex.net/v1/disk/resources",
                                headers=self.headers,
                                params=params)
        assert resource.status_code == statuscode

if __name__ == "__main__":
    pytest.main()
