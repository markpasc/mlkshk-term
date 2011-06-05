# mlkshk-term #

`mlkshk-term` is a command line tool for controlling some of your MLKSHK account. It can:

* list your shakes
* upload a file from your computer to a shake


## Installation ##

Install its dependencies from the `requirements.txt` file:

    $ pip install -r requirements.txt

Then you can install it as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies system-wide, try installing it in a [virtual environment](http://www.virtualenv.org/).


## Configuring ##

First, you'll need a MLKSHK API key. Register an application in the developers section of mlkshk.com to get a key. Once you have a key, run the `configure` command:

    $ mlkshk configure
    API key: 68-A
    API secret: f73D85A83def7BC29580FEB9f087A69Bc6bfacd1DDDBEBfb2bAF52c1
    Code: 13b24c7D485A9C4e99F1B4b163ddAE6eE4b9917e
    Configured!

After entering your API secret, the authorization page should open in your web browser. After approving your app, copy the `code` from the URL of the resulting error page and paste it at the `Code:` prompt.


## Usage ##

See `mlkshk --help` for supported commands.

    $ mlkshk shakes
    +-----+--------------+----------+------+---------------------------------+
    |  ID |     Name     |  Owner   | Type |               URL               |
    +-----+--------------+----------+------+---------------------------------+
    | 114 | Mark Paschal | markpasc | user | http://mlkshk.com/user/markpasc |
    +-----+--------------+----------+------+---------------------------------+

    $ mlkshk upload ~/Pictures/funny-picture.jpg

    $
