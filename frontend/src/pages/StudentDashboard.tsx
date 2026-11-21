import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Zap,
  Flame,
  ArrowRight,
  AlertTriangle,
  RotateCcw,
  Network,
  Sparkles,
  ChevronRight,
  Award,
  FlaskConical,
  Dna,
  Sigma,
  Layers,
  GraduationCap,
  Target,
  Compass,
  FileCheck2,
  Clock,
  TrendingUp,
  BrainCircuit
} from 'lucide-react';
import { api } from '../services/api';
import { useAuth } from '../context/AuthContext';
import { useSubject } from '../context/SubjectContext';
import { useGrade } from '../context/GradeContext';
import { SubjectBar } from '../components/SubjectBar';
import { GradeSelector } from '../components/GradeSelector';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';
import { AnimatedCounter } from '../components/animations/AnimatedCounter';
import { MasteryRing } from '../components/animations/MasteryRing';
import { AnimatedPage } from '../components/animations/AnimatedPage';

export const StudentDashboard: React.FC = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const { selectedSubject, setSelectedSubject, subjects, currentSubjectMeta } = useSubject();
  const { selectedGrade, currentGradeMeta } = useGrade();
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      setLoading(true);
      try {
        const res = await api.getStudentDashboard({
          grade: selectedGrade,
          subject: selectedSubject !== 'all' ? selectedSubject : undefined,
        });
        setData(res);
      } catch (err) {
        console.warn('Dashboard fetch failed, using fallback display data.');
      } finally {
        setLoading(false);
      }
    }
    loadDashboard();
  }, [selectedGrade, selectedSubject]);

  const overallMastery = data?.stats?.overall_mastery ?? (currentGradeMeta?.average_mastery || 72);
  const streak = data?.student?.streak_days ?? 6;
  const xp = data?.student?.xp ?? 1420;
  const chapters = data?.mastery_by_chapter ?? [];
  const weakConcepts = data?.weak_concepts ?? [];
  const subjectStats = data?.subjects || subjects;

  const getSubjectIcon = (id: string) => {
    switch (id) {
      case 'physics':
        return <Zap className="w-5 h-5 text-cyan-400 fill-cyan-400" />;
      case 'chemistry':
        return <FlaskConical className="w-5 h-5 text-emerald-400 fill-emerald-400" />;
      case 'biology':
        return <Dna className="w-5 h-5 text-rose-400 fill-rose-400" />;
      case 'mathematics':
        return <Sigma className="w-5 h-5 text-amber-400" />;
      default:
        return <Layers className="w-5 h-5 text-indigo-400" />;
    }
  };

  const getSubjectColorStyles = (id: string) => {
    switch (id) {
      case 'physics':
        return {
          glowColor: 'cyan' as const,
          border: 'border-cyan-500/30 hover:border-cyan-400/60',
          badge: 'bg-cyan-950/60 text-cyan-300 border-cyan-800/60',
          gradient: 'from-cyan-500 to-blue-600',
          text: 'text-cyan-400',
          bgLight: 'bg-cyan-950/40',
        };
      case 'chemistry':
        return {
          glowColor: 'emerald' as const,
          border: 'border-emerald-500/30 hover:border-emerald-400/60',
          badge: 'bg-emerald-950/60 text-emerald-300 border-emerald-800/60',
          gradient: 'from-emerald-500 to-teal-600',
          text: 'text-emerald-400',
          bgLight: 'bg-emerald-950/40',
        };
      case 'biology':
        return {
          glowColor: 'rose' as const,
          border: 'border-rose-500/30 hover:border-rose-400/60',
          badge: 'bg-rose-950/60 text-rose-300 border-rose-800/60',
          gradient: 'from-rose-500 to-pink-600',
          text: 'text-rose-400',
          bgLight: 'bg-rose-950/40',
        };
      case 'mathematics':
        return {
          glowColor: 'amber' as const,
          border: 'border-amber-500/30 hover:border-amber-400/60',
          badge: 'bg-amber-950/60 text-amber-300 border-amber-800/60',
          gradient: 'from-amber-500 to-orange-600',
          text: 'text-amber-400',
          bgLight: 'bg-amber-950/40',
        };
      default:
        return {
          glowColor: 'blue' as const,
          border: 'border-blue-500/30 hover:border-blue-400/60',
          badge: 'bg-blue-950/60 text-blue-300 border-blue-800/60',
          gradient: 'from-blue-600 to-violet-600',
          text: 'text-blue-400',
          bgLight: 'bg-blue-950/40',
        };
    }
  };

  return (
    <AnimatedPage className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6 font-sans">
      {/* Dynamic Controls Capsule: Grade & Subject Selectors */}
      <motion.div
        initial={{ opacity: 0, y: -12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.35 }}
        className="flex flex-col lg:flex-row lg:items-center justify-between gap-3 bg-slate-900/70 p-3.5 rounded-3xl border border-white/10 shadow-glass-card backdrop-blur-2xl"
      >
        <div className="flex items-center gap-2.5 px-1.5">
          <div className="w-8 h-8 rounded-xl bg-cyan-950/80 border border-cyan-800/60 flex items-center justify-center text-cyan-400 shadow-glow-sm">
            <GraduationCap className="w-4 h-4" />
          </div>
          <div className="flex flex-col">
            <span className="text-[10px] font-mono font-bold text-cyan-400 uppercase tracking-wider">
              Academic Track
            </span>
            <span className="text-xs text-slate-300 font-bold">
              {currentGradeMeta?.name || 'Class 10'} · {selectedSubject === 'all' ? 'All Subjects' : currentSubjectMeta?.name}
            </span>
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2.5">
          <GradeSelector />
          <SubjectBar />
        </div>
      </motion.div>

      {/* Futuristic Command Center Hero Card */}
      <AnimatedCard
        spotlight={true}
        glowColor="cyan"
        className="p-6 sm:p-8 border-white/10 bg-gradient-to-br from-slate-950/90 via-[#070c18]/90 to-slate-900/80 shadow-glass-card-hover"
      >
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-8">
          {/* Left Column: Greeting, Grade Focus & Description */}
          <div className="space-y-3.5 max-w-xl">
            <div className="flex flex-wrap items-center gap-2">
              <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-black text-white bg-gradient-to-r ${currentGradeMeta?.color || 'from-cyan-500 to-blue-600'} shadow-glow-sm`}>
                <Sparkles className="w-3.5 h-3.5 animate-spin [animation-duration:4s]" />
                <span>{currentGradeMeta?.name}</span>
                <span>·</span>
                <span>{currentGradeMeta?.badge}</span>
              </span>

              <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold text-slate-300 px-2.5 py-0.5 rounded-full bg-white/[0.06] border border-white/10">
                <Target className="w-3 h-3 text-cyan-400" />
                <span>{currentGradeMeta?.exam_focus}</span>
              </span>
            </div>

            <h1 className="text-2xl sm:text-3xl md:text-4xl font-black text-white tracking-tight">
              Welcome back, {user?.name || 'Alex'}!
            </h1>

            <p className="text-sm text-slate-300 font-medium leading-relaxed">
              {currentGradeMeta?.description}. Continuous BKT learner model reflects an overall readiness of{' '}
              <strong className="text-cyan-400 font-extrabold">{overallMastery}%</strong>.
            </p>

            {/* Quick Metrics Bar */}
            <div className="pt-2 flex flex-wrap items-center gap-4 text-xs font-mono font-bold text-slate-400">
              <div className="flex items-center gap-1.5 text-amber-300 bg-amber-950/40 border border-amber-800/50 px-2.5 py-1 rounded-lg">
                <Flame className="w-3.5 h-3.5 fill-amber-400 text-amber-400" />
                <span><AnimatedCounter value={streak} /> Day Streak</span>
              </div>
              <div className="flex items-center gap-1.5 text-cyan-300 bg-cyan-950/40 border border-cyan-800/50 px-2.5 py-1 rounded-lg">
                <Zap className="w-3.5 h-3.5 text-cyan-400 fill-cyan-400" />
                <span><AnimatedCounter value={xp} /> XP</span>
              </div>
              <div className="flex items-center gap-1.5 text-emerald-300 bg-emerald-950/40 border border-emerald-800/50 px-2.5 py-1 rounded-lg">
                <Award className="w-3.5 h-3.5 text-emerald-400" />
                <span><AnimatedCounter value={chapters.length} /> Active Chapters</span>
              </div>
            </div>
          </div>

          {/* Right Column: Mastery Ring & Direct Launch CTA */}
          <div className="flex sm:flex-row lg:flex-col items-center justify-between sm:justify-end lg:justify-center gap-6 shrink-0">
            <div className="flex items-center gap-4">
              <MasteryRing
                percentage={overallMastery}
                size={104}
                strokeWidth={9}
                label="Mastery"
                colorScheme="cyan"
              />
              <div className="hidden sm:block text-left">
                <div className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider">
                  Target Status
                </div>
                <div className="text-sm font-extrabold text-white mt-0.5">
                  {overallMastery >= 80 ? 'Exam Ready' : overallMastery >= 60 ? 'Advancing Well' : 'Building Foundations'}
                </div>
                <div className="text-[11px] text-cyan-400 font-mono mt-0.5">
                  Top 8% in Cohort
                </div>
              </div>
            </div>

            <GlowButton
              variant="electric"
              size="lg"
              onClick={() => navigate(selectedSubject !== 'all' ? `/arena?grade=${selectedGrade}&subject_id=${selectedSubject}` : `/arena?grade=${selectedGrade}`)}
              icon={Zap}
              className="w-full sm:w-auto"
            >
              <span>
                {selectedSubject === 'all'
                  ? `Practice ${currentGradeMeta?.name}`
                  : `Practice ${selectedSubject.charAt(0).toUpperCase() + selectedSubject.slice(1)}`}
              </span>
              <ArrowRight className="w-4 h-4 ml-1" />
            </GlowButton>
          </div>
        </div>
      </AnimatedCard>

      {/* 4 STEM Subject Cards */}
      <div>
        <div className="flex items-center justify-between mb-3.5">
          <div className="flex items-center gap-2">
            <TrendingUp className="w-4 h-4 text-cyan-400" />
            <h2 className="text-base font-extrabold text-white">
              {currentGradeMeta?.name} Subject Tracks
            </h2>
          </div>
          <span className="text-xs text-slate-400 font-medium">Click any subject to filter chapters</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {subjectStats.map((subj: any) => {
            const styles = getSubjectColorStyles(subj.id);
            const isSelected = selectedSubject === subj.id;
            const mastery = Math.round(subj.average_mastery || 70);

            return (
              <AnimatedCard
                key={subj.id}
                spotlight={true}
                glowColor={styles.glowColor}
                onClick={() => setSelectedSubject(subj.id === selectedSubject ? 'all' : subj.id)}
                className={`p-5 flex flex-col justify-between ${
                  isSelected ? 'border-cyan-400 ring-2 ring-cyan-400/30 shadow-glow-cyan' : ''
                }`}
              >
                <div>
                  {/* Subject top bar */}
                  <div className="flex items-start justify-between mb-3">
                    <div className={`w-11 h-11 rounded-2xl ${styles.bgLight} border border-white/10 flex items-center justify-center shadow-xs`}>
                      {getSubjectIcon(subj.id)}
                    </div>
                    <div className="text-right">
                      <span className={`text-xl font-extrabold font-mono ${styles.text}`}>
                        <AnimatedCounter value={mastery} suffix="%" />
                      </span>
                      <div className="text-[10px] text-slate-400 font-bold uppercase tracking-wider">
                        Mastery
                      </div>
                    </div>
                  </div>

                  <h3 className="text-base font-extrabold text-white">{subj.name}</h3>
                  <p className="text-xs text-slate-400 mt-0.5 line-clamp-1">{subj.tagline}</p>

                  {/* Progress bar */}
                  <div className="w-full bg-slate-900 h-2 rounded-full mt-3.5 overflow-hidden p-0.5 border border-white/[0.08]">
                    <motion.div
                      initial={{ width: 0 }}
                      animate={{ width: `${mastery}%` }}
                      transition={{ duration: 1 }}
                      className={`h-full rounded-full bg-gradient-to-r ${styles.gradient}`}
                    />
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-white/[0.06] flex items-center justify-between text-xs">
                  <span className="text-[11px] text-slate-400 font-mono font-bold">
                    {subj.total_chapters || 4} Chapters
                  </span>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      navigate(`/arena?grade=${selectedGrade}&subject_id=${subj.id}`);
                    }}
                    className={`font-bold font-mono text-xs flex items-center gap-1 ${styles.text} hover:underline`}
                  >
                    Practice <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </AnimatedCard>
            );
          })}
        </div>
      </div>

      {/* 3 Quick Action Navigation Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-3.5">
        <AnimatedCard
          onClick={() => navigate(selectedSubject !== 'all' ? `/arena?grade=${selectedGrade}&subject_id=${selectedSubject}` : `/arena?grade=${selectedGrade}`)}
          glowColor="cyan"
          className="p-4"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-cyan-950/60 border border-cyan-800/60 flex items-center justify-center text-cyan-400 shrink-0 shadow-glow-sm">
                <Zap className="w-5 h-5 fill-cyan-400" />
              </div>
              <div>
                <div className="text-sm font-extrabold text-white">Adaptive Arena</div>
                <div className="text-[11px] text-slate-400 font-medium">Class {selectedGrade} Real-Time Challenges</div>
              </div>
            </div>
            <ChevronRight className="w-4 h-4 text-slate-500" />
          </div>
        </AnimatedCard>

        <AnimatedCard
          onClick={() => navigate(selectedSubject !== 'all' ? `/concept-graph?grade=${selectedGrade}&subject_id=${selectedSubject}` : `/concept-graph?grade=${selectedGrade}`)}
          glowColor="violet"
          className="p-4"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-violet-950/60 border border-violet-800/60 flex items-center justify-center text-violet-400 shrink-0 shadow-glow-violet">
                <Network className="w-5 h-5" />
              </div>
              <div>
                <div className="text-sm font-extrabold text-white">Knowledge Graph</div>
                <div className="text-[11px] text-slate-400 font-medium">Prerequisites & Mastery Nodes</div>
              </div>
            </div>
            <ChevronRight className="w-4 h-4 text-slate-500" />
          </div>
        </AnimatedCard>

        <AnimatedCard
          onClick={() => navigate('/revision')}
          glowColor="amber"
          className="p-4"
        >
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-amber-950/60 border border-amber-800/60 flex items-center justify-center text-amber-400 shrink-0 shadow-glow-amber">
                <RotateCcw className="w-5 h-5" />
              </div>
              <div>
                <div className="text-sm font-extrabold text-white">Spaced Review</div>
                <div className="text-[11px] text-amber-400 font-bold font-mono">3 SM-2 Concepts Due</div>
              </div>
            </div>
            <ChevronRight className="w-4 h-4 text-slate-500" />
          </div>
        </AnimatedCard>
      </div>

      {/* Suggested Focus: Weak Concepts & Misconception Alert Radar */}
      {weakConcepts.length > 0 && (
        <AnimatedCard glowColor="amber" className="p-5 sm:p-6 border-amber-500/30 bg-amber-950/20">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2 text-sm font-extrabold text-white">
              <AlertTriangle className="w-4 h-4 text-amber-400 animate-pulse" />
              <span>Priority Mastery Remediations ({currentGradeMeta?.name})</span>
            </div>
            <span className="text-xs font-mono font-bold text-amber-400">Target Gaps</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            {weakConcepts.slice(0, 3).map((item: any) => (
              <div
                key={item.concept_id}
                className="p-4 rounded-2xl bg-slate-900/80 border border-white/10 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded-md bg-white/[0.06] text-cyan-300 border border-white/10">
                      {item.subject_id || 'STEM'}
                    </span>
                    <span className="text-xs text-amber-400 font-bold font-mono">
                      {item.mastery_score}%
                    </span>
                  </div>
                  <div className="text-sm font-extrabold text-white mt-2 leading-snug">
                    {item.concept_name}
                  </div>
                </div>

                <div className="mt-4 flex justify-end">
                  <GlowButton
                    variant="electric"
                    size="sm"
                    onClick={() => navigate(`/arena?grade=${selectedGrade}&concept_id=${item.concept_id}`)}
                  >
                    Remediate Now
                  </GlowButton>
                </div>
              </div>
            ))}
          </div>
        </AnimatedCard>
      )}

      {/* Chapter Progress Cards Grid */}
      <div>
        <div className="flex items-center justify-between mb-3.5">
          <div className="flex items-center gap-2">
            <h2 className="text-base font-extrabold text-white">
              {currentGradeMeta?.name}{' '}
              {selectedSubject === 'all'
                ? 'Curriculum Chapters'
                : `${selectedSubject.charAt(0).toUpperCase() + selectedSubject.slice(1)} Chapters`}
            </h2>
            <span className="text-xs text-slate-400 font-mono font-bold">
              ({chapters.length} chapters)
            </span>
          </div>
          <button
            onClick={() => navigate(selectedSubject !== 'all' ? `/concept-graph?grade=${selectedGrade}&subject_id=${selectedSubject}` : `/concept-graph?grade=${selectedGrade}`)}
            className="text-xs font-bold text-cyan-400 hover:text-cyan-300 flex items-center gap-0.5 transition-colors"
          >
            Explore on Knowledge Map <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
          {chapters.map((ch: any, idx: number) => {
            const chSubject = ch.subject_id || 'physics';
            const chStyles = getSubjectColorStyles(chSubject);

            return (
              <AnimatedCard
                key={ch.chapter_id || ch.id}
                spotlight={true}
                glowColor={chStyles.glowColor}
                onClick={() => navigate(`/arena?grade=${selectedGrade}&chapter_id=${ch.chapter_id || ch.id}`)}
                className="p-4 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <span className={`text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded-md ${chStyles.badge}`}>
                        {ch.subject_name || chSubject}
                      </span>
                      <span className="text-[10px] font-mono text-slate-400 font-bold">
                        {currentGradeMeta?.name}
                      </span>
                    </div>
                    <span className={`text-xs font-extrabold font-mono ${chStyles.text}`}>
                      {ch.average_mastery}%
                    </span>
                  </div>

                  <div className="text-sm font-extrabold text-white mt-2 truncate">
                    {ch.title}
                  </div>

                  {/* Animated Progress Bar */}
                  <div className="w-full bg-slate-900 h-2 rounded-full mt-3 overflow-hidden p-0.5 border border-white/[0.08]">
                    <motion.div
                      initial={{ width: 0 }}
                      animate={{ width: `${ch.average_mastery}%` }}
                      transition={{ duration: 0.8, delay: idx * 0.04 }}
                      className={`bg-gradient-to-r ${chStyles.gradient} h-full rounded-full`}
                    />
                  </div>
                </div>

                <div className="flex items-center justify-between text-[11px] text-slate-400 mt-3 pt-2.5 border-t border-white/[0.06] font-medium">
                  <span>{ch.mastered_concepts || 0} / {ch.total_concepts || 2} Mastered</span>
                  <span className={`${chStyles.text} font-bold font-mono flex items-center gap-0.5`}>
                    Practice &rarr;
                  </span>
                </div>
              </AnimatedCard>
            );
          })}
        </div>
      </div>
    </AnimatedPage>
  );
};
