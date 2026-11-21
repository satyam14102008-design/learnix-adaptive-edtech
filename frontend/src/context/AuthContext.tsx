import React, { createContext, useContext, useState, useEffect } from 'react';
import { User } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: User | null;
  token: string | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string, name: string, role?: string, grade?: string) => Promise<void>;
  demoLogin: (role: 'student' | 'teacher') => Promise<void>;
  logout: () => void;
  setUser: React.Dispatch<React.SetStateAction<User | null>>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(localStorage.getItem('learnix_token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function initAuth() {
      if (token) {
        try {
          const profile = await api.getMe();
          setUser(profile);
        } catch (e) {
          console.warn('[Learnix Auth] Failed to restore session from token, clearing.');
          localStorage.removeItem('learnix_token');
          setToken(null);
          // Set default demo student so app is never in a broken blank state
          setDemoDefault();
        }
      } else {
        setDemoDefault();
      }
      setLoading(false);
    }
    initAuth();
  }, [token]);

  const setDemoDefault = () => {
    setUser({
      _id: 'student_alex_chen',
      id: 'student_alex_chen',
      name: 'Alex Chen',
      email: 'student@learnix.ai',
      role: 'student',
      grade: 'Class 10',
      avatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=Alex',
      xp: 1420,
      level: 4,
      level_title: 'Quantum Apprentice',
      streak_days: 6,
      daily_goal: 5,
      daily_completed: 3,
      total_study_minutes: 240
    });
  };

  const login = async (email: string, password: string) => {
    const res = await api.login({ email, password });
    localStorage.setItem('learnix_token', res.token);
    setToken(res.token);
    setUser(res.user);
  };

  const signup = async (email: string, password: string, name: string, role: string = 'student', grade: string = 'Class 10') => {
    const res = await api.signup({ email, password, name, role, grade });
    localStorage.setItem('learnix_token', res.token);
    setToken(res.token);
    setUser(res.user);
  };

  const demoLogin = async (role: 'student' | 'teacher') => {
    try {
      const res = await api.demoLogin(role);
      localStorage.setItem('learnix_token', res.token);
      setToken(res.token);
      setUser(res.user);
    } catch (e) {
      // Fallback local mock state
      if (role === 'teacher') {
        setUser({
          _id: 'teacher_sarah_jenkins',
          id: 'teacher_sarah_jenkins',
          name: 'Dr. Sarah Jenkins',
          email: 'teacher@learnix.ai',
          role: 'teacher',
          avatar: 'https://api.dicebear.com/7.x/bottts/svg?seed=Sarah'
        });
      } else {
        setDemoDefault();
      }
    }
  };

  const logout = () => {
    localStorage.removeItem('learnix_token');
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, loading, login, signup, demoLogin, logout, setUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within an AuthProvider');
  return ctx;
};
