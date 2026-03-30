def clean_text(text):
    return text[:600]

def clean_rating(rating):
    if isinstance(rating, (int, float)):
        return float(round(rating, 1))
    return str(rating) if rating else "Нет"

