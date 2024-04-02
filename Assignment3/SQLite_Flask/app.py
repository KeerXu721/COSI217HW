# import os
# from flask import Flask, render_template, request, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
#
# from sqlalchemy.sql import func
# from sqlalchemy import delete, insert, update
#
# basedir = os.path.abspath(os.path.dirname(__file__))
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = \
#     'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
#
# class Entity(db.Model):
#     entity = db.Column(db.String(100), nullable=False)
#     relation = db.Column(db.String(100), nullable=False)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc3bb2a43ff1103895a4ee315ee27740'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity1_id = db.Column(db.Integer, db.ForeignKey('entity.id'))
    entity2_id = db.Column(db.Integer, db.ForeignKey('entity.id'))

    entity1 = db.relationship('Entity', foreign_keys=[entity1_id])
    entity2 = db.relationship('Entity', foreign_keys=[entity2_id])



@app.get('/')
def index():
    users = Entity.query.all()
    return f'{users}\n'


@app.get('/<string:entity>')
def get_entity(entity):
    entity = Entity.query.filter_by(entity=entity).first()
    return f'{entity}\n'


@app.post('/<string:entity>/<string:relation>')
def add_entity(entity, relation):
    entity = Entity(entity=entity, relation=relation)
    db.session.add(entity)
    db.session.commit()
    return f'{entity}\n'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
