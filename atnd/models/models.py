from atnd import db

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    title = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(id=self.id, title=self.title)

    def init():
        db.create_all()
