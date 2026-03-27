import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(resume_text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume analyzer."
            },
            {
                "role": "user",
                "content": f"""
                Analyze this resume and provide:
                1. Top 3 strengths
                2. Top 3 weaknesses
                3. Key skills found
                4. Overall score out of 10
                
                Resume:
                {resume_text}
                """
            }
        ]
    )
    return response.choices[0].message.content
