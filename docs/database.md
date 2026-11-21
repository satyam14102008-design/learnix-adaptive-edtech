# Learnix AI — Database Architecture & Schema Design

Learnix AI uses a document-oriented database design with MongoDB. It supports live MongoDB instances via PyMongo and features an automatic In-Memory Document fallback engine for zero-config demonstration.

---

## 1. Database Collections Overview

| Collection Name | Description | Key Indexes |
|---|---|---|
| `users` | User accounts (students, teachers), roles, XP, and credentials | `email` (unique), `role` |
| `chapters` | Syllabus chapters for Class 10 Physics | `id`, `order` |
| `concepts` | Granular concept nodes with formulas & difficulty baselines | `id`, `chapter_id` |
| `concept_relationships` | Directed edges (prerequisites, reinforces, applications) | `source_concept_id`, `target_concept_id` |
| `questions` | Curriculum question bank with expected reasoning & distractors | `id`, `concept_id`, `chapter_id`, `difficulty` |
| `attempts` | Complete historical audit log of student question submissions | `student_id`, `question_id`, `timestamp` |
| `learner_models` | Live concept mastery (0-100), confidence, attempts, and misconceptions | `student_id`, `concept_id` (compound unique) |
| `misconceptions` | Structured catalog of Class 10 physics misconceptions & remediations | `id`, `chapter_id`, `concept_id` |
| `revision_schedules` | SuperMemo-2 spaced repetition state, intervals, and due dates | `student_id`, `concept_id`, `due_date` |
| `learning_paths` | Individualized roadmaps with prioritized milestones | `student_id`, `concept_id` |
| `assignments` | Teacher-created class tasks, target concepts, and completion metrics | `teacher_id`, `chapter_id`, `due_date` |

---

## 2. Document Schemas

### 2.1. `users`
```json
{
  "_id": "student_alex_chen",
  "email": "student@learnix.ai",
  "password_hash": "$2b$12$...",
  "name": "Alex Chen",
  "role": "student",
  "grade": "Class 10",
  "target_exam": "CBSE Physics Board Exam",
  "avatar": "https://api.dicebear.com/7.x/bottts/svg?seed=Alex",
  "xp": 1420,
  "level": 4,
  "level_title": "Quantum Apprentice",
  "streak_days": 6,
  "daily_goal": 5,
  "daily_completed": 3,
  "total_study_minutes": 240,
  "created_at": "2026-11-21T07:45:00Z"
}
```

### 2.2. `learner_models`
Tracks live concept mastery for every student:
```json
{
  "_id": "lm_6b014d",
  "student_id": "student_alex_chen",
  "concept_id": "c_resistance_factors",
  "concept_name": "Resistance & Resistivity",
  "chapter_id": "electricity",
  "mastery_score": 36.0,
  "confidence_level": 0.40,
  "total_questions_answered": 9,
  "correct_answers": 3,
  "incorrect_answers": 6,
  "last_studied": "2026-11-21T01:45:00Z",
  "current_difficulty": "easy",
  "misconceptions_detected": [
    "Longer Wire Decreases Resistance"
  ],
  "revision_due_date": "2026-11-22T07:45:00Z",
  "review_interval_days": 1,
  "ease_factor": 2.2
}
```

### 2.3. `concept_relationships`
Directed edges in the curriculum graph:
```json
{
  "_id": "rel_ohms_series",
  "source_concept_id": "c_ohms_law",
  "target_concept_id": "c_series_circuits",
  "relationship_type": "prerequisite"
}
```

### 2.4. `attempts`
Complete historical student submissions:
```json
{
  "_id": "att_9a8b7c",
  "student_id": "student_alex_chen",
  "question_id": "q_elec_rf_01",
  "concept_id": "c_resistance_factors",
  "selected_option": "B",
  "is_correct": true,
  "reasoning": "When wire is stretched to double length, volume is conserved so area must halve...",
  "reasoning_score": 0.88,
  "mastery_before": 36.0,
  "mastery_after": 48.2,
  "misconception_detected": false,
  "response_time_seconds": 24.5,
  "timestamp": "2026-11-21T07:40:00Z"
}
```

---

## 3. Seeded Accounts

1. **Student Account**:
   - Email: `student@learnix.ai`
   - Password: `password123`
   - Role: `student`
   - Profile: Alex Chen (CBSE Class 10 Physics)

2. **Teacher Account**:
   - Email: `teacher@learnix.ai`
   - Password: `password123`
   - Role: `teacher`
   - Profile: Dr. Sarah Jenkins (St. Jude Senior Academy)
