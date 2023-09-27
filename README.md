# Back-end Developer Capstone Project

Each of the following endpoints uses Token authentication.

## Get A New Token

- Step 1: create a superuser in the terminal:  `python manage.py createsuperuser`

- Step 2:  Get a token with a username and password at this endpoint: `http://127.0.0.1:8000/auth`


## Booking  
`http://127.0.0.1:8000/restaurant/booking/tables/`

## Single Booking
 `http://127.0.0.1:8000/restaurant/booking/tables/<int:id>`

## Menu
  `http://127.0.0.1:8000/restaurant`

## Single Menu
  `http://127.0.0.1:8000/restaurant/<int:id>`

## Djoser auth
  `http://127.0.0.1:8000/auth`

## Token (Insomnia)
 `http://127.0.0.1:8000/restaurant/api-token-auth/`
