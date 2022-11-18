# stripe-pay
### Connection of the Stripe payment system

#### Deployed on Heroku:
https://

Backend implemented in Django.

The functionality of the site:
- choose product;
- click 'Buy' button;
- wait for Stripe payment form;
- enter test card number 4242 4242 4242 4242, validity - 01/30, CVC - 123;
- wait for the payment to be completed.
- data for access to admin panel:
  login: admin
  password: StripePay

## Web application at work:

### Payment process
![]()

### Django Administration Panel
![]()


### Technologies:
- Python 3;
- Django Framework;
- HTML, CSS, Bootstrap.

### You can run this project locally just do:
- `git clone https://github.com/slychagin/stripe-pay.git`;
- you must have Python 3 installed on your computer;
- install all requirements from requirements.txt;
- `python manage.py runserver`;
- or go to https://

### You can alsow pull Docker images:
- `docker pull serhio777/stripepay_web_run`;
- `docker pull serhio777/stripepay_web_migrate`;
- `docker pull serhio777/stripepay_web`.
