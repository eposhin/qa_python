Список проверок
1. test_add_new_book_two_books - Добавление двух разных книг
2. test_add_empty_title_not_added - Нельзя добавить книгу с пустым названием
3. test_add_duplicate_book_fails - Нельзя добавить книгу с одинаковым названием дважды
4. test_new_book_has_empty_genre - Новая книга создается без жанра
5. test_set_genre_for_existing_book - Получение жанра существующей книги
6. test_cannot_set_invalid_genre	- Нельзя установить недопустимый жанр
7. test_get_books_by_genre - Фильтрация книг по жанру (параметризованный)
~~8. test_get_book_genre_name - Корректность получения жанра книги~~
9. test_add_to_favorites_only_once - Книга добавляется в избранное только один раз
10. test_remove_from_favorites - Удаление книги из избранного
11. test_add_book_in_favorites_existing_book - Добавление существующей книги в избранное
12. test_add_book_in_favorites_add_book_again - Повторное добавления в избранное
13. test_delete_book_from_favorites_real_book - Удаление реальной книги из избранного
14. test_delete_book_from_favorites_unreal_book -  Удаление несуществующей книги
15. test_get_list_of_favorites_books_empty_list - Проверка пустого списка избранного

Исправления:
1. Убрал фикстуру new_book
2. Добавил test_get_list_of_favorites_books - получение списка избранных книг
3. Добавил def test_get_books_genre - получение жанра по книге
4. Убрал проверку 8