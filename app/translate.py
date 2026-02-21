from flask_babel import _


def translate(text, source_language, dest_language):
    """
    Mock translation function for development/testing.
    Replace with real Azure/Google Translator when ready.
    """
    # Simple mock: just return the text with a note
    return f"[{dest_language.upper()}] {text}"

