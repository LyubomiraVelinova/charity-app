# Charity_app

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
A charity app that contains information about the organization "Caps for Future" and "Club for Future". The user can log in as a member, volunteer or sponsor. Volunteers can participate in campaigns and track the history of their participation, members can write articles about an organization, sponsors can donate to certain campaigns. There is also a donation feature for unauthorized users. Any user - whether unauthorized or authorized - can contact the organization through the contact form.

## Technologies
Project is created with:
* Django(4.2.4)
* HTML, CSS
* JavaScript
* Bootstrap
* PostgreSQL
* Unit and Integration Testing

## Setup
* Clone the repository - HTTPS or SSH:
git clone https://github.com/LyubomiraVelinova/Charity_app.git
git clone git@github.com:LyubomiraVelinova/Charity_app.git

* Install project dependencies:
pip install -r requirements.txt

* Set up environment variables

* Apply database migrations:
python manage.py makemigrations
python manage.py migrate

* Run the development server:
python manage.py runserver


* Followed the MVT (Model-View-Template) pattern to ensure a well-structured application.
* Crafted 8 apps, comprising over 30 pages with both function and class-based views for a seamless user experience.
* Utilized more than 10 models to efficiently manage and organize data.
* Designed the frontend with Bootstrap, providing an intuitive and responsive user interface.
* Implemented role-based access control to safeguard sensitive information and features.
* Prioritized security measures, including data validation and the production of high-quality, maintainable code.
* Employed PostgreSQL as the relational database system, ensuring robust data management and retrieval.
