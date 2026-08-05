library = []

def addBook(id: int, title: str, author: str):
    book = {"id": id, 
            "title": title, 
            "author": author}
    library.append(book)
    
def issueBook(id: int):
    for book in library:
        if book["id"] == id:
            library.remove(book)
            return f"🟢 Book with ID {id} has been issued."            
    return f"🔴 Book with ID {id} not found."

def returnBook(id: int, title: str, author: str):
    book = {"id": id, 
            "title": title, 
            "author": author}
    library.append(book)
    
def searchBook(id: int):
    for book in library:
        if book["id"] == id:
            return f"📖 Found -> ID: {book['id']} | Title: {book['title']} | Author: {book['author']}"
    return f"🔴 Book with ID {id} not found."

def displayBooks():
    if not library:
        return "No books in the library."
    
    output = []
    output.append("\n📚 CURRENT LIBRARY CATALOG")
    output.append("=" * 65)
    output.append(f"{'ID':<5} | {'TITLE':<25} | {'AUTHOR':<25}")
    output.append("-" * 65)
    
    for book in library:
        output.append(f"{book['id']:<5} | {book['title']:<25} | {book['author']:<25}")
        
    output.append("=" * 65)
    return "\n".join(output)

addBook(1, "The Great Gatsby", "F. Scott Fitzgerald")
addBook(2, "To Kill a Mockingbird", "Harper Lee")
addBook(3, "1984", "George Orwell")
addBook(4, "Pride and Prejudice", "Jane Austen")
addBook(5, "The Catcher in the Rye", "J.D. Salinger")

print(displayBooks())

print(issueBook(3))
print(displayBooks())

returnBook(3, "1984", "George Orwell")
print(displayBooks())
