def is_palindrome(text):
    """Проверяет, является ли строка палиндромом (игнорирует регистр и пробелы)."""
    clean_text = ''.join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]
