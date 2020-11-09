##versions
python3.6

##create virtualenv
python3.6 -m venv venv

activate venv 
source venv/bin/activate

##install packages
pip install -r requirements.txt

##create dabatase in msql
i.e. infoware

##set proper credentials like password and user.

##export env variables in terminal
export the values of .env

## run commands
python manage.py makemigartions
python manage.py migrate
python manage.py runserver
##create a super user
python manage.py createsuperuser

##can proceed with url shown in terminal
i.e
for register
http://127.0.0.1:8000/api/users
for login 
http://127.0.0.1:8000/api/auth/login
for logout
http://127.0.0.1:8000/api/auth/logout

for userlist view(admin purpose)
http://127.0.0.1:8000/api/users
here we can update and delete users data 
