import configuration
import requests
import data


def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=data.create_order_body,  # тут тело
                         headers=data.create_order_header)  # а здесь заголовки


response = create_new_order();
print(response.status_code)


def request_order_by_track_number(track_id):
    # подставляем полный url
    return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER_BY_TRACK_NUMBER_PATH + str(track_id))


response = request_order_by_track_number(track_id=data.track_id);
print(response.status_code)