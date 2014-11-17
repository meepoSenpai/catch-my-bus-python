#catch-my-bus-python

A small GTK3 StatusIcon that displays the next Bus-Arrivals of a given station, which is pre-defined
in the fetch_station.py


###Installation

Clone the Git-Repo to your $HOME directory and rename it to ".catch-my-bus-python". Then simply run
the CatchMy.py script.

You will need to have PyGObject installed, as well as Python 3.x

###Changing the Bus-Stop

In line 16 of CatchMy.py you will have to change the String argument passed to the get_departure_list method
of the fetch_station module.

###Screenshot

Still under construction, but for a first view of what it looks like:

![screenshot](./screenshot.png)

It should be the same thing as [kiliankoe/catchmybus](https://github.com/kiliankoe/catchmybus)


Icon by [Tumsi](http://openclipart.org/detail/182201/bushaltestelle-by-tumsi-182201)