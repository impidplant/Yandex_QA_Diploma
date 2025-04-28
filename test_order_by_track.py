# Анастасия Шостко, 29-ая когорта - Финальный проект. Инженер по тестированию плюс

import new_order
import data

def test_get_order_info_by_track():
    track = new_order.create_order(data.order_body).json()["track"]
    response = new_order.get_order_info_by_track(track)
    assert response.status_code == 200