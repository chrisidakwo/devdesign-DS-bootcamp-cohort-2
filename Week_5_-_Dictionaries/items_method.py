library = {
    "The Hobbit": {
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "genre": "Fantasy",
        "read": True,
    },
    "Dune": {
        "author": "Frank Herbert",
        "year": 1965,
        "genre": "Fiction",
        "read": False,
    },
}
print(library.items())
for (bookTitle, bookDetails) in library.items():
    print("Book Title:", bookTitle)
    print("Book Details:", bookDetails)
    print("")