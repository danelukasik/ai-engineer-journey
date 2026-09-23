from weather_check import get_weather

def test_get_weather_returns_dict():
    result = get_weather("Denver", 39.7392, -104.9903)
    assert result is not None
    assert "temp_f" in result
    assert result["city"] == "Denver"

def test_get_weather_has_reasonable_temp():
    result = get_weather("Denver", 39.7392, -104.9903)
    assert -30 < result["temp_f"] < 130