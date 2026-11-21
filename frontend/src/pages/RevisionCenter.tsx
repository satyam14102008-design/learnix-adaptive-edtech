import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  RotateCcw,
  Flame,
  Clock,
  CheckCircle2,
  AlertCircle,
  Calendar,
  Sparkles,
  Zap,
  ArrowRight,
  X,
  BookOpen,
  ThumbsUp,
  HelpCircle
} from 'lucide-react';
import { api } from '../services/api';
import { RevisionItem } from '../types';
import { useSubject } from '../context/SubjectContext';
import { useGrade } from '../context/GradeContext';
import { SubjectBar } from '../components/SubjectBar';
import { GradeSelector } from '../components/GradeSelector';
import { AnimatedPage } from '../components/animations/AnimatedPage';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';
import { AnimatedCounter } from '../components/animations/AnimatedCounter';

export const RevisionCenter: React.FC = () => {
  const navigate = useNavigate();
  const { selectedSubject } = useSubject();
  const { selectedGrade, currentGradeMeta } = useGrade();
  const [data, setData] = useState<any>(null);
  const [activeTab, setActiveTab] = useState<'due' | 'overdue' | 'upcoming'>('due');
  const [selectedRevision, setSelectedRevision] = useState<RevisionItem | null>(null);
  const [completing, setCompleting] = useState(false);
  const [feedbackMsg, setFeedbackMsg] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadRevisions();
  }, []);

  const loadRevisions = async () => {
    try {
      const res = await api.getDueRevisions();
      setData(res);
    } catch (err) {
      console.error('Failed to load revisions:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleRecordQuality = async (qualityScore: number) => {
    if (!selectedRevision) return;
    setCompleting(true);
    try {
      const res = await api.completeRevision({
        concept_id: selectedRevision.concept_id,
        quality_score: qualityScore,
      });
      setFeedbackMsg(res.message || 'Progress saved! Updated SM-2 review schedule.');
      setTimeout(() => {
        setFeedbackMsg(null);
        setSelectedRevision(null);
        loadRevisions();
      }, 1400);
    } catch (err) {
      console.error('Failed to complete revision:', err);
    } finally {
      setCompleting(false);
    }
  };

  const filterRevisions = (items: RevisionItem[]) => {
    let filtered = items;
    if (selectedGrade) {
      filtered = filtered.filter((item: any) => !item.grade || item.grade === selectedGrade);
    }
    if (selectedSubject && selectedSubject !== 'all') {
      filtered = filtered.filter((item: any) => item.subject_id === selectedSubject);
    }
    return filtered;
  };

  const rawDueList: RevisionItem[] = data?.due_today || [];
  const rawOverdueList: RevisionItem[] = data?.overdue || [];
  const rawUpcomingList: RevisionItem[] = data?.upcoming || [];

  const dueList = filterRevisions(rawDueList);
  const overdueList = filterRevisions(rawOverdueList);
  const upcomingList = filterRevisions(rawUpcomingList);

  const displayedList = activeTab === 'due' ? dueList : (activeTab === 'overdue' ? overdueList : upcomingList);

  return (
    <AnimatedPage className="p-4 sm:p-8 max-w-5xl mx-auto space-y-6 font-sans">
      {/* Top Filter and Topic Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-slate-900/70 p-3 rounded-2xl border border-white/10 shadow-glass-card backdrop-blur-xl">
        <span className="text-xs font-mono font-bold text-slate-300 uppercase tracking-wider px-2">
          Filter Review Topics
        </span>
        <div className="flex flex-wrap items-center gap-2">
          <GradeSelector compact={true} />
          <SubjectBar compact={true} />
        </div>
      </div>

      {/* Hero Spaced Repetition Card */}
      <AnimatedCard glowColor="amber" className="p-6 sm:p-8 bg-slate-950/80 border-white/10 shadow-glass-card-hover">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="flex items-center gap-2 text-xs font-mono font-bold text-amber-400 uppercase tracking-widest">
              <RotateCcw className="w-4 h-4 text-amber-400 animate-spin [animation-duration:10s]" />
              <span>SM-2 Memory Retention Engine</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
              Spaced Revision Center
            </h1>
            <p className="text-slate-400 text-xs sm:text-sm max-w-lg leading-relaxed font-medium">
              Review key concepts at scientifically optimal forgetting curve intervals to cement formulas and mechanisms into long-term memory.
            </p>
          </div>

          <div className="flex items-center gap-4 shrink-0">
            <div className="text-center px-5 py-3.5 rounded-2xl bg-amber-950/50 border border-amber-800/60 shadow-glow-amber">
              <div className="text-[10px] font-mono text-amber-300 uppercase tracking-wider font-bold">Due Today</div>
              <div className="text-2xl font-black text-amber-400 font-mono mt-0.5">
                <AnimatedCounter value={dueList.length + overdueList.length} />
              </div>
            </div>
            <div className="text-center px-5 py-3.5 rounded-2xl bg-cyan-950/50 border border-cyan-800/60 shadow-glow-cyan">
              <div className="text-[10px] font-mono text-cyan-300 uppercase tracking-wider font-bold">Est. Time</div>
              <div className="text-2xl font-black text-cyan-400 font-mono mt-0.5">
                <AnimatedCounter value={Math.max((dueList.length + overdueList.length) * 2, 5)} suffix="m" />
              </div>
            </div>
          </div>
        </div>
      </AnimatedCard>

      {/* Tabs */}
      <div className="flex items-center gap-2 border-b border-white/[0.08] pb-3 text-xs font-bold font-mono">
        <button
          onClick={() => setActiveTab('due')}
          className={`px-4 py-2 rounded-xl transition-all ${
            activeTab === 'due'
              ? 'bg-amber-950/80 text-amber-300 border border-amber-800/80 shadow-glow-amber font-black'
              : 'text-slate-400 hover:text-white hover:bg-white/[0.04]'
          }`}
        >
          Due Today ({dueList.length})
        </button>
        <button
          onClick={() => setActiveTab('overdue')}
          className={`px-4 py-2 rounded-xl transition-all ${
            activeTab === 'overdue'
              ? 'bg-rose-950/80 text-rose-300 border border-rose-800/80 shadow-glow-rose font-black'
              : 'text-slate-400 hover:text-white hover:bg-white/[0.04]'
          }`}
        >
          Catch Up ({overdueList.length})
        </button>
        <button
          onClick={() => setActiveTab('upcoming')}
          className={`px-4 py-2 rounded-xl transition-all ${
            activeTab === 'upcoming'
              ? 'bg-cyan-950/80 text-cyan-300 border border-cyan-800/80 shadow-glow-cyan font-black'
              : 'text-slate-400 hover:text-white hover:bg-white/[0.04]'
          }`}
        >
          Upcoming ({upcomingList.length})
        </button>
      </div>

      {/* Revisions Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {displayedList.length === 0 ? (
          <div className="col-span-2 glass-panel-dark p-12 rounded-3xl text-center text-slate-400 space-y-3 border border-white/10 shadow-glass-card">
            <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto" />
            <h4 className="text-white font-black text-lg">You are completely up to date!</h4>
            <p className="text-xs text-slate-400 max-w-md mx-auto">
              No concepts are due for review right now. Head into the Adaptive Arena to challenge new curriculum targets!
            </p>
            <GlowButton
              variant="electric"
              size="md"
              onClick={() => navigate('/arena')}
              icon={Zap}
              className="mt-2"
            >
              Go to Adaptive Arena
            </GlowButton>
          </div>
        ) : (
          displayedList.map((item, idx) => (
            <AnimatedCard
              key={item.concept_id}
              spotlight={true}
              glowColor="amber"
              className="p-6 flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between">
                  <span className="text-[10px] font-mono font-bold text-cyan-400 uppercase tracking-wider">
                    {item.chapter_id?.replace(/_/g, ' ')}
                  </span>
                  <span className="text-xs font-mono font-bold text-emerald-300 bg-emerald-950/60 px-2 py-0.5 rounded-full border border-emerald-800/60 shadow-glow-sm">
                    {item.mastery_score}% Mastered
                  </span>
                </div>
                <h3 className="text-base font-extrabold text-white mt-1.5">
                  {item.concept_name}
                </h3>
                <div className="text-xs text-slate-400 mt-2 flex items-center gap-3 font-mono">
                  <span className="flex items-center gap-1.5">
                    <Clock className="w-3.5 h-3.5 text-slate-500" />
                    Interval: {item.interval_days} {item.interval_days === 1 ? 'day' : 'days'}
                  </span>
                </div>
              </div>

              <div className="mt-5 pt-3 border-t border-white/[0.06] flex items-center justify-between">
                <span className="text-[11px] font-mono text-amber-400 font-bold">
                  {item.status === 'due_today'
                    ? 'Due for review'
                    : item.status === 'overdue'
                    ? 'Interval exceeded'
                    : 'Scheduled'}
                </span>
                <GlowButton
                  variant="secondary"
                  size="sm"
                  onClick={() => setSelectedRevision(item)}
                  icon={ArrowRight}
                >
                  Review Flashcard
                </GlowButton>
              </div>
            </AnimatedCard>
          ))
        )}
      </div>

      {/* Review Flashcard Modal */}
      <AnimatePresence>
        {selectedRevision && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 bg-slate-950/80 backdrop-blur-md"
              onClick={() => setSelectedRevision(null)}
            />
            <motion.div
              initial={{ scale: 0.92, opacity: 0, y: 20 }}
              animate={{ scale: 1, opacity: 1, y: 0 }}
              exit={{ scale: 0.92, opacity: 0, y: 20 }}
              transition={{ type: 'spring', damping: 25 }}
              className="relative w-full max-w-lg glass-panel-dark p-6 sm:p-8 rounded-3xl border border-white/10 shadow-2xl z-10 space-y-6"
            >
              <div className="flex items-start justify-between">
                <div>
                  <span className="text-xs font-mono font-bold text-amber-400 uppercase tracking-widest bg-amber-950/60 px-2.5 py-1 rounded-full border border-amber-800/60">
                    Flash Recall Check
                  </span>
                  <h2 className="text-xl font-black text-white mt-2">
                    {selectedRevision.concept_name}
                  </h2>
                </div>
                <button
                  onClick={() => setSelectedRevision(null)}
                  className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-white/[0.06] transition-colors"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              <div className="p-4 rounded-2xl bg-white/[0.03] border border-white/[0.08] text-sm text-slate-300 leading-relaxed font-medium">
                <p className="font-extrabold text-white mb-1">Active Recall Prompt:</p>
                Can you state the governing formula, definition, or physical mechanism for this topic from memory?
              </div>

              {feedbackMsg ? (
                <motion.div
                  initial={{ scale: 0.9 }}
                  animate={{ scale: 1 }}
                  className="p-4 rounded-2xl bg-emerald-950/80 border border-emerald-500/60 text-emerald-300 text-center font-bold text-sm shadow-glow-emerald font-mono"
                >
                  {feedbackMsg}
                </motion.div>
              ) : (
                <div className="space-y-3">
                  <div className="text-xs font-mono font-bold text-slate-400 uppercase tracking-wider">
                    Rate Your Memory Recall Quality
                  </div>
                  <div className="grid grid-cols-3 gap-2.5 text-xs font-bold">
                    <button
                      onClick={() => handleRecordQuality(1)}
                      disabled={completing}
                      className="p-3.5 rounded-2xl border border-rose-800/60 bg-rose-950/50 hover:bg-rose-900/60 text-rose-300 text-center flex flex-col items-center gap-1 shadow-sm transition-all"
                    >
                      <span className="text-lg">❌</span>
                      <span>Forgot</span>
                    </button>
                    <button
                      onClick={() => handleRecordQuality(3)}
                      disabled={completing}
                      className="p-3.5 rounded-2xl border border-amber-800/60 bg-amber-950/50 hover:bg-amber-900/60 text-amber-300 text-center flex flex-col items-center gap-1 shadow-sm transition-all"
                    >
                      <span className="text-lg">⚠️</span>
                      <span>Partially</span>
                    </button>
                    <button
                      onClick={() => handleRecordQuality(5)}
                      disabled={completing}
                      className="p-3.5 rounded-2xl border border-emerald-800/60 bg-emerald-950/50 hover:bg-emerald-900/60 text-emerald-300 text-center flex flex-col items-center gap-1 shadow-sm transition-all"
                    >
                      <span className="text-lg">⚡</span>
                      <span>Mastered</span>
                    </button>
                  </div>

                  <div className="pt-2 text-center">
                    <button
                      onClick={() => {
                        const conceptId = selectedRevision.concept_id;
                        setSelectedRevision(null);
                        navigate(`/arena?concept_id=${conceptId}`);
                      }}
                      className="text-xs text-cyan-400 hover:text-cyan-300 font-bold inline-flex items-center gap-1 transition-colors"
                    >
                      Want to solve real questions on this? <ArrowRight className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>
              )}
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </AnimatedPage>
  );
};
