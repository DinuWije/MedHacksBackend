# SentiJournal
Hackathon Project for MedHacks 2020


# What it does
SentiJournal provides a platform for patients to write brief journals based on their daily emotions and experiences. These journals are then analyzed by the Google Natural Language Processing API, to give a breakdown of the sentiment (overall emotion) in the journal. Caregivers (such as physicians, therapists, and family members) can view the sentiment breakdown and gain a better understanding of the patient's mental well being. Over time, as the patient contributes more daily journals, caregivers can better track and understand the patient's mental health and overall happiness based on the overall emotions present in their self-reflections.

# Tech Stack
With a comprehensive backend and user-friendly frontend, SentiJournal seeks to make using the app easy for all parties involved. The backend is built with python, using a locally hosted Flask webserver and SQLite database for storage. Once journals are submitted by patients, the backend makes a call to Google Cloud's NLP Sentiment Analysis API. This breakdown is then passed along to caregivers via HTTP requests. The backend also manages logins/user registration with tokens.


The frontend of SentiJournal is a Kotlin-based app developed with Android Studio which collects information from users and passes it along to the backend via HTTP requests. The front end is designed with the intention of making it easily accessible and understandable for patients, and clean/organized for caregivers. 

# Check it out:
[On Devpost!](https://devpost.com/software/sentijournal)
