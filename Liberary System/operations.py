books = {
    "9780140449136": {"title": "Database System", "author": "Mr Sheikh Umar", "genre": "Fiction", "copies": 3}
}

members = [
    {"member_id": 1, "name": "Shadrach", "email": "shadrach@gmail.com", "borrowed_books": []}
]

genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery")

def add_book(isbn, title, author, genre, copies):
    if isbn in books:
        return "Book already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "copies": copies
    }
    return "Book added successfully."


def add_member(member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return "Member already exists."
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return "Member added successfully."


def search_books(keyword):
    results = []
    for isbn, details in books.items():
        if keyword.lower() in details["title"].lower() or keyword.lower() in details["author"].lower():
            results.append((isbn, details))
    return results


def update_book(isbn, title=None, author=None, genre=None, copies=None):
    if isbn not in books:
        return "Book not found."
    if genre and genre not in genres:
        return "Invalid genre."
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if copies is not None:
        books[isbn]["copies"] = copies
    return "Book updated successfully."


def update_member(member_id, name=None, email=None):
    for m in members:
        if m["member_id"] == member_id:
            if name:
                m["name"] = name
            if email:
                m["email"] = email
            return "Member updated successfully."
    return "Member not found."


def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    # Ensure book not currently borrowed
    for m in members:
        if isbn in m["borrowed_books"]:
            return "Cannot delete book. It is currently borrowed."
    del books[isbn]
    return "Book deleted successfully."


def delete_member(member_id):
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) > 0:
                return "Cannot delete member. They have borrowed books."
            members.remove(m)
            return "Member deleted successfully."
    return "Member not found."


def borrow_book(member_id, isbn):
    # Find member
    member = None
    for m in members:
        if m["member_id"] == member_id:
            member = m
            break
    if not member:
        return "Member not found."
    if isbn not in books:
        return "Book not found."
    if books[isbn]["copies"] <= 0:
        return "No copies available."
    if len(member["borrowed_books"]) >= 3:
        return "Borrow limit reached."
    member["borrowed_books"].append(isbn)
    books[isbn]["copies"] -= 1
    return "Book borrowed successfully."


def return_book(member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if isbn in m["borrowed_books"]:
                m["borrowed_books"].remove(isbn)
                books[isbn]["copies"] += 1
                return "Book returned successfully."
            return "Book not borrowed by this member."
    return "Member not found."
