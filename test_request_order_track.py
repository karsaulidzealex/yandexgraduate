import sender_stand_request

# Функция создания нового заказа и получения его номера
def get_new_order_number():
    # Сохраняем в переменную user_response запрос на создание нового заказа
    user_response = sender_stand_request.create_new_order()
    # Сохраняем в переменную new_order_number номер заказа
    new_order_number = user_response.json()["track"]
    # Возвращаем номер заказа как результат работы функции
    return new_order_number

# Функция для позитивной проверки получения номера заказа
def request_order_by_track_number():
    # Получаем новый номер заказа и сохраняем его в переменную new_track_id
    new_track_id = get_new_order_number()
    # Сохраняем наш запрос в переменную user_response
    user_response = sender_stand_request.request_order_by_track_number(track_id=new_track_id)
    # Проверяем, что тест прошел успешно
    assert user_response.status_code == 200

# Позитивный тест на проверку получения номера заказа
def test_request_order_by_track_number():
    request_order_by_track_number()