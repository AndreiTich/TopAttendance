## Bootstrapping the project
1. Install python 3 (on Mac: `brew install python3`)
1. Clone this repo: `git clone git@github.com:AndreiTich/TopAttendance.git`.
1. `cd` into the repo directory.
1. Create a virtual environment for your python dependencies: `python3 -m venv .virtualenv`
1. Activate the virtual environment (on Mac/Linux: `source .virtualenv/bin/activate`; on Windows: `./.virtualenv/Scripts/activate.bat`)
1. Install the python requirements via `pip3 install -r requirements.txt`

## Learning resources
### Python / Django
* [Python 3 reference](https://docs.python.org/3/reference/)
* [Django tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
* [An unofficial Django tutorial](https://tutorial.djangogirls.org/en/index.html) which may be helpful as well
* [Django reference material](https://docs.djangoproject.com/en/1.10/) (Really good documentation if you dig into it!)
* [A collection of Django resources](https://www.fullstackpython.com/django.html)

### React
* [How to use state in React](https://facebook.github.io/react/docs/state-and-lifecycle.html)
* [How to make new components in React](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md#importing-a-component)
* [React router](https://github.com/ReactTraining/react-router/blob/master/packages/react-router-dom/docs/guides/quick-start.md)

## Ideas
Misc. ideas that have been brought up.

* Correlate geoip (Django has a great geoip/GIS feature) with the user-reported GPS lat/long to double check that they agree, to make sure they're not cheating the GPS location.
* Add attendance "sessions": allow the prof to start/stop the attendance window.
* iBeacon transmission from prof to student devices
* Something with having the students taking a photo of themselves so that the prof can go check if a student looks like they're in-class, if they have some reason to be suspicious
* Consider other sensor data that might be interesting from mobile devices

Feel free to experiment!
