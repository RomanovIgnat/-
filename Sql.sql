SELECT book.name
FROM user_book
JOIN book ON user_book.id_book = book.id
JOIN user ON user_book.id_user = user.id
WHERE user.name = 'Bob'
