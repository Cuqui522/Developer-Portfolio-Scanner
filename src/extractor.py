def extract_skills(text):
    skills = ["python", "sql", "machine learning", "excel", "javascript"]
    return [skill for skill in skills if skill in text]


def extract_availability(text):
    keywords = ["open to work", "available", "freelance", "hire me"]
    return any(word in text for word in keywords)