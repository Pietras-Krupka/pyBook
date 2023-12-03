Feature: Book managment
 Scenario: Getting information about a book
Given: I have a book titled "Wiedźmin" by "Sapkowski" published in 2000
When: I get the book information
Then:The information should by "Książka: Wiedźmin Autor: Sapkowski Rok: 2000"
