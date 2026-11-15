# FuturePath: Career Counselor & TNEA Seat Predictor Chatbot

A Python-based, knowledge-driven career counseling chatbot designed to help Class 12 students in Tamil Nadu discover specialized academic streams aligned with their personal hobbies and interests—moving beyond conventional engineering and medical paths to include Aviation, Cyber Security, Marine Engineering, Defense, Forensics, Veterinary Science, Architecture, Design, Law, Finance, and Performing Arts.

---

## Key Features

- **Official TNEA Cutoff Calculation:** Computes standardized cutoffs out of 200 based on the current 100-mark-per-subject Tamil Nadu Higher Secondary scheme:
  $$\text{Cutoff} = \text{Maths} + \left(\frac{\text{Physics}}{2}\right) + \left(\frac{\text{Chemistry}}{2}\right)$$
- **Multi-Hobby Keyword Filtering:** Supports simultaneous comma-separated interest searches (e.g., `aero, cyber, photography, gaming`) using regular expression matching across a curated dataset.
- **Curated 134-Program Knowledge Base:** Covers Anna University departments (CEG, MIT, ACT, SAP), all 13 constituent University Colleges of Engineering, Government & Government-Aided colleges, top self-financing institutions, and specialized arts, medical, maritime, and defense institutes across Tamil Nadu.
- **Seat Probability Prediction:** Compares the student's cutoff against reference cutoffs ($\Delta = \text{User Cutoff} - \text{Reference Cutoff}$) to classify admission chances:
  - **High Chance** ($\Delta \ge 2.0$)
  - **Moderate / Borderline** ($-1.5 \le \Delta < 2.0$)
  - **Low Chance / Reach** ($\Delta < -1.5$)

---

## Working Principle

The system operates as a **Deterministic Knowledge-Based Recommender Engine** following three phases:

1. **Normalization:** Converts raw 100-scale Maths, Physics, and Chemistry marks into a unified TNEA cutoff out of 200.
2. **Pattern Matching:** Parses user-entered hobbies into regex keyword queries to filter relevant `hobby_tag` entries in `anna_university_colleges_2026.csv`.
3. **Heuristic Ranking:** Evaluates the cutoff variance ($\Delta$) for each matched program and outputs a ranked table sorted by historical cutoff competitiveness.
<img width="790" height="1321" alt="TNEA Cutoff-Based College Recommendation Flowchart" src="https://github.com/user-attachments/assets/5992a46f-90d2-42f2-b3a4-1d02d44b88cb" />

