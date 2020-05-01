# services/users/manage.py
import os
import sys

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.users.models import User

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('create')
def create_db():

    engine = create_engine(os.environ.get('DATABASE_URL'))
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))

    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed')
def seed_db():
    """Seeds the database."""
    db.session.add(User(
        username='tonystark',
        email='avengers@gmail.com',
        password='supersecret'
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()
