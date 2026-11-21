import {
  User,
  AdaptiveQuestion,
  SubmissionResponse,
  LearningPathItem,
  RevisionItem,
  TeacherDashboardData
} from '../types';

const env = (import.meta as any).env;
const API_BASE = env?.VITE_API_URL 
  ? `${env.VITE_API_URL.replace(/\/$/, '')}/api` 
  : '/api';

function getAuthHeader(): Record<string, string> {
  const token = localStorage.getItem('learnix_token');
  return token ? { 'Authorization': `Bearer ${token}` } : {};
}

async function request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const headers = {
    'Content-Type': 'application/json',
    ...getAuthHeader(),
    ...options.headers,
  };

  try {
    const res = await fetch(`${API_BASE}${endpoint}`, {
      ...options,
      headers,
    });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.detail || `HTTP Error ${res.status}`);
    }

    return await res.json();
  } catch (err: any) {
    console.warn(`[Learnix API] Request failed for ${endpoint}:`, err.message);
    throw err;
  }
}

export const api = {
  // Auth
  login: (data: { email: string; password: string }) =>
    request<{ token: string; user: User }>('/auth/login', { method: 'POST', body: JSON.stringify(data) }),

  signup: (data: { email: string; password: string; name: string; role?: string; grade?: string }) =>
    request<{ token: string; user: User }>('/auth/signup', { method: 'POST', body: JSON.stringify(data) }),

  demoLogin: (role: 'student' | 'teacher') =>
    request<{ token: string; user: User }>(`/auth/demo-login/${role}`, { method: 'POST' }),

  getMe: () =>
    request<User>('/auth/me'),

  // Grades
  getGrades: () =>
    request<any[]>('/student/grades'),

  // Subjects
  getSubjects: (params?: { grade?: number }) => {
    const query = new URLSearchParams();
    if (params?.grade) query.append('grade', params.grade.toString());
    const qs = query.toString() ? `?${query.toString()}` : '';
    return request<any[]>(`/student/subjects${qs}`);
  },

  // Student Dashboard
  getStudentDashboard: (params?: { subject?: string; grade?: number }) => {
    const query = new URLSearchParams();
    if (params?.subject) query.append('subject', params.subject);
    if (params?.grade) query.append('grade', params.grade.toString());
    const qs = query.toString() ? `?${query.toString()}` : '';
    return request<any>(`/student/dashboard${qs}`);
  },

  getStudentMastery: () =>
    request<any[]>('/student/mastery'),

  getLearningPath: () =>
    request<LearningPathItem[]>('/student/learning-path'),

  getRevisions: () =>
    request<RevisionItem[]>('/student/revisions'),

  // Adaptive Learning Arena
  getNextQuestion: (params?: { grade?: number; subject_id?: string; chapter_id?: string; concept_id?: string }) => {
    const query = new URLSearchParams();
    if (params?.grade) query.append('grade', params.grade.toString());
    if (params?.subject_id) query.append('subject_id', params.subject_id);
    if (params?.chapter_id) query.append('chapter_id', params.chapter_id);
    if (params?.concept_id) query.append('concept_id', params.concept_id);
    const qs = query.toString() ? `?${query.toString()}` : '';
    return request<AdaptiveQuestion>(`/learning/next-question${qs}`);
  },

  submitAnswer: (data: {
    question_id: string;
    concept_id: string;
    selected_option: string;
    student_reasoning: string;
    response_time_seconds?: number;
  }) => request<SubmissionResponse>('/learning/submit-answer', {
    method: 'POST',
    body: JSON.stringify(data),
  }),

  getConceptGraph: (params?: { grade?: number; subject_id?: string }) => {
    const query = new URLSearchParams();
    if (params?.grade) query.append('grade', params.grade.toString());
    if (params?.subject_id) query.append('subject_id', params.subject_id);
    const qs = query.toString() ? `?${query.toString()}` : '';
    return request<any>(`/learning/concept-graph${qs}`);
  },

  // Diagnostic
  startDiagnostic: (params?: { grade?: number; subject_id?: string }) => {
    const query = new URLSearchParams();
    if (params?.grade) query.append('grade', params.grade.toString());
    if (params?.subject_id) query.append('subject_id', params.subject_id);
    const qs = query.toString() ? `?${query.toString()}` : '';
    return request<any>(`/assessment/start${qs}`, { method: 'POST' });
  },

  submitDiagnostic: (data: { answers: any[] }) =>
    request<any>('/assessment/submit', { method: 'POST', body: JSON.stringify(data) }),

  // Revision Center
  getDueRevisions: () =>
    request<any>('/revision/due'),

  completeRevision: (data: { concept_id: string; quality_score: number }) =>
    request<any>('/revision/complete', { method: 'POST', body: JSON.stringify(data) }),

  // Teacher Dashboard
  getTeacherDashboard: () =>
    request<TeacherDashboardData>('/teacher/dashboard'),

  getConceptGaps: () =>
    request<any>('/teacher/concept-gaps'),

  createAssignment: (data: {
    title: string;
    chapter_id: string;
    target_concepts: string[];
    assigned_class?: string;
    due_date: string;
  }) => request<any>('/teacher/assignments', { method: 'POST', body: JSON.stringify(data) }),
};
