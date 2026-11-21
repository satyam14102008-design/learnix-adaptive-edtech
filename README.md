# Learnix AI — Adaptive Exam-Prep Tutor
> **Intelligent, Responsive, Cognitive AI-Powered Adaptive Learning Platform for Class 10 Physics.**

[![React](https://img.shields.io/badge/React-18-blue.svg)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-blue.svg)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688.svg)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Supported-green.svg)](https://www.mongodb.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-38bdf8.svg)](https://tailwindcss.com/)

Learnix AI is not a generic chatbot. Its core engine tracks individual student understanding, analyzes free-form written explanations to identify misconceptions, adapts question difficulty dynamically, and schedules spaced repetitions.

---

## 🌟 Key Features

1. **Continuous Learner Modeling**: Maintains an explainable mastery score ($0-100\%$) and confidence level for all 26 sub-concepts across Class 10 Physics.
2. **Cognitive Reasoning & Misconception Analysis**: Analyzes student written reasoning using Gemini API and structured heuristic physics databases. Detects specific fallacies (e.g. *"current gets consumed by bulbs"* or *"longer wires decrease resistance"*).
3. **Interactive Concept Graph**: Built with React Flow. Explore directional prerequisite dependencies, filter by chapter, and view live mastery heatmaps.
4. **Adaptive Learning Arena**: Serves problems matched to the student's mastery tier, evaluates reasoning, provides step-by-step physical explanations, and recalculates mastery in real time.
5. **SuperMemo-2 (SM-2) Spaced Repetition**: Predicts forgetting risk and schedules retention reviews.
6. **Class 10 Physics Comprehensive Coverage**:
   - Chapter 1: Light – Reflection & Refraction
   - Chapter 2: Human Eye & Colourful World
   - Chapter 3: Electricity
   - Chapter 4: Magnetic Effects of Electric Current
   - Chapter 5: Chemical Effects of Electric Current
   - Chapter 6: Force & Motion Fundamentals
7. **Teacher Analytics & Class Concept Heatmap**: Cohort overview, student roster with drilldown, concept gap analysis, and assignment creator.
8. **1-Click Demo Ready**: Zero setup required. Features pre-seeded demo accounts for both Student and Teacher with historical mastery data, attempts, and analytics.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10+
- Node.js 18+ (v20+ recommended)
- MongoDB *(Optional: Application includes an automatic In-Memory Document Store if MongoDB is not running locally!)*

### 2. Backend Setup
```bash
cd backend
python -m pip install -r requirements.txt
python main.py
```
*The FastAPI backend will start at `http://localhost:8000` and automatically seed all chapters, concepts, questions, and demo accounts.*

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
*The Vite development server will open at `http://localhost:5173` with automatic API proxying.*

---

## 🎮 Instant Demo Evaluation

When exploring the application:
1. Visit `http://localhost:5173`.
2. Click **"Demo Student"** on the landing page or login screen to immediately explore the student experience as **Alex Chen** (mastery rings, adaptive arena, concept graph, diagnostic reports).
3. Click **"Switch to Teacher View"** or **"Demo Teacher"** to access the cohort dashboard as **Dr. Sarah Jenkins** (class concept heatmap, student roster, assignment management).

---

## 📁 Repository Structure
```
learnix-ai/
├── frontend/
│   ├── src/
│   │   ├── components/       # Custom React Flow nodes, badges, cards
│   │   ├── pages/            # Landing, Dashboard, Arena, ConceptGraph, Diagnostic, Revision, Teacher
│   │   ├── layouts/          # AppLayout with sidebar & header
│   │   ├── context/          # AuthContext with session persistence
│   │   ├── services/         # API client with automatic endpoints
│   │   └── types/            # Complete TypeScript interfaces
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/              # FastAPI route endpoints
│   │   ├── ai/               # Gemini prompt templates, fallback engine, misconception database
│   │   ├── algorithms/       # Learner model update logic, SM-2 spaced repetition, adaptive selection
│   │   ├── database/         # Hybrid MongoDB & In-Memory document store
│   │   ├── schemas/          # Pydantic models
│   │   ├── services/         # Seed service and business logic
│   │   └── utils/            # JWT auth and security helpers
│   ├── main.py
│   └── requirements.txt
│
├── docs/
│   ├── architecture.md       # Architecture diagrams & component design
│   ├── database.md           # MongoDB schemas & collections
│   └── learner_model.md      # Mathematical formulations & SM-2 algorithms
│
├── README.md
└── .env.example
```
