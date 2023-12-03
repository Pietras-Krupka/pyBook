from behave import  given, when, then
from book import Book

@given('I have a book tittled "{tittle}" by "{author}" published om {year:d}')
def steps_impl(context, title, author, year):
    context.book = Book(title, author, year)
@when('I get the book information')
def steps_impl(context):
    context.info = context.book.get_info()
@then('The information should by "{info}"')
def steps_impl(context, info)
    assert context.info == info
    

