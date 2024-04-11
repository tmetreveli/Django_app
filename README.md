# Book store

This Django application provides a platform to list, retrieve, and display books.

## Installation

To set up this project locally, follow the instructions below:

1. Clone the repository:
`
git clone https://github.com/tmetreveli/Django_app/
`
2. Install the required dependencies:
`
pip install -r requirements.txt
`

3. Apply the migrations:
   `
   python manage.py migrate
   `
4. Run the development server:

` python manage.py runserver
`


## Usage

Once the server is running, you can access the following endpoints:

- List all books: `GET /books/`
- Book detail: `GET /books/<product_id>/`
- Paginated books display: Navigate to the root URL to view books in a paginated format.




