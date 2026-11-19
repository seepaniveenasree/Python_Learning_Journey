books_all = []

def insert_book(name, author, price, year, genre):
    book = (name, author, price, year, genre)
    books_all.append(book)
    print("Book added successfully")


def get_all_books():
    return books_all


def search_book(name):
    for book in books_all:
        if name.lower() == book[0].lower():
            return book
    return None


def delete_book(name):
    for book in books_all:
        if name.lower() == book[0].lower():
            books_all.remove(book)
            print("Book removed successfully")
            return
    print("Book not found")


def update_price(name, new_price):
    for i in range(len(books_all)):
        book = books_all[i]

        if name.lower() == book[0].lower():
            lis_book = list(book)
            lis_book[2] = new_price
            books_all[i] = tuple(lis_book)
            print("Book price updated successfully")
            return

    print("Book not found")
