import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import {
  Milestone,
  CheckCircle2,
  Lock,
  Play,
  Clock,
  Target,
  AlertCircle,
  Sparkles,
  ArrowRight,
  BookOpen
} from 'lucide-react';
import { api } from '../services/api';
import { LearningPathItem } from '../types';
import { AnimatedPage } from '../components/animations/AnimatedPage';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';
import { LoadingState } from '../components/animations/LoadingState';

export const LearningPathPage: React.FC = () => {
  const navigate = useNavigate();
  const [pathItems, setPathItems] = useState<LearningPathItem[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadPath() {
      try {
        const res = await api.getLearningPath();
        setPathItems(res || []);
      } catch (err) {
        console.error('Failed to load learning path:', err);
      } finally {
        setLoading(false);
      }
    }
    loadPath();
  }, []);

  const getPriorityBadge = (p: string) => {
    switch (p) {
      case 'Critical':
        return 'bg-rose-950/80 text-rose-300 border-rose-800/60 shadow-glow-rose font-bold';
      case 'High':
        return 'bg-amber-950/80 text-amber-300 border-amber-800/60 shadow-glow-amber font-bold';
      default:
        return 'bg-cyan-950/80 text-cyan-300 border-cyan-800/60 shadow-glow-cyan font-bold';
    }
  };

  return (
    <AnimatedPage className="p-4 sm:p-8 max-w-4xl mx-auto space-y-8 font-sans">
      {/* Top Banner */}
      <AnimatedCard glowColor="cyan" className="p-6 sm:p-8 bg-slate-950/80 border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-6">
        <div className="space-y-2">
          <div className="flex items-center gap-2 text-xs font-mono font-bold text-cyan-400 uppercase tracking-widest">
            <Milestone className="w-4 h-4 text-cyan-400" />
            <span>Optimal Prerequisite Sequence</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
            Personalized Mastery Roadmap
          </h1>
          <p className="text-slate-400 text-xs sm:text-sm max-w-lg font-medium leading-relaxed">
            Organized into structured milestones across your STEM curriculum, balancing prerequisites, active gaps, and forgetting curve intervals.
          </p>
        </div>

        <GlowButton
          variant="electric"
          size="md"
          onClick={() => navigate('/arena')}
          icon={Play}
          className="shrink-0"
        >
          Resume Active Step
        </GlowButton>
      </AnimatedCard>

      {loading ? (
        <AnimatedCard className="p-16 text-center">
          <LoadingState
            stages={[
              'Traversing knowledge graph dependency chains...',
              'Sequencing prerequisite paths...',
              'Synthesizing adaptive milestones...',
            ]}
          />
        </AnimatedCard>
      ) : (
        /* Vertical Roadmap Timeline */
        <div className="relative pl-6 sm:pl-8 space-y-6 before:absolute before:left-3 before:top-4 before:bottom-4 before:w-0.5 before:bg-gradient-to-b before:from-cyan-500 before:via-blue-600 before:to-slate-800">
          {pathItems.map((item, idx) => {
            const isCompleted = item.status === 'completed';
            const isInProgress = item.status === 'in_progress';
            const isLocked = item.status === 'locked';

            return (
              <AnimatedCard
                key={item.id || idx}
                spotlight={true}
                glowColor={isInProgress ? 'cyan' : isCompleted ? 'emerald' : 'blue'}
                className={`p-6 relative ${
                  isInProgress
                    ? 'border-cyan-400/80 ring-1 ring-cyan-400/40 shadow-glow-cyan'
                    : isCompleted
                    ? 'border-emerald-500/40 bg-slate-950/70'
                    : 'border-white/[0.06] bg-slate-950/40 opacity-70'
                }`}
              >
                {/* Timeline node marker */}
                <div
                  className={`absolute -left-9 sm:-left-11 top-6 w-7 h-7 rounded-full border-2 flex items-center justify-center shadow-sm ${
                    isCompleted
                      ? 'border-emerald-400 bg-emerald-950 text-emerald-400'
                      : isInProgress
                      ? 'border-cyan-400 bg-cyan-500 text-slate-950 shadow-glow-cyan animate-pulse'
                      : 'border-slate-700 bg-slate-900 text-slate-500'
                  }`}
                >
                  {isCompleted ? (
                    <CheckCircle2 className="w-4 h-4" />
                  ) : isInProgress ? (
                    <Play className="w-3 h-3 fill-current ml-0.5" />
                  ) : (
                    <Lock className="w-3 h-3" />
                  )}
                </div>

                <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-white/[0.08]">
                  <div className="flex items-center gap-2">
                    <span className="text-[10px] font-mono text-slate-400 uppercase font-bold">
                      Milestone 0{idx + 1}
                    </span>
                    <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold border ${getPriorityBadge(item.priority)}`}>
                      {item.priority} Priority
                    </span>
                  </div>

                  <div className="flex items-center gap-4 text-xs text-slate-400 font-mono font-semibold">
                    <span className="flex items-center gap-1">
                      <Clock className="w-3.5 h-3.5 text-slate-500" />
                      {item.estimated_minutes} mins
                    </span>
                    <span className="flex items-center gap-1 font-bold text-cyan-400">
                      <Target className="w-3.5 h-3.5 text-cyan-400" />
                      Target: {item.mastery_target}%
                    </span>
                  </div>
                </div>

                <div className="py-4">
                  <h3 className="text-base sm:text-lg font-black text-white">
                    {item.concept_name}
                  </h3>
                  <p className="text-xs text-slate-300 mt-1 leading-relaxed font-medium">
                    {item.reason}
                  </p>

                  <div className="mt-3.5 p-3.5 rounded-2xl bg-white/[0.03] border border-white/[0.08] text-xs text-slate-300 flex items-start gap-2.5">
                    <BookOpen className="w-4 h-4 text-cyan-400 shrink-0 mt-0.5" />
                    <div>
                      <strong className="text-cyan-300 font-mono">Prescribed Target:</strong>{' '}
                      {item.recommended_activity}
                    </div>
                  </div>
                </div>

                <div className="pt-2 flex items-center justify-between">
                  <span
                    className={`text-xs font-mono font-bold capitalize ${
                      isInProgress
                        ? 'text-cyan-300'
                        : isCompleted
                        ? 'text-emerald-400'
                        : 'text-slate-500'
                    }`}
                  >
                    {isInProgress ? '● Currently Active' : isCompleted ? '✓ Completed' : 'Locked (Prerequisite Required)'}
                  </span>

                  {!isLocked && (
                    <GlowButton
                      variant={isInProgress ? 'electric' : 'secondary'}
                      size="sm"
                      onClick={() => navigate(`/arena?concept_id=${item.concept_id}`)}
                      icon={ArrowRight}
                    >
                      Practice Milestone
                    </GlowButton>
                  )}
                </div>
              </AnimatedCard>
            );
          })}
        </div>
      )}
    </AnimatedPage>
  );
};
