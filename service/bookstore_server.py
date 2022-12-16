from concurrent import futures
import logging

import grpc
from bookstore_pb2 import Book, CreateBookResponse
import bookstore_pb2_grpc
# Books are harcordwed as a list of books and imported from db.py file
from db import Books


class InventoryService(bookstore_pb2_grpc.InventoryServiceServicer):
    def GetBook(self, request, context):
        # ISBN missing
        if not request.ISBN:
            context.abort(grpc.StatusCode.FAILED_PRECONDITION, "Please input an ISBN")
        # find a book with matching ISBN
        for book in Books:
            if book.ISBN == request.ISBN:
                return book
        # ISBN not found
        context.abort(grpc.StatusCode.NOT_FOUND, "Such ISBN is not found")

    def CreateBook(self, request, context):
        ISBN = request.ISBN
        title = request.title
        author = request.author
        genre = request.genre
        publish_year = request.publish_year
        check_genre = genre in range(3) or genre
        # all attributes are required for creating a book
        if ISBN and title and author and publish_year and check_genre:
            book_new = Book(
                ISBN=ISBN,
                title=title,
                author=author,
                genre=genre,
                publish_year=publish_year,
            )
            Books.append(book_new)
            return CreateBookResponse(message="Success", ISBN=ISBN)
        else:
            return CreateBookResponse(
                message="Fail, please input ISBN, title, author, genre, and publish_year to register a book",
                ISBN="",
            )


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bookstore_pb2_grpc.add_InventoryServiceServicer_to_server(
        InventoryService(), server
    )
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
