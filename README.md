#Sellerapp(User-Auction)

This project is a Django-based auction application.

## Features

- Auction Management
  - Create, Read, Update, and Delete auctions (admin only)
  - Users can view ongoing auctions
  - Bidding on auctions (authenticated users)

- User Management
  - User login (token-based)
  - Basic CRUD operations for users 

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run migrations: `python manage.py migrate`.
5. Start the server: `python manage.py runserver`.

## Usage

- To create an auction, make a POST request to `/api/auctions/create/`.
- To view ongoing auctions, make a GET request to `/api/auctions/auctions/`.
- To bid on an auction, make a POST request to `/api/auctions/place_bid/<auction_id>/`.
- To create a user,make a POST request to '/api/users/register/'.
- To login a user,make a POST request to '/api/users/login/'.
- To update a user details, make a PUT request to `/api/users/<id>/`.
-To update an auction details, make a PUT request to `/api/auctions/<auction_id>/`.
-And other read and delete operations ,make a DELETE request for user and auction.

