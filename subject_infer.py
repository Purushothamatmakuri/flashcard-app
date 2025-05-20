SUBJECT_KEYWORDS = {
    "Biology": ["photosynthesis", "cell", "organism", "mitosis", "evolution"],
    "Physics": ["newton", "gravity", "velocity", "acceleration", "force"],
    "Chemistry": ["atom", "molecule", "reaction", "acid", "base"],
    "Math": ["algebra", "geometry", "calculus", "equation", "theorem"],
    "History": ["war", "revolution", "empire", "king", "president"],
}

def infer_subject(text):
    text_lower = text.lower()
    for subject, keywords in SUBJECT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                return subject
    return "General"
