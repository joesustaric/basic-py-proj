from datetime import datetime

import src.aggregate_time_series as agg_data

def test_given_one_data_point_it_buckets_correctly_60_sec():
    point = datetime(2025,6,3,14,30,10)
    data = [(point.timestamp(), 50)]

    expected = [(1748925000.0, 50.0)]
    result = agg_data.aggregate_time_series(data, 60)

    assert result == expected

def test_given_several_values_it_buckets_correctly_60_sec():
    data = [
    (1000, 10),   # timestamp=1000, value=10
    (1005, 20),   # timestamp=1005, value=20
    (1010, 30),   # timestamp=1010, value=30
    (1065, 40),   # timestamp=1065, value=40
    (1070, 50),   # timestamp=1070, value=50
    (1130, 60),   # timestamp=1130, value=60
]
    expected = [(960, 20.0), (1020, 45.0), (1080, 60.0)]

    result = agg_data.aggregate_time_series(data, 60)

    assert result == expected
