import React, { createContext, useContext, useState, useEffect } from 'react';
import { Subject } from '../types';
import { api } from '../services/api';

export const DEFAULT_SUBJECTS: Subject[] = [
  {
    id: 'physics',
    name: 'Physics',
    icon: 'Zap',
    color: 'from-blue-600 to-indigo-600',
    badgeColor: 'bg-blue-50 text-blue-700 border-blue-200',
    gradient: 'bg-gradient-to-tr from-blue-600 to-indigo-600',
    tagline: 'Electricity, Optics & Mechanics',
    accent: 'blue',
    average_mastery: 74,
    total_chapters: 6,
    total_concepts: 26,
    mastered_concepts: 12
  },
  {
    id: 'chemistry',
    name: 'Chemistry',
    icon: 'FlaskConical',
    color: 'from-emerald-600 to-teal-600',
    badgeColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
    gradient: 'bg-gradient-to-tr from-emerald-600 to-teal-600',
    tagline: 'Reactions, Acids & Carbon',
    accent: 'emerald',
    average_mastery: 68,
    total_chapters: 4,
    total_concepts: 15,
    mastered_concepts: 6
  },
  {
    id: 'biology',
    name: 'Biology',
    icon: 'Dna',
    color: 'from-rose-600 to-pink-600',
    badgeColor: 'bg-rose-50 text-rose-700 border-rose-200',
    gradient: 'bg-gradient-to-tr from-rose-600 to-pink-600',
    tagline: 'Life Processes & Genetics',
    accent: 'rose',
    average_mastery: 81,
    total_chapters: 4,
    total_concepts: 15,
    mastered_concepts: 9
  },
  {
    id: 'mathematics',
    name: 'Mathematics',
    icon: 'Sigma',
    color: 'from-amber-500 to-orange-600',
    badgeColor: 'bg-amber-50 text-amber-700 border-amber-200',
    gradient: 'bg-gradient-to-tr from-amber-500 to-orange-600',
    tagline: 'Algebra & Trigonometry',
    accent: 'amber',
    average_mastery: 72,
    total_chapters: 4,
    total_concepts: 16,
    mastered_concepts: 8
  }
];

interface SubjectContextType {
  selectedSubject: string; // 'all' | 'physics' | 'chemistry' | 'biology' | 'mathematics'
  setSelectedSubject: (id: string) => void;
  subjects: Subject[];
  refreshSubjects: () => Promise<void>;
  currentSubjectMeta: Subject | null;
}

const SubjectContext = createContext<SubjectContextType | undefined>(undefined);

export const SubjectProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [selectedSubject, setSelectedSubjectState] = useState<string>(() => {
    return localStorage.getItem('learnix_active_subject') || 'all';
  });
  const [subjects, setSubjects] = useState<Subject[]>(DEFAULT_SUBJECTS);

  const setSelectedSubject = (id: string) => {
    setSelectedSubjectState(id);
    localStorage.setItem('learnix_active_subject', id);
  };

  const refreshSubjects = async () => {
    try {
      const data = await api.getSubjects();
      if (Array.isArray(data) && data.length > 0) {
        setSubjects(data);
      }
    } catch (e) {
      // Fallback already in initial state
    }
  };

  useEffect(() => {
    refreshSubjects();
  }, []);

  const currentSubjectMeta = subjects.find((s) => s.id === selectedSubject) || null;

  return (
    <SubjectContext.Provider
      value={{
        selectedSubject,
        setSelectedSubject,
        subjects,
        refreshSubjects,
        currentSubjectMeta,
      }}
    >
      {children}
    </SubjectContext.Provider>
  );
};

export const useSubject = () => {
  const context = useContext(SubjectContext);
  if (!context) {
    throw new Error('useSubject must be used within a SubjectProvider');
  }
  return context;
};
