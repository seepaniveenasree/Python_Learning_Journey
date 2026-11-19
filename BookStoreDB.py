books_all=[] #to store all books details

def insert_book(name,author,price,year,genre):
    book={"Name":name,"Author":author,"Price": price,"Year":year,"Genre":genre}
    books_all.append(book)
    print("Book added successfully")
    
def get_all_books():
    return books_all

def search_book(name):
    for book in books_all:
        if (book["Name"]==name):
            return book
    return None
def delete_book(name):
    for book in books_all:
        if (book["Name"]==name):
            books_all.remove(book)
            print("Book Deleted Successfully")
            return
    else:
        print("Book not found")

def update_price(name,new_price):
    book=search_book(name)
    if book:
        book["Price"]=new_price
        print("Book Price Updated Successfully")
        return
    else:
        print("Book not found")
    