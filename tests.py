import pytest

from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_two_books(self, collector):
        collector.add_new_book('Атака титанов')
        collector.add_new_book('Фунтик')
        assert len(collector.get_books_genre()) == 2

    def test_add_empty_title_not_added(self, collector):
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    def test_new_book_has_empty_genre(self, collector):
        collector.add_new_book('Лукоморье')
        assert collector.get_book_genre('Лукоморье') == ''

    def test_set_book_genre_choose_genre_from_list(self,collector):
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        assert collector.get_books_genre() == {'Властелин колец': 'Фантастика'}

    def test_get_genre_for_existing_book(self, collector):
        collector.add_new_book('Фунтик')
        collector.set_book_genre('Фунтик', 'Мультфильмы')
        assert collector.get_book_genre('Фунтик') == 'Мультфильмы'

    def test_get_books_with_specific_genre(self,collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert('Гарри Поттер', collector.get_books_with_specific_genre("Фантастика"))

    def test_cannot_set_invalid_genre(self, collector):
        collector.add_new_book('Лукоморье')
        collector.set_book_genre('Лукоморье', 'Несуществующий жанр')
        assert collector.get_book_genre('Лукоморье') == ''

    @pytest.mark.parametrize('book,genre', [
        ('Книга 1', 'Фантастика'),
        ('Книга 2', 'Детективы'),
        ('Книга 3', 'Мультфильмы')
    ])
    def test_get_books_by_genre(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert book in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize('book,genre', [
        ('Книга1', 'Мультфильмы'),
        ('Книга2', 'Комедии')
    ])
    def test_get_books_for_children_not_from_age_rating_get_list(self, book, genre, collector):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == [book]

    @pytest.mark.parametrize('book,genre', [
        ('Книга1', 'Ужасы'),
        ('Книга2', 'Детективы')
    ])
    def test_get_books_for_children_from_age_rating_get_empty_list(self, book, genre, collector):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == []

    def test_add_to_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_not_from_book_genre(self, collector):
        collector.add_new_book('Фунтик')
        collector.set_book_genre('Фунтик', 'Мультфильмы')
        collector.add_book_in_favorites('Лукоморье')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_add_book_again(self,collector):
        collector.add_new_book('Фунтик')
        collector.set_book_genre('Фунтик', 'Мультфильмы')
        collector.add_book_in_favorites('Фунтик')
        collector.add_book_in_favorites('Фунтик')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_real_book(self, collector):
        collector.add_new_book('Фунтик')
        collector.add_book_in_favorites('Фунтик')
        collector.delete_book_from_favorites('Фунтик')
        assert len(collector.get_list_of_favorites_books()) == 0