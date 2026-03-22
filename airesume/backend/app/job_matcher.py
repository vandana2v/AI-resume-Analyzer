from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.database import jobs_collection

def match_jobs(resume_text):
    jobs = list(jobs_collection.find())
    job_texts = [job["description"] + " " + job["skills"] for job in jobs]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text] + job_texts)

    similarities = cosine_similarity(vectors[0:1], vectors[1:])[0]

    results = []
    for job, score in zip(jobs, similarities):
        results.append({
            "title": job["title"],
            "company": job["company"],
            "match_score": int(score * 100)
        })

    return sorted(results, key=lambda x: x["match_score"], reverse=True)