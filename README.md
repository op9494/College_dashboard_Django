# COLLEGE DASHBOARD USING DJANGO
This is na web application used to deliver the online dashborad for the **student to have the official news from the college** in internet without going ofline.

## INSTALLATION
1. Install [django](https://www.djangoproject.com/download/) and then install 'pip'
2. Use the below code to install the needed packages used in the application
```
appdirs          1.4.4
distlib          0.3.1
Django           3.2
pip              21.1.1
plotly           4.14.3
python-dotenv    0.15.0
pytz             2021.1
retrying         1.3.3
setuptools       54.2.0
sqlparse         0.4.1
virtualenv       20.4.3
```
### To install
> $ pip install
> $ pip update

3.To create the model in django
> python manage.py makemigrations
> python manage.py migrate

4.How to run the application. from the current directory run the code from bash
> python manage.py runserver

To visit [Admin and staff login](http://127.0.0.1:8000/admin)
To look the [dashboard](http://127.0.0.1:8000/) 

## Models 
- Admin
- Staffs
- Student 

### Admin
- Admin can add/delete/disable user,group policy.
- Admin can change the content of all database field,add,edit and delete.

### Staffs
- Staffs of individual department is given by login id and password witha help of admin.
- Staffs have the definite group policy to view and edit the data.

### Students/Public
- Users can see the online dashboard by visiting the link given and can know the official information given in an form of scrollable notification wich can be downloaded.
- Topper informatin of past academinyear / Exams conducted by the college.
- Status of the colege strength of definite department and overall information in an form of virtulization.
