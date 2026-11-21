import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import confetti from 'canvas-confetti';
import {
  Zap,
  BrainCircuit,
  ShieldAlert,
  CheckCircle2,
  XCircle,
  ArrowRight,
  Lightbulb,
  Clock,
  Sparkles,
  BookOpen,
  Filter,
  Check,
  RotateCcw,
  Award
} from 'lucide-react';
import { api } from '../services/api';
import { AdaptiveQuestion, SubmissionResponse, Chapter } from '../types';
import { useAuth } from '../context/AuthContext';
import { useSubject } from '../context/SubjectContext';
import { useGrade } from '../context/GradeContext';
import { SubjectBar } from '../components/SubjectBar';
import { GradeSelector } from '../components/GradeSelector';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';
import { LoadingState } from '../components/animations/LoadingState';
import { AnimatedPage } from '../components/animations/AnimatedPage';
import { MasteryRing } from '../components/animations/MasteryRing';

export const AdaptiveArena: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const { user, setUser } = useAuth();
  const { selectedSubject, setSelectedSubject, currentSubjectMeta } = useSubject();
  const { selectedGrade, currentGradeMeta } = useGrade();

  const [question, setQuestion] = useState<AdaptiveQuestion | null>(null);
  const [selectedOption, setSelectedOption] = useState<string | null>(null);
  const [reasoning, setReasoning] = useState<string>('');
  const [showHint, setShowHint] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);
  const [submitting, setSubmitting] = useState<boolean>(false);
  const [result, setResult] = useState<SubmissionResponse | null>(null);
  const [timerSeconds, setTimerSeconds] = useState<number>(0);
  const [chapters, setChapters] = useState<Chapter[]>([]);

  const selectedChapter = searchParams.get('chapter_id') || '';

  // Synchronize URL subject_id if present
  useEffect(() => {
    const urlSubj = searchParams.get('subject_id');
    if (urlSubj && urlSubj !== selectedSubject) {
      setSelectedSubject(urlSubj);
    }
  }, [searchParams]);

  // Load chapters for dropdown
  useEffect(() => {
    async function loadChapters() {
      try {
        const res = await api.getConceptGraph({
          grade: selectedGrade,
          subject_id: selectedSubject !== 'all' ? selectedSubject : undefined,
        });
        setChapters(res.chapters || []);
      } catch (e) {
        // fallback
      }
    }
    loadChapters();
  }, [selectedGrade, selectedSubject]);

  useEffect(() => {
    fetchNextQuestion();
  }, [searchParams, selectedGrade, selectedSubject]);

  useEffect(() => {
    if (result) return;
    const interval = setInterval(() => {
      setTimerSeconds((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(interval);
  }, [result]);

  // Keyboard shortcut listener for options (A, B, C, D)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (result || submitting || !question) return;
      const key = e.key.toUpperCase();
      if (['A', 'B', 'C', 'D'].includes(key)) {
        const exists = question.options.some((o) => o.id === key);
        if (exists) {
          setSelectedOption(key);
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [question, result, submitting]);

  const fetchNextQuestion = async () => {
    setLoading(true);
    setResult(null);
    setSelectedOption(null);
    setReasoning('');
    setShowHint(false);
    setTimerSeconds(0);

    const activeSubj = searchParams.get('subject_id') || (selectedSubject !== 'all' ? selectedSubject : undefined);

    try {
      const q = await api.getNextQuestion({
        grade: selectedGrade,
        subject_id: activeSubj,
        chapter_id: searchParams.get('chapter_id') || undefined,
        concept_id: searchParams.get('concept_id') || undefined,
      });
      setQuestion(q);
    } catch (err) {
      console.error('Failed to fetch adaptive question:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async () => {
    if (!question || !selectedOption) return;
    setSubmitting(true);

    try {
      const res = await api.submitAnswer({
        question_id: question.id,
        concept_id: question.concept_id,
        selected_option: selectedOption,
        student_reasoning: reasoning,
        response_time_seconds: timerSeconds,
      });

      setResult(res);

      if (res.is_correct && res.mastery_update.new_mastery >= 70) {
        confetti({
          particleCount: 80,
          spread: 70,
          origin: { y: 0.6 },
          colors: ['#38bdf8', '#818cf8', '#34d399', '#f472b6'],
        });
      }

      if (user) {
        setUser({
          ...user,
          xp: (user.xp || 1420) + res.xp_awarded,
          streak_days: res.streak_days,
        });
      }
    } catch (err) {
      console.error('Failed to submit answer:', err);
    } finally {
      setSubmitting(false);
    }
  };

  const handleFilterChange = (ch: string) => {
    const params = new URLSearchParams(searchParams);
    if (ch) {
      params.set('chapter_id', ch);
    } else {
      params.delete('chapter_id');
    }
    params.delete('concept_id');
    setSearchParams(params);
  };

  const getDifficultyStyles = (diff: string) => {
    switch (diff) {
      case 'easy':
        return 'bg-emerald-950/70 text-emerald-300 border-emerald-800/60 shadow-glow-emerald';
      case 'medium':
        return 'bg-cyan-950/70 text-cyan-300 border-cyan-800/60 shadow-glow-cyan';
      case 'hard':
        return 'bg-amber-950/70 text-amber-300 border-amber-800/60 shadow-glow-amber';
      default:
        return 'bg-violet-950/70 text-violet-300 border-violet-800/60 shadow-glow-violet';
    }
  };

  return (
    <AnimatedPage className="p-4 sm:p-8 max-w-4xl mx-auto space-y-6 font-sans">
      {/* Top Filter and Topic Bar */}
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-panel-dark p-4 rounded-3xl border border-white/10 flex flex-col md:flex-row md:items-center justify-between gap-3.5 shadow-glass-card"
      >
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-xl bg-cyan-950/80 border border-cyan-800/60 flex items-center justify-center text-cyan-400 shadow-glow-sm">
            <Zap className="w-4 h-4 fill-cyan-400" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-sm font-extrabold text-white">Adaptive Arena</span>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-cyan-950 text-cyan-300 border border-cyan-800/60 font-bold">
                Level Adaptive
              </span>
            </div>
            <div className="text-[11px] text-slate-400 font-medium">Auto-calibrating to your cognitive zone</div>
          </div>
        </div>

        {/* Global Grade & Subject Selector */}
        <div className="flex flex-wrap items-center gap-2.5">
          <GradeSelector compact={true} />
          <SubjectBar compact={true} />

          {chapters.length > 0 && (
            <div className="flex items-center gap-1.5 shrink-0">
              <Filter className="w-3.5 h-3.5 text-slate-400" />
              <select
                value={selectedChapter}
                onChange={(e) => handleFilterChange(e.target.value)}
                className="px-2.5 py-1.5 rounded-xl text-xs font-bold text-slate-200 bg-slate-900 border border-white/10 focus:ring-2 focus:ring-cyan-500 shadow-xs max-w-[170px] truncate outline-none"
              >
                <option value="">All Chapters (Adaptive)</option>
                {chapters.map((ch) => (
                  <option key={ch.id} value={ch.id}>
                    {ch.title}
                  </option>
                ))}
              </select>
            </div>
          )}
        </div>
      </motion.div>

      {/* Main Content Area */}
      {loading ? (
        <AnimatedCard className="p-16 text-center">
          <LoadingState
            stages={[
              'Fetching zone-of-proximal-development challenge...',
              'Calibrating item response parameters...',
              'Querying knowledge graph prerequisite vectors...',
            ]}
          />
        </AnimatedCard>
      ) : question ? (
        <div className="space-y-6">
          {/* Question Card */}
          <AnimatedCard spotlight={true} glowColor="cyan" className="p-6 sm:p-8 border-white/10 bg-slate-950/80 shadow-glass-card-hover">
            {/* Meta Tags Bar */}
            <div className="flex flex-wrap items-center justify-between gap-3 pb-5 border-b border-white/[0.08]">
              <div className="flex flex-wrap items-center gap-2">
                <span className="px-2.5 py-1 rounded-lg text-xs font-mono font-black uppercase bg-violet-950/70 text-violet-300 border border-violet-800/60 shadow-glow-sm">
                  Class {question.grade || selectedGrade}
                </span>
                <span className="px-2.5 py-1 rounded-lg text-xs font-mono font-black uppercase bg-blue-950/70 text-blue-300 border border-blue-800/60 shadow-glow-sm">
                  {question.subject_name || 'STEM'}
                </span>
                <span className="px-2.5 py-1 rounded-lg text-xs font-bold bg-white/[0.04] text-slate-300 border border-white/10">
                  {question.chapter_name}
                </span>
                <span className="text-xs text-slate-400 font-bold truncate max-w-[180px]">
                  {question.concept_name}
                </span>
                <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold border uppercase ${getDifficultyStyles(question.difficulty)}`}>
                  {question.difficulty}
                </span>
              </div>

              <div className="flex items-center gap-3 text-xs text-slate-400 font-mono">
                <span className="flex items-center gap-1.5 bg-white/[0.04] px-2.5 py-1 rounded-lg border border-white/10 text-cyan-300">
                  <Clock className="w-3.5 h-3.5 text-cyan-400 animate-pulse" />
                  {timerSeconds}s
                </span>
                <span>·</span>
                <span>
                  Topic Mastery: <strong className="text-cyan-400 font-bold">{question.current_mastery}%</strong>
                </span>
              </div>
            </div>

            {/* Question Text */}
            <div className="py-6">
              <h2 className="text-lg sm:text-xl font-bold text-white leading-relaxed">
                {question.question_text}
              </h2>

              {/* Answer Option Buttons */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5 mt-6">
                {question.options.map((opt) => {
                  const isSelected = selectedOption === opt.id;
                  const isCorrectAnswer = result && opt.id === result.correct_option;
                  const isWrongAnswer = result && isSelected && !result.is_correct;

                  let borderClass = 'border-white/[0.08] bg-white/[0.03] text-slate-300 hover:border-white/20 hover:bg-white/[0.06]';
                  if (isSelected && !result) {
                    borderClass = 'border-cyan-400 bg-cyan-950/60 text-white shadow-glow-cyan ring-1 ring-cyan-400';
                  } else if (isCorrectAnswer) {
                    borderClass = 'border-emerald-400 bg-emerald-950/70 text-emerald-200 shadow-glow-emerald ring-2 ring-emerald-400/40';
                  } else if (isWrongAnswer) {
                    borderClass = 'border-rose-400 bg-rose-950/70 text-rose-200 shadow-glow-rose ring-2 ring-rose-400/40';
                  }

                  return (
                    <motion.button
                      key={opt.id}
                      whileHover={!result && !submitting ? { scale: 1.015, y: -1 } : {}}
                      whileTap={!result && !submitting ? { scale: 0.98 } : {}}
                      disabled={!!result || submitting}
                      onClick={() => setSelectedOption(opt.id)}
                      className={`p-4 rounded-2xl text-left border text-sm font-bold transition-all flex items-start gap-3.5 shadow-sm outline-none select-none cursor-pointer ${borderClass}`}
                    >
                      <span
                        className={`w-7 h-7 rounded-xl flex items-center justify-center text-xs font-mono font-black shrink-0 transition-transform ${
                          isSelected
                            ? 'bg-cyan-500 text-slate-950 scale-110 shadow-glow-sm'
                            : 'bg-white/[0.08] text-slate-400 border border-white/10'
                        }`}
                      >
                        {opt.id}
                      </span>
                      <span className="leading-snug mt-0.5">{opt.text}</span>
                    </motion.button>
                  );
                })}
              </div>

              {/* Student Written Reasoning deduction */}
              <div className="mt-6">
                <div className="flex items-center justify-between mb-2">
                  <label className="text-xs font-bold text-slate-300 flex items-center gap-1.5">
                    <BrainCircuit className="w-4 h-4 text-cyan-400 animate-pulse" />
                    Why did you choose this option? (Deduction analyzed by AI)
                  </label>
                  {question.hint && !showHint && !result && (
                    <button
                      onClick={() => setShowHint(true)}
                      className="text-xs text-amber-400 hover:text-amber-300 font-bold flex items-center gap-1 bg-amber-950/40 px-2.5 py-1 rounded-lg border border-amber-800/60 shadow-sm cursor-pointer"
                    >
                      <Lightbulb className="w-3.5 h-3.5" />
                      Show Hint
                    </button>
                  )}
                </div>

                {showHint && question.hint && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    className="mb-3 p-3.5 rounded-xl bg-amber-950/40 border border-amber-800/60 text-xs text-amber-200 flex items-start gap-2 shadow-sm"
                  >
                    <Lightbulb className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                    <span><strong>Hint:</strong> {question.hint}</span>
                  </motion.div>
                )}

                <textarea
                  disabled={!!result || submitting}
                  value={reasoning}
                  onChange={(e) => setReasoning(e.target.value)}
                  placeholder="State your formula, scientific principle, or step-by-step logic (e.g. V = IR, conservation of volume, or Mendelian segregation)..."
                  className="w-full h-20 p-3.5 rounded-xl glass-input-dark text-xs resize-none font-medium text-white placeholder-slate-500"
                />
              </div>

              {/* Submitting Stage Sequence or Action Buttons */}
              <div className="mt-6 flex items-center justify-between">
                {submitting ? (
                  <div className="w-full">
                    <LoadingState
                      stages={[
                        'Analyzing your reasoning with Gemini AI...',
                        'Evaluating conceptual traps and misconceptions...',
                        'Updating continuous BKT learner profile...',
                        'Adapting optimal next challenge...',
                      ]}
                    />
                  </div>
                ) : !result ? (
                  <div className="flex items-center justify-between w-full">
                    <span className="text-[11px] text-slate-500 font-mono hidden sm:inline">
                      Press <kbd className="px-1.5 py-0.5 rounded bg-white/[0.08] text-slate-300 border border-white/10 font-bold">A</kbd> <kbd className="px-1.5 py-0.5 rounded bg-white/[0.08] text-slate-300 border border-white/10 font-bold">B</kbd> <kbd className="px-1.5 py-0.5 rounded bg-white/[0.08] text-slate-300 border border-white/10 font-bold">C</kbd> <kbd className="px-1.5 py-0.5 rounded bg-white/[0.08] text-slate-300 border border-white/10 font-bold">D</kbd> to pick
                    </span>
                    <GlowButton
                      variant="electric"
                      size="lg"
                      onClick={handleSubmit}
                      disabled={!selectedOption || submitting}
                      icon={ArrowRight}
                    >
                      Submit Answer
                    </GlowButton>
                  </div>
                ) : (
                  <div className="flex items-center justify-between w-full">
                    <div className="flex items-center gap-2">
                      <span className="text-xs font-mono font-bold text-slate-400">Next Question Ready</span>
                    </div>
                    <GlowButton
                      variant="electric"
                      size="lg"
                      onClick={fetchNextQuestion}
                      icon={ArrowRight}
                    >
                      Next Challenge
                    </GlowButton>
                  </div>
                )}
              </div>
            </div>
          </AnimatedCard>

          {/* Interactive Result Feedback Breakdown */}
          <AnimatePresence>
            {result && (
              <motion.div
                initial={{ opacity: 0, y: 25, scale: 0.97 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ type: 'spring', damping: 20 }}
                className="glass-panel-dark p-6 sm:p-8 rounded-3xl border border-white/10 shadow-glass-card-hover space-y-5"
              >
                {/* Result Header */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                  <div className="flex items-center gap-3.5">
                    {result.is_correct ? (
                      <div className="w-12 h-12 rounded-2xl bg-emerald-950/80 border border-emerald-500/60 text-emerald-400 flex items-center justify-center shadow-glow-emerald">
                        <CheckCircle2 className="w-7 h-7" />
                      </div>
                    ) : (
                      <div className="w-12 h-12 rounded-2xl bg-rose-950/80 border border-rose-500/60 text-rose-400 flex items-center justify-center shadow-glow-rose">
                        <XCircle className="w-7 h-7" />
                      </div>
                    )}
                    <div>
                      <div className="text-base sm:text-lg font-black text-white">
                        {result.is_correct ? 'Correct! Strong Conceptual Reasoning!' : 'Incorrect Deduction'}
                      </div>
                      <div className="text-xs text-slate-400 font-medium">
                        {result.is_correct
                          ? `Awarded +${result.xp_awarded} XP toward your learning streak!`
                          : 'Carefully review the conceptual diagnosis below to remediate this gap.'}
                      </div>
                    </div>
                  </div>

                  {/* Score Update Badge */}
                  <div className="flex items-center gap-3 bg-white/[0.04] p-3 rounded-2xl border border-white/10">
                    <div className="text-right font-mono">
                      <div className="text-[10px] text-slate-400 uppercase tracking-wider font-bold">
                        Mastery Shift
                      </div>
                      <div className="text-sm font-black text-white">
                        {result.mastery_update.previous_mastery}% &rarr; {result.mastery_update.new_mastery}%
                      </div>
                    </div>
                    <span
                      className={`px-2.5 py-1 rounded-xl text-xs font-mono font-black ${
                        result.mastery_update.delta >= 0
                          ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-800/60 shadow-glow-emerald'
                          : 'bg-rose-950/80 text-rose-300 border border-rose-800/60 shadow-glow-rose'
                      }`}
                    >
                      {result.mastery_update.delta >= 0 ? `+${result.mastery_update.delta}%` : `${result.mastery_update.delta}%`}
                    </span>
                  </div>
                </div>

                {/* Concept Explanation Box */}
                <div className="p-4 rounded-2xl bg-white/[0.03] border border-white/[0.08] text-xs text-slate-300 leading-relaxed font-medium">
                  <p className="font-extrabold text-white mb-1.5 flex items-center gap-1.5">
                    <Sparkles className="w-4 h-4 text-cyan-400" />
                    Concept Explanation & Reasoning Analysis:
                  </p>
                  {result.explanation}
                </div>

                {/* Misconception Notice if detected */}
                {result.misconception && (
                  <div className="p-4 rounded-2xl bg-amber-950/40 border border-amber-500/40 text-amber-200 text-xs space-y-1.5 shadow-glow-amber">
                    <div className="font-extrabold text-amber-300 flex items-center gap-2">
                      <ShieldAlert className="w-4 h-4 text-amber-400" />
                      <span>Conceptual Trap Identified: {result.misconception.label}</span>
                    </div>
                    <p className="text-slate-300 leading-relaxed">
                      {result.misconception.remediation}
                    </p>
                  </div>
                )}
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      ) : null}
    </AnimatedPage>
  );
};
