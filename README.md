# Charity_app

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [License](#license)
* [Screenshots](#screenshots)

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
###### git clone https://github.com/LyubomiraVelinova/Charity_app.git
###### git clone git@github.com:LyubomiraVelinova/Charity_app.git

* Install project dependencies:
pip install -r requirements.txt

* Set up environment variables

* Apply database migrations:
-- python manage.py makemigrations
-- python manage.py migrate

* Run the development server:
python manage.py runserver

## Features
* #### MVT Pattern:
Followed the MVT (Model-View-Template) pattern to ensure a well-structured application, enhancing code organization and maintainability.

* #### Multiple Apps:
Crafted 8 separate applications within the project, totaling over 30 pages, to compartmentalize functionality and improve project scalability.

* #### Data Management:
Utilized over 10 models to efficiently manage and organize data, providing a structured and organized database schema.

* #### Responsive UI: 
Designed the frontend using Bootstrap and personal HTML CSS and JavaScript skillsм ensuring an intuitive and responsive user interface across various devices and screen sizes.

* #### Access Control:
Implemented role-based access control, enhancing security by restricting access to sensitive information and features based on user roles.

* #### Security Focus:
Prioritized security measures, including robust data validation and the production of high-quality, maintainable code to protect against vulnerabilities.

* #### Database Choice:
Employed PostgreSQL as the relational database system, ensuring robust data management and retrieval capabilities, which is particularly valuable for handling structured data effectively.

## License
* MIT License

## Screenshots

