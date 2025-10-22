from operations import *

# Reset data structures before testing
books.clear()
members.clear()

print("=== RUNNING TESTS ===")

# TEST 1
result = add_book("111", "Database System", "Mr Sheikh Umar", "Fiction", 3)
assert result == "Book added successfully.", "Test 1 Failed: Could not add book."
print("Test 1 Passed: Book added successfully.")

# TEST 2
result = add_member(1, "Shadrach", "shadrach@gmail.com")
assert result == "Member added successfully.", "Test 2 Failed: Could not add member."
print("Test 2 Passed: Member added successfully.")

# TEST 3
result = borrow_book(1, "111")
assert result == "Book borrowed successfully.", "Test 3 Failed: Borrowing failed."
print("Test 3 Passed: Book borrowed successfully.")

# TEST 4
# Reduce book copies to zero
books["111"]["copies"] = 0
result = borrow_book(1, "111")
assert result == "No copies available.", "Test 4 Failed: Should not borrow when no copies left."
print("Test 4 Passed: Borrow blocked when no copies left.")

# TEST 5
# Reset book copies and borrowed_books
books["111"]["copies"] = 2
members[0]["borrowed_books"].append("111")
result = return_book(1, "111")
assert result == "Book returned successfully.", "Test 5 Failed: Could not return book."
print("Test 5 Passed: Book returned successfully.")

# TEST 6
members[0]["borrowed_books"] = ["111"]
result = delete_member(1)
assert result == "Cannot delete member. They have borrowed books.", "Test 6 Failed: Member deletion should be blocked."
print("Test 6 Passed: Member deletion blocked when books borrowed.")

# TEST 7: Delete book currently borrowed
books["111"]["copies"] = 1
result = delete_book("111")
assert result == "Cannot delete book. It is currently borrowed.", "Test 7 Failed: Book deletion should be blocked."
print("Test 7 Passed: Book deletion blocked when borrowed.")

print("\nAll tests passed successfully! ")
