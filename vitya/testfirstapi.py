import pytest
import requests

class TestFirstAPI:
    names = [
        ("Viktor"),
        ("Arseniy"),
        ("")
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, 'Wrong response code'#текст если проверка не выполнится
        #Проверяется, что статус-код ответа равен 200 (что означает успешный запрос). Если это не так, будет выдана ошибка с текстом 'Wrong response code'.

        response_dict = response.json()
        assert "answer" in response_dict, "there is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"
# - ожидаемый результат; + актуальный результат


