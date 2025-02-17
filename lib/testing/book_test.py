from lib.book import Book

def test_book_initialization():
    """Test that a Book instance is initialized correctly"""
    book = Book("1984", "George Orwell", 328)
    assert book.title == "1984"
    assert book.author == "George Orwell"
    assert book.page_count == 328

def test_page_count_validation():
    """Test that page_count must be an integer"""
    book = Book("1984", "George Orwell", 328)
    book.page_count = "not an integer"  # This should print an error message
    assert book.page_count == 328  # Value should not change

def test_turn_page():
    """Test the turn_page method"""
    book = Book("1984", "George Orwell", 328)
    # Capture the printed output (optional, requires pytest's capsys fixture)
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    book.turn_page()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Flipping the page...wow, you read fast!"