import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_cover_letter(resume_text, job_description, resume_analysis, job_match):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert cover letter writer."
            },
            {
                "role": "user",
                "content": f"""
                Using the resume analysis and job match results,
                write a professional and compelling cover letter.
                
                Make it:
                1. Personalized to the job
                2. Highlight matching skills
                3. Address missing skills positively
                4. Professional but warm tone
                5. Maximum 3 paragraphs
                
                Resume:
                {resume_text}
                
                Job Description:
                {job_description}
                
                Resume Analysis:
                {resume_analysis}
                
                Job Match Results:
                {job_match}
                """
            }
        ]
    )
    return response.choices[0].message.content
