# dubber-challenge
Dubber Junior Developer Coding Challenge

## Introduction
First of all, I decided to make a full-stack app to demonstrate the Lottery Challenge. Which uses React at Frontend and Python FastAPI at Backend.
I could directly develop it with using with React and make the number generator directly with javascript in React but I wanted to illustrate that how I build full-stack structure and what kind of additions I could do in future. Recently, I am also trying to get AWS Cloud Practioner Certificate so I also wanted to give additional info that how I would move this full-stack app to AWS or even maybe Kubernetes in AWS. So let's start.

## STEP 1: INITIALIZATION 
Started with installing necessary packages for backend and created backend folder. 
Frontend:
- Created a Python VENV : python3 -m venv venv
- Activated Venv to install necessary packages with pip: source venv/bin/activate
- Installed necessary packages (fastapi, uvicorn) on requirements.txt that I created: pip install -r requirements.txt

Backend:
- On terminal I created Vite Application with React Framework for Frontend: npm create vite@latest frontend --template react
- I deleted the unnecessary files and example codes in App.jsx and leaved ready to write my code in src/App.jsx
- Installed tailwindcss to give a basic good look. Source: https://tailwindcss.com/docs/installation/using-vite

## STEP 2: BACKEND
- Started with adding goals in comment section. Created FastAPI app.
- Added the generate numbers endpoint.
- Added future possible scenarios as comments in app.py
- Run the backend with uvicorn app:app --reload and test the endpoint over http://127.0.0.1:8000/docs

## STEP 3: FRONTEND
- I will keep it simple so I am planning to center the lottery balls, a title and bonus ball in the one division which will cover screen height and generate button to generate balls.
- HTML part added, styling addded with tailwindcss.
- Generator is working now.
- Test the frontend with: npm run dev

## STEP 4: FUTURE PLANS
- I mentioned about them mostly in the comments of scripts. If I had more time I would add, sound, animations to balls, routing system, user system. On the other hand, at backend side we could add more endpoints to keep history of the lotteries, authentication systems, user systems, database connections, saving lotteries to database etc.
- I could write a dockerfiles to containerize the apps.
- Could create YAML files for kubernetes deployments.
