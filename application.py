from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Book {self.id}>"

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully', 'book_id': new_book.id}), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify({'books': [{'id': book.id, 'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher} for book in books]}), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        data = request.get_json()
        book.book_name = data.get('book_name', book.book_name)
        book.author = data.get('author', book.author)
        book.publisher = data.get('publisher', book.publisher)
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'}), 200
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 200
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
