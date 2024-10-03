#!/usr/bin/python3

class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out_book(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._book = []

    def add_book(self,book):
        self._book.append(book)

    def check_out_book(self, title):
        for b in _book:
            if b.title==title and b.is_available:
                b.checkout()
                return True
            return False
    
    def return_book(self, title):
        for b in _book:
            if b.title == title and not b.is_available:
                b.book_return()
                return True
            return False

    def list_available_books(self):
        available_books = [
               book for b in self._book if b.is_available
                ]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No book available")
