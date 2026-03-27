import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def match_job(resume_text, job_description):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert job match analyzer."
            },
            {
                "role": "user",
                "content": f"""
                Compare this resume against the job description and provide:
                1. Match percentage (out of 100%)
                2. Top 3 matching skills
                3. Top 3 missing skills
                4. Should they apply? YES or NO and why
                
                Resume:
                {resume_text}
                
                Job Description:
                {job_description}
                """
            }
        ]
    )
    return response.choices[0].message.content