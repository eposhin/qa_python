import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def new_book(collector):
    collector.add_new_book('Фунтик')
    collector.set_book_genre('Фунтик', 'Мультфильмы')
    return collector