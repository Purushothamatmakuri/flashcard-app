from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flashcard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(100), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    subject = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Flashcard {self.id} - {self.subject}>'
