# Merit Market

Merit market is an application developed to give co-workers recognition for
their actions. It uses the merit money idea from Mangement 3.0.


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


## TODO
- Tests
- Update this README
- Product shop
- Dashboard and sidebar events.


## License

All files are under the MIT License, as stated in LICENSE.
