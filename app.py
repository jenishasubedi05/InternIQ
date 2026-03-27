import streamlit as st
import google.generativeai as genai
from agents.resume_agent import analyze_resume
from agents.job_match_agent import match_job
from agents.cover_letter_agent import generate_cover_letter

# Page Setup
st.set_page_config(
    page_title="InternIQ",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 InternIQ — AI Internship Assistant")
st.subheader("Powered by 3 AI Agents working together!")

# Divider
st.divider()

# Step 1 — Resume Input
st.header("📄 Step 1 — Paste Your Resume")
resume_text = st.text_area(
    "Paste your resume text here",
    height=200,
    placeholder="Paste your entire resume here..."
)

# Step 2 — Job Description Input
st.header("📋 Step 2 — Paste Job Description")
job_description = st.text_area(
    "Paste the job description here",
    height=200,
    placeholder="Paste the internship job description here..."
)

# Analyze Button
if st.button("🚀 Analyze with AI Agents!", type="primary"):
    if resume_text and job_description:
        
        # Agent 1
        with st.spinner("🤖 Agent 1 is analyzing your resume..."):
            resume_analysis = analyze_resume(resume_text)
        
        st.success("✅ Agent 1 Done!")
        st.header("🤖 Agent 1 — Resume Analysis")
        st.write(resume_analysis)
        st.divider()
        
        # Agent 2
        with st.spinner("🎯 Agent 2 is matching you to the job..."):
            job_match = match_job(resume_text, job_description)
        
        st.success("✅ Agent 2 Done!")
        st.header("🎯 Agent 2 — Job Match Results")
        st.write(job_match)
        st.divider()
        
        # Agent 3
        with st.spinner("✍️ Agent 3 is writing your cover letter..."):
            cover_letter = generate_cover_letter(
                resume_text,
                job_description,
                resume_analysis,
                job_match
            )
        
        st.success("✅ Agent 3 Done!")
        st.header("✍️ Agent 3 — Your Cover Letter")
        st.write(cover_letter)
        st.divider()
        
        st.balloons()
        st.success("🎉 All 3 Agents completed successfully!")
    
    else:
        st.error("⚠️ Please paste both your resume AND job description!")
