from flask import Flask, request, jsonify
from models import db, Flashcard
from subject_infer import infer_subject
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/flashcard', methods=['POST'])
def add_flashcard():
    data = request.get_json()
    question = data['question']
    subject = infer_subject(question + " " + data['answer'])
    flashcard = Flashcard(
        student_id=data['student_id'],
        question=question,
        answer=data['answer'],
        subject=subject
    )
    db.session.add(flashcard)
    db.session.commit()
    return jsonify({"message": "Flashcard added successfully", "subject": subject})

@app.route('/get-subject', methods=['GET'])
def get_flashcards():
    student_id = request.args.get('student_id')
    limit = int(request.args.get('limit', 5))

    flashcards = Flashcard.query.filter_by(student_id=student_id).all()

    subject_map = {}
    for fc in flashcards:
        subject_map.setdefault(fc.subject, []).append(fc)

    selected = []
    for cards in subject_map.values():
        if cards:
            selected.append(random.choice(cards))
            if len(selected) >= limit:
                break

    random.shuffle(selected)

    return jsonify([{
        "question": fc.question,
        "answer": fc.answer,
        "subject": fc.subject
    } for fc in selected[:limit]])

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)

