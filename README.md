# Merit Market

Merit market is an application developed to give co-workers recognition for
their actions. It uses the merit money idea from Mangement 3.0 with the
currency in the for of 'hearts'.


## Installation

To install, firstly you need to clone this repository:

    $ git clone https://github.com/intip/merit-market.git

Then install all python dependencies (virtual env is highly advised):

    $ cd merit-market
    $ pip install -r requirements.txt

Edit the settings.py file inside market with your installation settings and
run migrate:

    $ python manage.py migrate

Run the project:

    $ python manage.py runserver

To reset the amount of hearts each person has run (you can use in a cron):

    $ python manage.py weekly_hearts


## TODO

- Tests
- Product shop
- Dashboard and sidebar events.
- Migrate to django-cron?
- Transaction audit
- E-mail with 'hearts received' notification
- Translation


## License

All files are under the MIT License, as stated in LICENSE.
