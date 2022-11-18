# StripePayConnect
### Connection of the Stripe payment system

#### Deployed on Heroku:
https://stripe-pay-connect.herokuapp.com/

Backend implemented in Django.

The functionality of the site:
- choose product;
- click 'Buy' button;
- wait for Stripe payment form;
- enter test card number 4242 4242 4242 4242, validity - 01/30, CVC - 123;
- wait for the payment to be completed.
- data for access to admin panel:
  - login: admin
  - password: admin777

## Web application at work:

### Payment process
![payment_process](https://github.com/slychagin/StripePayConnect/blob/master/demogifs/Buy.gif)

### Django Administration Panel
![admin_panel](https://github.com/slychagin/StripePayConnect/blob/master/demogifs/Admin%20panel.gif)


### Technologies:
- Python 3;
- Django Framework;
- HTML, CSS, Bootstrap.

### You can run this project locally just do:
- in command line `git clone https://github.com/slychagin/StripePayConnect.git`;
- install all requirements from requirements.txt;
- `python manage.py runserver`;
- or test on https://stripe-pay-connect.herokuapp.com/
