"""Simple Web interface to spaCy entity recognition

To see the pages point your browser at http://127.0.0.1:5000.

"""

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

import spaCy_model

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc3bb2a43ff1103895a4ee315ee27740'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_flask.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine('sqlite:///app_flask.sqlite')

db = SQLAlchemy(app)


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String)
    entity_count = db.Column(db.Integer)
    relation = db.relationship('Relationship', backref='author', lazy=True)

    def __repr__(self):
        return f"Entity: {self.entity}"


class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    head = db.Column(db.String)
    relationship = db.Column(db.String(100), nullable=False)
    relation_count = db.Column(db.Integer)
    head_entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=False)

    def __repr__(self):
        return f"{self.relationship} {self.relation_count}"


@app.post('/<string:entity>')
def add_entity(entity, entity_count):
    entity = Entity(entity=entity, entity_count=entity_count)
    db.session.add(entity)
    db.session.commit()
    return f'{entity}\n'


@app.post('/<string:entity1>/<string:relation>/<string:entity2>')
def add_relation(relation, head_entity, count, head_entity_id):
    relation = Relationship(relationship=relation, head=head_entity, relation_count=count, head_entity_id=head_entity_id)
    db.session.add(relation)
    db.session.commit()
    return f'{relation}\n'


# For the website we use the regular Flask functionality and serve up HTML pages.
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', input=open('sample_text.txt', encoding="utf-8").read())
    else:
        text = request.form['text']
        ner = spaCy_model.NerClass(text)
        markup = ner.get_entities_with_markup()
        markup_paragraphed = ''
        for line in markup.split('\n'):
            if line.strip() == '':
                markup_paragraphed += '<p/>\n'
            else:
                markup_paragraphed += line
        return render_template('result.html', markup=markup_paragraphed)


@app.get('/get')
def index_get():
    return render_template('index.html', input=open('sample_text.txt').read())


@app.route('/stats')
def stats():
    relation_data = Relationship.query.all()
    entity_data = Entity.query.all()
    return render_template('stats.html', entity_data=entity_data)


@app.post('/post')
def index_post():
    text = request.form['text']
    ner_doc = spaCy_model.NerClass(text)
    entities = ner_doc.get_entities()
    entity_markup = ner_doc.get_entities_with_markup()
    dep_doc = spaCy_model.DepClass(text)
    dep_l = dep_doc.process_data()
    dep_graph = dep_doc.dep_graph()
    ner_parse = ''
    dep_parse = ''
    for line in entity_markup.split('\n'):
        if line.strip() == '':
            ner_parse += '<p/>\n'
        else:
            ner_parse += line

    for entity in entities:
        existing_entity = Entity.query.filter_by(entity=entity).first()
        if existing_entity is not None:
            # the entity already exist
            existing_entity.entity_count += 1
            db.session.commit()
        else:   # add new entity
            add_entity(entity=entity, entity_count=1)

    for item in dep_l:
        has_entity = False
        entity = None
        for ent in entities:
            if item[0] in ent:
                has_entity = True
                entity = ent
        if has_entity:
            entity = Entity.query.filter_by(entity=entity).first()  # find the existing entity
            existing_relationship = Relationship.query.filter_by(
                relationship=f'{item[2]} {item[1]} {item[0]}').first()
            if existing_relationship is not None:
                # dependency already exist, just update the count
                existing_relationship.relation_count += 1
                db.session.commit()

            else:
                # add new dependency
                add_relation(relation=f'{item[2]} {item[1]} {item[0]}', head_entity=item[0], count=1,
                             head_entity_id=entity.id)
            db.session.commit()
        dep_parse += '<p style="text-align: center;">' + item[2] + " " + item[1] + " " + item[0] + '</p>\n'
    return render_template('result2.html', ner=ner_parse, dep=dep_parse, dep_graph=dep_graph)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
