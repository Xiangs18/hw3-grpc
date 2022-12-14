from bookstore_pb2 import Book, Genre


Books = [
    Book(
        ISBN="1",
        title="17645_a1",
        author="Mat1",
        genre=Genre.FICTION,
        publish_year=2020,
    ),
    Book(
        ISBN="2", title="17645_a2", author="Mat2", genre=Genre.NOVEL, publish_year=2021
    ),
    Book(
        ISBN="3",
        title="17645_a3",
        author="Mat3",
        genre=Genre.FANTACY,
        publish_year=2022,
    ),
]
