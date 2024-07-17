# Warm

## Project Video Link : http://youtu.be/cpPmBlvtdrs

## Requirement

[get-pip.zip](http://github.com/7Har/Warm/files/6250009/get-pip.zip)

    pip install --upgrade pip

    pip install django

    pip install psycopg2

    pip install pycryptodome

    pip install django-admin-rangefilter

    python -m pip install Pillow

    pip install django-tenants

    pip install bootstrap4

    pip install djangorestframework

    pip install channels

    `<!-- pip install daphne -->`
    pip install gunicorn

## To run the server, run the following command:

    python manage.py makemigrations client
    python manage.py makemigrations
    python manage.py migrate_schemas

    python manage.py migrate client
    python manage.py makemigrations yolo5test

    <!-- python manage.py migrate
    python manage.py migrate_schemas --shared -->

    python manage.py createsuperuser
    python manage.py create_tenant
    python manage.py create_tenant_superuser

    python manage.py collectstatic

    daphne -u /tmp/daphne1.sock -b 0.0.0.0 -p 8003 Warm.asgi:application

    python manage.py runserver

docker system prune -a
docker image prune
docker volume prune

docker-compose logs -f

cli/powershell  ->    docker run -it --rm -v C:\Users\Notebook\Neo\ws-server:/ws-server neo-ws /bin/bash

# Κατεβάστε τα TensorFlow models

git clone http://github.com/tensorflow/models.git

# Εγκαταστήστε το object_detection

cd models/research
protoc object_detection/protos/*.proto --python_out=.
cp object_detection/packages/tf2/setup.py .
python -m pip install .

pyside6-uic interface.ui -o output.py


pyside6-designer


python -m venv myenv
pip cache purge
myenv\Scripts\activate
pip install --no-cache-dir -r requirements.txt
pip install -r requirements.txt




myenv\Scripts\activate