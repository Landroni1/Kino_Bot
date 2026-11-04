import pytest

from utils.text_utils import clean_rating, clean_text


@pytest.mark.parametrize(
    "input_text,expected_len",
    [
        ("Привет, мир!", 12),
        ("А" * 700, 600),
    ],
)
def test_clean_text(input_text, expected_len):
    """Тестирование функции обрезки текста."""
    result = clean_text(input_text)
    assert len(result) == expected_len
    if len(input_text) <= 600:
        assert result == input_text


@pytest.mark.parametrize(
    "raw_rating,expected",
    [
        (7.856, 7.9),
        (8.0, 8.0),
        (8, 8.0),
        (None, "Нет"),
        ("", "Нет"),
        ("N/A", "N/A"),
    ],
)
def test_clean_rating(raw_rating, expected):
    """Тестирование очистки и форматирования рейтинга."""
    assert clean_rating(raw_rating) == expected
