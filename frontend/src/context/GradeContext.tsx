import React, { createContext, useContext, useState, useEffect } from 'react';
import { Grade } from '../types';
import { api } from '../services/api';

export const DEFAULT_GRADES: Grade[] = [
  {
    id: 'class_9',
    grade: 9,
    name: 'Class 9',
    tagline: 'Foundational High School STEM',
    badge: 'Foundation',
    exam_focus: 'CBSE 9th Foundation & Science Olympiads',
    color: 'from-emerald-500 to-teal-600',
    accent: 'emerald',
    description: 'Kinematics, Atomic Structure, Cell Biology, Number Systems & Triangles',
    total_chapters: 8,
    total_concepts: 16,
    average_mastery: 72
  },
  {
    id: 'class_10',
    grade: 10,
    name: 'Class 10',
    tagline: 'Secondary Board Exam Mastery',
    badge: 'Board Exam',
    exam_focus: 'CBSE / ICSE Class 10 Board Examinations',
    color: 'from-blue-600 to-indigo-600',
    accent: 'blue',
    description: 'Optics & Electricity, Chemical Reactions & Carbon, Life Processes, Trigonometry',
    total_chapters: 18,
    total_concepts: 74,
    average_mastery: 74
  },
  {
    id: 'class_11',
    grade: 11,
    name: 'Class 11',
    tagline: 'Senior Secondary & JEE/NEET Pre',
    badge: 'JEE / NEET Pre',
    exam_focus: 'JEE Main / NEET Foundation & Senior Secondary',
    color: 'from-violet-600 to-purple-600',
    accent: 'violet',
    description: 'Rotational Mechanics & Thermo, Chemical Bonding, Physiology, Conic Sections & Calculus',
    total_chapters: 8,
    total_concepts: 16,
    average_mastery: 66
  },
  {
    id: 'class_12',
    grade: 12,
    name: 'Class 12',
    tagline: 'Boards & National Entrance (JEE/NEET)',
    badge: 'Board + JEE/NEET',
    exam_focus: 'Class 12 Boards & National Competitive Entrances',
    color: 'from-amber-500 to-rose-600',
    accent: 'amber',
    description: 'Electrostatics & Wave Optics, Organic Mechanisms, Molecular Genetics, Integral Calculus',
    total_chapters: 8,
    total_concepts: 16,
    average_mastery: 69
  }
];

interface GradeContextType {
  selectedGrade: number; // 9 | 10 | 11 | 12
  setSelectedGrade: (grade: number) => void;
  grades: Grade[];
  refreshGrades: () => Promise<void>;
  currentGradeMeta: Grade | null;
}

const GradeContext = createContext<GradeContextType | undefined>(undefined);

export const GradeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [selectedGrade, setSelectedGradeState] = useState<number>(() => {
    const saved = localStorage.getItem('learnix_active_grade');
    if (saved) {
      const parsed = parseInt(saved, 10);
      if ([9, 10, 11, 12].includes(parsed)) return parsed;
    }
    return 10;
  });

  const [grades, setGrades] = useState<Grade[]>(DEFAULT_GRADES);

  const setSelectedGrade = (grade: number) => {
    setSelectedGradeState(grade);
    localStorage.setItem('learnix_active_grade', grade.toString());
  };

  const refreshGrades = async () => {
    try {
      const data = await api.getGrades();
      if (Array.isArray(data) && data.length > 0) {
        setGrades(data);
      }
    } catch (e) {
      // Fallback already loaded
    }
  };

  useEffect(() => {
    refreshGrades();
  }, []);

  const currentGradeMeta = grades.find((g) => g.grade === selectedGrade) || DEFAULT_GRADES[1];

  return (
    <GradeContext.Provider
      value={{
        selectedGrade,
        setSelectedGrade,
        grades,
        refreshGrades,
        currentGradeMeta
      }}
    >
      {children}
    </GradeContext.Provider>
  );
};

export const useGrade = (): GradeContextType => {
  const context = useContext(GradeContext);
  if (!context) {
    throw new Error('useGrade must be used within a GradeProvider');
  }
  return context;
};
