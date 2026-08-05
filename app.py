import streamlit as st

# Setup browser page configuration
st.set_page_config(page_title="Library Management System", page_icon="📚", layout="centered")
st.title("📚 Digital Library Management System")

# Initialize library in session state so data persists between button clicks
if "library" not in st.session_state:
    st.session_state.library = [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"id": 3, "title": "1984", "author": "George Orwell"},
        {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
        {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger"}
    ]

# --- Sidebar Actions ---
st.sidebar.header("⚙️ Library Actions")
action = st.sidebar.selectbox("Choose Action", ["View Catalog", "Add Book", "Issue Book", "Return Book", "Search Book"])

# --- Action Implementations ---
if action == "View Catalog":
    st.subheader("📊 Current Books Catalog")
    if not st.session_state.library:
        st.warning("No books left in the library.")
    else:
        # Displays your dict cleanly inside an interactive data table widget
        st.dataframe(st.session_state.library, use_container_width=True, hide_index=True)

elif action == "Add Book":
    st.subheader("➕ Add a New Book")
    new_id = st.number_input("Book ID", min_value=1, step=1)
    new_title = st.text_input("Title")
    new_author = st.text_input("Author")
    
    if st.button("Add to Catalog", type="primary"):
        if new_title and new_author:
            # Check for duplicate ID
            if any(b["id"] == new_id for b in st.session_state.library):
                st.error(f"A book with ID {new_id} already exists!")
            else:
                st.session_state.library.append({"id": new_id, "title": new_title, "author": new_author})
                st.success(f"🎉 '{new_title}' added successfully!")
        else:
            st.error("Please fill out both Title and Author fields.")

elif action == "Issue Book":
    st.subheader("🟢 Issue (Remove) a Book")
    issue_id = st.number_input("Enter Book ID to Issue", min_value=1, step=1)
    
    if st.button("Issue Book", type="primary"):
        found = False
        for book in st.session_state.library:
            if book["id"] == issue_id:
                st.session_state.library.remove(book)
                st.success(f"✅ Book with ID {issue_id} has been successfully issued!")
                found = True
                break
        if not found:
            st.error(f"❌ Book with ID {issue_id} not found in catalog.")

elif action == "Return Book":
    st.subheader("↩️ Return a Book")
    ret_id = st.number_input("Book ID", min_value=1, step=1)
    ret_title = st.text_input("Title")
    ret_author = st.text_input("Author")
    
    if st.button("Return Book", type="primary"):
        if ret_title and ret_author:
            st.session_state.library.append({"id": ret_id, "title": ret_title, "author": ret_author})
            st.success(f"✅ '{ret_title}' returned to catalog!")
        else:
            st.error("Please fill out all fields.")

elif action == "Search Book":
    st.subheader("🔍 Search for a Book")
    search_id = st.number_input("Enter Book ID", min_value=1, step=1)
    
    if st.button("Search", type="primary"):
        book = next((b for b in st.session_state.library if b["id"] == search_id), None)
        if book:
            st.info(f"📖 **Found:** ID {book['id']} | **Title:** {book['title']} | **Author:** {book['author']}")
        else:
            st.error(f"❌ No book found with ID {search_id}.")
