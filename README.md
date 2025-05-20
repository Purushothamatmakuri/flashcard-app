# Smart Flashcard Backend

This is a Flask backend for a smart flashcard system that automatically detects the subject of each flashcard.

## 📦 Requirements
- Python 3.x
- Flask
- Flask_SQLAlchemy

## 🚀 Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

## 🔧 Endpoints

### Add Flashcard
`POST /flashcard`

**Body:**
```json
{
  "student_id": "stu001",
  "question": "What is Newton's Second Law?",
  "answer": "Force equals mass times acceleration"
}
```

### Get Flashcards by Subject
`GET /get-subject?student_id=stu001&limit=5`
