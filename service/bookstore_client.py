import logging

import grpc
import bookstore_pb2
import bookstore_pb2_grpc


def print_getbook_message(response):
    print(
        "Bookstore client received a GetBook info: "
        + "ISBN: {}, title: {}, author: {}, genre: {}, publish_year: {}".format(
            response.ISBN,
            response.title,
            response.author,
            response.genre,
            response.publish_year,
        )
    )


def print_createbook_message(response):
    print(
        "Bookstore client received a CreateBook info: "
        + "message: {}, ISBN: {}".format(response.message, response.ISBN)
    )


def test_case_1(stub):
    response = stub.CreateBook(
        bookstore_pb2.CreateBookRequest(
            ISBN = "4",
            title="17645_a4",
            author="Mat4",
            genre=bookstore_pb2.Genre.FANTACY,
            publish_year=2023,
        )
    )
    print_createbook_message(response)


def test_case_2(stub):
    response = stub.GetBook(bookstore_pb2.GetBookRequest(ISBN="4"))
    print_getbook_message(response)


def run():
    print("Will try to access InventoryService ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = bookstore_pb2_grpc.InventoryServiceStub(channel)
        test_case_1(stub)
        test_case_2(stub)


if __name__ == "__main__":
    logging.basicConfig()
    run()
