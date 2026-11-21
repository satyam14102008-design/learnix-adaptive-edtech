import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { SubjectProvider } from './context/SubjectContext';
import { GradeProvider } from './context/GradeContext';
import { AppLayout } from './layouts/AppLayout';
import { LandingPage } from './pages/LandingPage';
import { LoginPage } from './pages/LoginPage';
import { SignupPage } from './pages/SignupPage';
import { StudentDashboard } from './pages/StudentDashboard';
import { AdaptiveArena } from './pages/AdaptiveArena';
import { ConceptGraphPage } from './pages/ConceptGraphPage';
import { DiagnosticAssessment } from './pages/DiagnosticAssessment';
import { RevisionCenter } from './pages/RevisionCenter';
import { LearningPathPage } from './pages/LearningPathPage';
import { TeacherDashboard } from './pages/TeacherDashboard';

export const App: React.FC = () => {
  return (
    <AuthProvider>
      <GradeProvider>
        <SubjectProvider>
          <BrowserRouter>
            <Routes>
              {/* Public Landing & Auth Routes */}
              <Route path="/" element={<LandingPage />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/signup" element={<SignupPage />} />

              {/* App Workspace Routes wrapped in AppLayout */}
              <Route element={<AppLayout />}>
                <Route path="/dashboard" element={<StudentDashboard />} />
                <Route path="/arena" element={<AdaptiveArena />} />
                <Route path="/concept-graph" element={<ConceptGraphPage />} />
                <Route path="/diagnostic" element={<DiagnosticAssessment />} />
                <Route path="/revision" element={<RevisionCenter />} />
                <Route path="/learning-path" element={<LearningPathPage />} />
                <Route path="/teacher" element={<TeacherDashboard />} />
              </Route>

              {/* Catch-all redirect */}
              <Route path="*" element={<Navigate to="/" replace />} />
            </Routes>
          </BrowserRouter>
        </SubjectProvider>
      </GradeProvider>
    </AuthProvider>
  );
};
