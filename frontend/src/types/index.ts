export interface User {
  id?: string;
  _id?: string;
  name: string;
  email: string;
  role: 'student' | 'teacher';
  avatar?: string;
  grade?: string;
  target_exam?: string;
  xp?: number;
  level?: number;
  level_title?: string;
  streak_days?: number;
  daily_goal?: number;
  daily_completed?: number;
  total_study_minutes?: number;
}

export interface Grade {
  id: string; // 'class_9' | 'class_10' | 'class_11' | 'class_12'
  grade: number; // 9 | 10 | 11 | 12
  name: string;
  tagline: string;
  badge: string;
  exam_focus: string;
  color: string;
  accent: string;
  description?: string;
  total_chapters?: number;
  total_concepts?: number;
  average_mastery?: number;
}

export interface Subject {
  id: string; // 'physics' | 'chemistry' | 'biology' | 'mathematics'
  name: string;
  icon: string;
  color: string;
  gradient?: string;
  badgeColor?: string;
  accent?: string;
  tagline?: string;
  average_mastery?: number;
  total_chapters?: number;
  total_concepts?: number;
  mastered_concepts?: number;
}

export interface Chapter {
  id: string;
  chapter_id?: string;
  grade?: number;
  subject_id?: string;
  subject_name?: string;
  title: string;
  order?: number;
  description?: string;
  icon?: string;
  color?: string;
  average_mastery?: number;
  total_concepts?: number;
  mastered_concepts?: number;
}

export interface ConceptMastery {
  concept_id: string;
  concept_name: string;
  chapter_id: string;
  grade?: number;
  subject_id?: string;
  subject_name?: string;
  mastery_score: number;
  confidence_level?: number;
  current_difficulty?: 'easy' | 'medium' | 'hard' | 'advanced';
  misconceptions_count?: number;
  misconceptions_detected?: string[];
  last_studied?: string;
  revision_due_date?: string;
}

export interface GraphNodeData {
  id: string;
  grade?: number;
  label: string;
  subject_id?: string;
  subject_name?: string;
  chapter_id: string;
  chapter_name: string;
  mastery: number;
  confidence: number;
  difficulty: string;
  status: 'mastered' | 'learning' | 'needs_improvement' | 'weak';
  total_attempts: number;
  correct_attempts: number;
  misconceptions: string[];
  formula?: string;
}

export interface QuestionOption {
  id: string;
  text: string;
}

export interface AdaptiveQuestion {
  id: string;
  grade?: number;
  subject_id?: string;
  subject_name?: string;
  chapter_id: string;
  chapter_name: string;
  concept_id: string;
  concept_name: string;
  difficulty: 'easy' | 'medium' | 'hard' | 'advanced';
  question_type: 'mcq' | 'numerical' | 'conceptual';
  question_text: string;
  options: QuestionOption[];
  hint?: string;
  expected_reasoning?: string;
  prerequisites: string[];
  current_mastery: number;
  selection_reason?: string;
}

export interface ReasoningAnalysis {
  reasoning_score: number;
  is_sound: boolean;
  misconception_detected: boolean;
  misconception_id?: string;
  misconception_label?: string;
  why_reasoning_flawed?: string;
  feedback_to_student: string;
  key_rule_to_remember: string;
}

export interface Misconception {
  id: string;
  chapter_id?: string;
  concept_id?: string;
  label: string;
  description: string;
  why_incorrect: string;
  remediation: string;
  remediation_activity?: string;
}

export interface MasteryUpdateBreakdown {
  previous_mastery: number;
  new_mastery: number;
  delta: number;
  previous_confidence: number;
  new_confidence: number;
  difficulty: string;
  recommended_next_difficulty: string;
  reasoning_score: number;
  explanation: string;
}

export interface SubmissionResponse {
  is_correct: boolean;
  correct_option: string;
  explanation: string;
  student_reasoning: string;
  reasoning_analysis: ReasoningAnalysis;
  misconception?: Misconception | null;
  remediation?: string | null;
  remediation_activity?: string | null;
  mastery_update: MasteryUpdateBreakdown;
  xp_awarded: number;
  streak_days: number;
  next_question_ready: boolean;
}

export interface LearningPathItem {
  id: string;
  concept_id: string;
  concept_name: string;
  chapter_id: string;
  priority: 'Critical' | 'High' | 'Medium' | 'Low';
  estimated_minutes: number;
  status: 'completed' | 'in_progress' | 'locked';
  mastery_target: number;
  reason: string;
  recommended_activity: string;
}

export interface RevisionItem {
  concept_id: string;
  concept_name: string;
  chapter_id: string;
  due_date: string;
  mastery_score: number;
  interval_days: number;
  repetition_count: number;
  status: 'due_today' | 'overdue' | 'upcoming';
}

export interface TeacherDashboardData {
  total_students: number;
  class_average_mastery: number;
  at_risk_students_count: number;
  active_streaks_count: number;
  weakest_concepts: Array<{
    concept_id: string;
    concept_name: string;
    chapter_id?: string;
    average_mastery: number;
    students_affected_by_misconception: number;
  }>;
  strongest_concepts: Array<{
    concept_id: string;
    concept_name: string;
    chapter_id?: string;
    average_mastery: number;
  }>;
  misconception_distribution: Array<{
    label: string;
    students_count: number;
    chapter: string;
  }>;
  chapter_averages: Array<{
    chapter_id: string;
    title: string;
    average_mastery: number;
  }>;
  students: Array<{
    id: string;
    name: string;
    email: string;
    avatar: string;
    mastery: number;
    streak_days: number;
    xp: number;
    weak_concepts_count: number;
    total_questions_answered: number;
    status: string;
  }>;
  recent_assignments: Array<{
    id: string;
    title: string;
    chapter_id: string;
    due_date: string;
    total_assigned: number;
    completed_count: number;
    average_score: number;
  }>;
}
