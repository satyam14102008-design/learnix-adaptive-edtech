from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

# Auth
class SignupRequest(BaseModel):
    email: str
    password: str
    name: str
    role: str = "student"  # 'student' or 'teacher'
    grade: Optional[str] = "Class 10"

class LoginRequest(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    token: str
    user: Dict[str, Any]

# Student Dashboard
class DashboardResponse(BaseModel):
    greeting: str
    student: Dict[str, Any]
    stats: Dict[str, Any]
    grades: Optional[List[Dict[str, Any]]] = None
    active_grade: Optional[int] = 10
    subjects: Optional[List[Dict[str, Any]]] = None
    subject_stats: Optional[List[Dict[str, Any]]] = None
    active_subject: Optional[str] = "all"
    mastery_by_chapter: List[Dict[str, Any]]
    weak_concepts: List[Dict[str, Any]]
    strong_concepts: List[Dict[str, Any]]
    recommended_next_lesson: Dict[str, Any]
    upcoming_revisions: List[Dict[str, Any]]
    weekly_activity: List[Dict[str, Any]]
    recent_attempts: List[Dict[str, Any]]
    achievements: List[Dict[str, Any]]

# Learning Arena
class QuestionOption(BaseModel):
    id: str
    text: str

class AdaptiveQuestionDto(BaseModel):
    id: str
    grade: Optional[int] = 10
    subject_id: Optional[str] = "physics"
    subject_name: Optional[str] = "Physics"
    chapter_id: str
    chapter_name: str
    concept_id: str
    concept_name: str
    difficulty: str
    question_type: str
    question_text: str
    options: List[QuestionOption]
    hint: Optional[str] = None
    expected_reasoning: Optional[str] = None
    prerequisites: List[str] = []
    current_mastery: float = 0.0

class SubmitAnswerRequest(BaseModel):
    question_id: str
    concept_id: str
    selected_option: str
    student_reasoning: str
    response_time_seconds: float = 20.0

class SubmitAnswerResponse(BaseModel):
    is_correct: bool
    correct_option: str
    explanation: str
    student_reasoning: str
    reasoning_analysis: Dict[str, Any]
    misconception: Optional[Dict[str, Any]] = None
    remediation: Optional[str] = None
    remediation_activity: Optional[str] = None
    mastery_update: Dict[str, Any]
    xp_awarded: int
    streak_days: int
    next_question_ready: bool = True

# Concept Graph
class GraphNodeData(BaseModel):
    id: str
    grade: Optional[int] = 10
    label: str
    subject_id: Optional[str] = "physics"
    subject_name: Optional[str] = "Physics"
    chapter_id: str
    chapter_name: str
    mastery: float
    confidence: float
    difficulty: str
    status: str  # 'mastered', 'learning', 'needs_improvement', 'weak'
    total_attempts: int
    correct_attempts: int
    misconceptions: List[str]
    formula: Optional[str] = None

class GraphNode(BaseModel):
    id: str
    type: str = "conceptNode"
    position: Dict[str, float]
    data: GraphNodeData

class GraphEdge(BaseModel):
    id: str
    source: str
    target: str
    label: Optional[str] = None
    animated: bool = False
    relationship_type: str

class ConceptGraphResponse(BaseModel):
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    chapters: List[Dict[str, Any]]
    subjects: Optional[List[Dict[str, Any]]] = None
    overall_mastery: float

# Diagnostic Assessment
class DiagnosticQuestion(BaseModel):
    id: str
    chapter_id: str
    chapter_name: str
    concept_id: str
    concept_name: str
    difficulty: str
    question_text: str
    options: List[QuestionOption]
    requires_reasoning: bool = True

class DiagnosticSubmissionItem(BaseModel):
    question_id: str
    concept_id: str
    selected_option: str
    reasoning: str
    response_time_seconds: float = 30.0

class SubmitDiagnosticRequest(BaseModel):
    answers: List[DiagnosticSubmissionItem]

# Teacher
class TeacherDashboardResponse(BaseModel):
    total_students: int
    class_average_mastery: float
    at_risk_students_count: int
    active_streaks_count: int
    weakest_concepts: List[Dict[str, Any]]
    strongest_concepts: List[Dict[str, Any]]
    misconception_distribution: List[Dict[str, Any]]
    chapter_averages: List[Dict[str, Any]]
    students: List[Dict[str, Any]]
    recent_assignments: List[Dict[str, Any]]

class CreateAssignmentRequest(BaseModel):
    title: str
    chapter_id: str
    target_concepts: List[str]
    assigned_class: str = "Class 10-A"
    due_date: str
