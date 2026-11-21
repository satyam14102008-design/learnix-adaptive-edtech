import React, { useState } from 'react';
import { Outlet, NavLink, useLocation, useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Zap,
  LayoutDashboard,
  BrainCircuit,
  Network,
  FileCheck2,
  RotateCcw,
  Milestone,
  GraduationCap,
  Menu,
  X,
  Flame,
  LogOut,
  Sparkles,
  ChevronRight
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useSubject } from '../context/SubjectContext';
import { useGrade } from '../context/GradeContext';
import { SubjectBar } from '../components/SubjectBar';
import { GradeSelector } from '../components/GradeSelector';
import { CosmicBackground } from '../components/animations/CosmicBackground';
import { AnimatedCounter } from '../components/animations/AnimatedCounter';

interface NavItem {
  to: string;
  label: string;
  icon: any;
  badge?: string;
  count?: string;
}

export const AppLayout: React.FC = () => {
  const { user, logout, demoLogin } = useAuth();
  const { selectedSubject, currentSubjectMeta } = useSubject();
  const { selectedGrade, currentGradeMeta } = useGrade();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  const isTeacher = user?.role === 'teacher';

  const studentNavItems: NavItem[] = [
    { to: '/dashboard', label: 'Command Center', icon: LayoutDashboard },
    { to: '/arena', label: 'Adaptive Practice', icon: Zap, badge: 'AI Adaptive' },
    { to: '/concept-graph', label: 'Knowledge Graph', icon: Network },
    { to: '/diagnostic', label: 'Diagnostic Assessment', icon: FileCheck2 },
    { to: '/revision', label: 'Spaced Revision', icon: RotateCcw, count: '3' },
    { to: '/learning-path', label: 'Mastery Roadmap', icon: Milestone },
  ];

  const teacherNavItems: NavItem[] = [
    { to: '/teacher', label: 'Cohort Analytics', icon: GraduationCap },
    { to: '/concept-graph', label: 'Curriculum Graph', icon: Network },
    { to: '/arena', label: 'Arena Preview', icon: Zap },
  ];

  const navItems = isTeacher ? teacherNavItems : studentNavItems;

  const handleRoleToggle = async () => {
    if (isTeacher) {
      await demoLogin('student');
      navigate('/dashboard');
    } else {
      await demoLogin('teacher');
      navigate('/teacher');
    }
  };

  return (
    <div className="flex h-screen bg-[#030712] text-slate-100 overflow-hidden font-sans relative selection:bg-cyan-500/20 selection:text-cyan-300">
      {/* Ambient Cosmic Background with subtle grid & luminous glows */}
      <CosmicBackground />

      {/* Desktop Sidebar */}
      <aside className="hidden md:flex flex-col w-64 border-r border-white/[0.08] bg-[#070c18]/85 backdrop-blur-2xl shrink-0 z-20 shadow-glass-card">
        {/* Brand Header */}
        <div className="h-16 flex items-center px-6 border-b border-white/[0.08] gap-3">
          <motion.div
            whileHover={{ rotate: 12, scale: 1.08 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => navigate('/dashboard')}
            className="w-9 h-9 rounded-xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-violet-600 flex items-center justify-center shadow-glow-cyan text-white cursor-pointer"
          >
            <Zap className="w-5 h-5 fill-white" />
          </motion.div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-extrabold text-base tracking-tight text-white">
                Learnix
              </span>
              <span className="text-[10px] font-black font-mono px-1.5 py-0.5 rounded-md bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-glow-sm">
                AI
              </span>
            </div>
            <div className="text-[10px] text-cyan-400 font-mono tracking-wider uppercase font-bold flex items-center gap-1 mt-0.5">
              <span>{currentGradeMeta?.name || 'Class 10'}</span>
              <span className="text-slate-600">·</span>
              <span className="capitalize text-slate-300">
                {selectedSubject === 'all' ? 'All Subjects' : currentSubjectMeta?.name || 'STEM'}
              </span>
            </div>
          </div>
        </div>

        {/* Navigation Links */}
        <div className="flex-1 px-3 py-6 space-y-1.5 overflow-y-auto no-scrollbar">
          <div className="px-3 pb-2 text-[10px] font-mono font-bold tracking-wider text-slate-500 uppercase">
            {isTeacher ? 'Instructor Portal' : 'Learner Navigation'}
          </div>

          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.to;
            return (
              <NavLink
                key={item.to}
                to={item.to}
                className={({ isActive: isCurrent }) => `
                  group relative flex items-center justify-between px-3.5 py-2.5 rounded-xl text-xs md:text-sm font-semibold transition-all duration-200 outline-none
                  ${isCurrent
                    ? 'text-white'
                    : 'text-slate-400 hover:text-white hover:bg-white/[0.04]'
                  }
                `}
              >
                {/* Active Indicator Sliding Background */}
                {isActive && (
                  <motion.div
                    layoutId="activeNavIndicator"
                    className="absolute inset-0 rounded-xl bg-gradient-to-r from-blue-600/80 via-indigo-600/80 to-cyan-500/80 border border-cyan-400/30 shadow-glow-blue"
                    transition={{ type: 'spring', stiffness: 500, damping: 35 }}
                  >
                    <div className="absolute inset-x-0 top-0 h-1/2 bg-white/15 rounded-t-xl" />
                  </motion.div>
                )}

                <div className="relative z-10 flex items-center gap-3">
                  <Icon
                    className={`w-4 h-4 transition-transform duration-200 group-hover:scale-115 ${
                      isActive ? 'text-cyan-200' : 'text-slate-500 group-hover:text-cyan-400'
                    }`}
                  />
                  <span>{item.label}</span>
                </div>

                <div className="relative z-10 flex items-center gap-1.5">
                  {item.badge && (
                    <span
                      className={`px-2 py-0.5 text-[9px] font-mono font-bold rounded-full flex items-center gap-1 ${
                        isActive
                          ? 'bg-white/20 text-white border border-white/30'
                          : 'bg-cyan-950/80 text-cyan-400 border border-cyan-800/60 shadow-glow-sm'
                      }`}
                    >
                      <Sparkles className="w-2.5 h-2.5 animate-spin [animation-duration:4s]" />
                      {item.badge}
                    </span>
                  )}
                  {item.count && (
                    <span
                      className={`px-1.5 py-0.5 text-[10px] font-mono font-extrabold rounded-md ${
                        isActive
                          ? 'bg-amber-400 text-slate-950'
                          : 'bg-amber-950/80 text-amber-300 border border-amber-800/80 shadow-glow-amber'
                      }`}
                    >
                      {item.count}
                    </span>
                  )}
                </div>
              </NavLink>
            );
          })}
        </div>

        {/* Demo Switcher & User Profile */}
        <div className="p-3 border-t border-white/[0.08] space-y-2 bg-slate-950/40">
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.97 }}
            onClick={handleRoleToggle}
            className="w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-bold bg-white/[0.04] hover:bg-white/[0.08] border border-white/10 text-slate-300 hover:text-white transition-all shadow-sm"
          >
            <span className="flex items-center gap-2">
              <BrainCircuit className="w-3.5 h-3.5 text-cyan-400 animate-pulse" />
              {isTeacher ? 'Switch to Student' : 'Switch to Teacher'}
            </span>
            <ChevronRight className="w-3.5 h-3.5 text-slate-500 group-hover:translate-x-1 transition-transform" />
          </motion.button>

          <div className="flex items-center justify-between px-2 pt-1">
            <div className="flex items-center gap-2.5">
              <motion.img
                whileHover={{ rotate: 10, scale: 1.1 }}
                src={user?.avatar || 'https://api.dicebear.com/7.x/bottts/svg?seed=Alex'}
                alt="Avatar"
                className="w-8 h-8 rounded-lg border border-cyan-500/40 bg-cyan-950/50 shadow-glow-sm"
              />
              <div className="leading-tight">
                <div className="text-xs font-bold text-slate-200 truncate max-w-[100px]">
                  {user?.name || 'Alex Chen'}
                </div>
                <div className="text-[10px] text-cyan-400 font-mono capitalize font-bold">
                  {user?.role || 'student'}
                </div>
              </div>
            </div>
            <motion.button
              whileHover={{ scale: 1.15, rotate: -8 }}
              whileTap={{ scale: 0.9 }}
              onClick={logout}
              title="Sign Out"
              className="p-1.5 rounded-lg text-slate-400 hover:text-rose-400 hover:bg-rose-950/40 border border-transparent hover:border-rose-800/40 transition-colors"
            >
              <LogOut className="w-4 h-4" />
            </motion.button>
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden z-10">
        {/* Top Header */}
        <header className="h-16 border-b border-white/[0.08] bg-[#070c18]/80 backdrop-blur-xl flex items-center justify-between px-4 md:px-8 shrink-0 gap-4">
          <div className="flex items-center gap-3 shrink-0">
            <button
              onClick={() => setMobileMenuOpen(true)}
              className="md:hidden p-2 rounded-lg text-slate-400 hover:text-white hover:bg-white/[0.06] border border-white/10"
            >
              <Menu className="w-5 h-5" />
            </button>
            <div className="flex items-center gap-2 text-xs md:text-sm">
              <span className="px-2.5 py-1 rounded-lg bg-cyan-950/60 border border-cyan-800/60 text-cyan-300 font-bold font-mono text-[11px] shadow-glow-sm">
                {currentGradeMeta?.name || 'Class 10'}
              </span>
              <span className="text-slate-600 hidden sm:inline">/</span>
              <span className="text-slate-300 font-bold hidden sm:inline">
                {selectedSubject === 'all' ? 'All Subjects' : currentSubjectMeta?.name || 'STEM'}
              </span>
            </div>
          </div>

          {/* Quick Grade & Subject Bar in Header */}
          <div className="hidden lg:flex items-center gap-2.5">
            <GradeSelector compact={true} />
            <SubjectBar compact={true} />
          </div>

          <div className="flex items-center gap-2.5 md:gap-3.5 shrink-0">
            {/* Streak Indicator */}
            {!isTeacher && (
              <motion.div
                whileHover={{ scale: 1.05 }}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-amber-950/50 border border-amber-800/60 text-amber-300 text-xs font-bold font-mono shadow-glow-amber"
              >
                <Flame className="w-3.5 h-3.5 fill-amber-400 text-amber-400 animate-wiggle" />
                <span>
                  <AnimatedCounter value={user?.streak_days || 6} suffix="d" /> Streak
                </span>
              </motion.div>
            )}

            {/* XP Pill */}
            {!isTeacher && (
              <motion.div
                whileHover={{ scale: 1.05 }}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-blue-950/50 border border-blue-800/60 text-blue-300 text-xs font-bold font-mono shadow-glow-blue"
              >
                <Zap className="w-3.5 h-3.5 text-cyan-400 fill-cyan-400 animate-pulse" />
                <span>
                  <AnimatedCounter value={user?.xp || 1420} suffix=" XP" />
                </span>
              </motion.div>
            )}

            {/* Quick Practice Action */}
            {!isTeacher && (
              <motion.div whileHover={{ scale: 1.04, y: -1 }} whileTap={{ scale: 0.96 }}>
                <NavLink
                  to="/arena"
                  className="hidden sm:flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-extrabold bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white shadow-glow-cyan border border-cyan-400/40 transition-all"
                >
                  <Zap className="w-3.5 h-3.5 fill-white" />
                  Practice Now
                </NavLink>
              </motion.div>
            )}
          </div>
        </header>

        {/* Page Body */}
        <main className="flex-1 overflow-y-auto bg-transparent relative no-scrollbar">
          <Outlet />
        </main>
      </div>

      {/* Mobile Menu Drawer */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <div className="fixed inset-0 z-50 md:hidden flex">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 bg-slate-950/80 backdrop-blur-md"
              onClick={() => setMobileMenuOpen(false)}
            />
            <motion.div
              initial={{ x: -300 }}
              animate={{ x: 0 }}
              exit={{ x: -300 }}
              transition={{ type: 'spring', damping: 25, stiffness: 300 }}
              className="relative w-76 bg-slate-950 border-r border-white/10 flex flex-col z-10 p-5 shadow-2xl"
            >
              <div className="flex items-center justify-between pb-4 border-b border-white/10">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-white">
                    <Zap className="w-4 h-4 fill-white" />
                  </div>
                  <span className="font-extrabold text-lg text-white">Learnix AI</span>
                </div>
                <button
                  onClick={() => setMobileMenuOpen(false)}
                  className="p-1 rounded-lg text-slate-400 hover:text-white"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <div className="flex-1 py-4 space-y-4 overflow-y-auto">
                <div className="space-y-1.5">
                  <div className="text-[10px] font-mono font-bold text-slate-500 uppercase tracking-wider px-1">
                    Select Grade
                  </div>
                  <GradeSelector compact={true} />
                </div>
                <div className="space-y-1.5">
                  <div className="text-[10px] font-mono font-bold text-slate-500 uppercase tracking-wider px-1">
                    Select Subject
                  </div>
                  <SubjectBar compact={true} />
                </div>
                <div className="pt-3 border-t border-white/[0.08] space-y-1">
                  {navItems.map((item) => (
                    <NavLink
                      key={item.to}
                      to={item.to}
                      onClick={() => setMobileMenuOpen(false)}
                      className="flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-sm font-semibold text-slate-300 hover:bg-white/[0.06] hover:text-white transition-colors"
                    >
                      <item.icon className="w-4 h-4 text-cyan-400" />
                      <span>{item.label}</span>
                    </NavLink>
                  ))}
                </div>
              </div>

              <button
                onClick={() => {
                  handleRoleToggle();
                  setMobileMenuOpen(false);
                }}
                className="w-full py-2.5 rounded-xl text-xs font-bold bg-white/[0.06] border border-white/10 text-cyan-300 hover:bg-white/[0.1]"
              >
                {isTeacher ? 'Switch to Student View' : 'Switch to Teacher View'}
              </button>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </div>
  );
};
