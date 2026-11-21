import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  FileCheck2,
  Clock,
  BrainCircuit,
  CheckCircle2,
  ArrowRight,
  ArrowLeft,
  Sparkles,
  BarChart2,
  AlertTriangle,
  RotateCcw,
  Milestone,
  Zap,
  Target
} from 'lucide-react';
import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  ResponsiveContainer
} from 'recharts';
import { api } from '../services/api';
import { useSubject } from '../context/SubjectContext';
import { useGrade } from '../context/GradeContext';
import { SubjectBar } from '../components/SubjectBar';
import { GradeSelector } from '../components/GradeSelector';
import { AnimatedPage } from '../components/animations/AnimatedPage';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';
import { AnimatedCounter } from '../components/animations/AnimatedCounter';
import { LoadingState } from '../components/animations/LoadingState';

export const DiagnosticAssessment: React.FC = () => {
  const navigate = useNavigate();
  const { selectedSubject } = useSubject();
  const { selectedGrade, currentGradeMeta } = useGrade();
  const [questions, setQuestions] = useState<any[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<string, { option: string; reasoning: string }>>({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [report, setReport] = useState<any>(null);

  useEffect(() => {
    async function loadTest() {
      setLoading(true);
      try {
        const res = await api.startDiagnostic({
          grade: selectedGrade,
          subject_id: selectedSubject !== 'all' ? selectedSubject : undefined,
        });
        setQuestions(res.questions || []);
        setCurrentIndex(0);
        setAnswers({});
      } catch (err) {
        console.error('Failed to load diagnostic questions:', err);
      } finally {
        setLoading(false);
      }
    }
    loadTest();
  }, [selectedGrade, selectedSubject]);

  const currentQ = questions[currentIndex];
  const currentAnswer = currentQ ? (answers[currentQ.id] || { option: '', reasoning: '' }) : { option: '', reasoning: '' };

  const handleSelectOption = (optId: string) => {
    if (!currentQ) return;
    setAnswers({
      ...answers,
      [currentQ.id]: {
        ...currentAnswer,
        option: optId,
      },
    });
  };

  const handleReasoningChange = (text: string) => {
    if (!currentQ) return;
    setAnswers({
      ...answers,
      [currentQ.id]: {
        ...currentAnswer,
        reasoning: text,
      },
    });
  };

  const handleSubmitDiagnostic = async () => {
    setSubmitting(true);
    const submissionPayload = questions.map((q) => ({
      question_id: q.id,
      concept_id: q.concept_id,
      selected_option: answers[q.id]?.option || 'A',
      reasoning: answers[q.id]?.reasoning || 'Diagnostic attempt',
      response_time_seconds: 45.0,
    }));

    try {
      const res = await api.submitDiagnostic({ answers: submissionPayload });
      setReport(res);
    } catch (err) {
      console.error('Failed to submit diagnostic:', err);
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <AnimatedPage className="p-16 text-center max-w-xl mx-auto">
        <AnimatedCard className="p-12">
          <LoadingState
            stages={[
              'Calibrating 10-Minute Skill Check diagnostic...',
              'Selecting cross-chapter benchmark probes...',
              'Constructing dynamic knowledge baseline...',
            ]}
          />
        </AnimatedCard>
      </AnimatedPage>
    );
  }

  // Diagnostic Report View
  if (report) {
    const radarData = (report.chapter_performance || []).map((ch: any) => ({
      subject: ch.chapter_name.split('–')[0].trim(),
      score: ch.score,
    }));

    return (
      <AnimatedPage className="p-4 sm:p-8 max-w-5xl mx-auto space-y-8 font-sans">
        <AnimatedCard glowColor="emerald" className="p-8 text-center space-y-3 bg-emerald-950/30 border-emerald-500/40 shadow-glow-emerald">
          <div className="w-14 h-14 rounded-2xl bg-emerald-950/80 border border-emerald-500/60 flex items-center justify-center text-emerald-400 mx-auto shadow-glow-emerald">
            <CheckCircle2 className="w-8 h-8" />
          </div>
          <span className="text-xs font-mono font-bold text-emerald-300 uppercase tracking-widest bg-emerald-950/80 px-3 py-1 rounded-full border border-emerald-800/60">
            Diagnostic Complete
          </span>
          <h1 className="text-2xl sm:text-3xl font-black text-white">
            {currentGradeMeta?.name} STEM Readiness Profile
          </h1>
          <p className="text-slate-300 text-xs sm:text-sm max-w-lg mx-auto font-medium">
            Cognitive analysis complete! We pinpointed your conceptual strengths and constructed your customized mastery roadmap.
          </p>
        </AnimatedCard>

        {/* Radar & Summary Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Radar Chart */}
          <AnimatedCard glowColor="cyan" className="p-6 flex flex-col items-center justify-center">
            <h3 className="text-sm font-extrabold text-white mb-2">Chapter Readiness Topology</h3>
            <div className="h-64 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <RadarChart data={radarData}>
                  <PolarGrid stroke="rgba(255, 255, 255, 0.1)" />
                  <PolarAngleAxis dataKey="subject" tick={{ fill: '#94a3b8', fontSize: 11, fontWeight: 700 }} />
                  <Radar name="Mastery" dataKey="score" stroke="#38bdf8" fill="#06b6d4" fillOpacity={0.35} />
                </RadarChart>
              </ResponsiveContainer>
            </div>
          </AnimatedCard>

          {/* Key Findings Card */}
          <AnimatedCard glowColor="blue" className="p-6 flex flex-col justify-between">
            <div>
              <h3 className="text-sm font-extrabold text-white mb-4">Diagnostic Synthesis</h3>
              <div className="space-y-3 text-xs font-mono">
                <div className="flex items-center justify-between p-3.5 rounded-xl bg-white/[0.04] border border-white/10">
                  <span className="text-slate-400 font-bold">Probes Evaluated</span>
                  <span className="font-extrabold text-white text-sm">{report.total_questions}</span>
                </div>
                <div className="flex items-center justify-between p-3.5 rounded-xl bg-white/[0.04] border border-white/10">
                  <span className="text-slate-400 font-bold">Overall Accuracy</span>
                  <span className="font-extrabold text-emerald-400 text-sm">{report.overall_accuracy}%</span>
                </div>
                <div className="flex items-center justify-between p-3.5 rounded-xl bg-white/[0.04] border border-white/10">
                  <span className="text-slate-400 font-bold">Target Gaps to Remediate</span>
                  <span className="font-extrabold text-amber-400 text-sm">
                    {report.misconceptions_detected?.length || 0} topics
                  </span>
                </div>
              </div>

              {/* Misconceptions detected */}
              {report.misconceptions_detected && report.misconceptions_detected.length > 0 && (
                <div className="mt-4 p-4 rounded-2xl bg-amber-950/40 border border-amber-800/60 text-xs text-amber-200 space-y-1 shadow-glow-amber">
                  <div className="font-extrabold text-amber-300 flex items-center gap-1.5">
                    <AlertTriangle className="w-4 h-4 text-amber-400" />
                    <span>Priority Focus Area:</span>
                  </div>
                  <div className="font-bold">{report.misconceptions_detected[0].label}</div>
                  <div className="text-[11px] text-slate-300 mt-1 font-medium">
                    This topic has been prioritized in your mastery roadmap so you can clear up misconceptions immediately.
                  </div>
                </div>
              )}
            </div>

            <div className="mt-6 flex gap-3">
              <GlowButton
                variant="electric"
                size="md"
                onClick={() => navigate('/learning-path')}
                icon={Milestone}
                className="flex-1"
              >
                View Mastery Roadmap
              </GlowButton>
              <GlowButton
                variant="secondary"
                size="md"
                onClick={() => navigate('/arena')}
                icon={Zap}
              >
                Start Practice
              </GlowButton>
            </div>
          </AnimatedCard>
        </div>
      </AnimatedPage>
    );
  }

  // Active Diagnostic Question Stepper
  const progressPercent = ((currentIndex + 1) / questions.length) * 100;

  return (
    <AnimatedPage className="p-4 sm:p-8 max-w-4xl mx-auto space-y-6 font-sans">
      {/* Top Filter and Topic Bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-slate-900/70 p-3 rounded-2xl border border-white/10 shadow-glass-card backdrop-blur-xl">
        <span className="text-xs font-mono font-bold text-slate-300 uppercase tracking-wider px-2">
          Diagnostic Scope
        </span>
        <div className="flex flex-wrap items-center gap-2">
          <GradeSelector compact={true} />
          <SubjectBar compact={true} />
        </div>
      </div>

      {/* Stepper Progress Bar */}
      <AnimatedCard className="p-5 flex items-center justify-between gap-4">
        <div>
          <span className="text-xs font-mono font-bold text-cyan-400 uppercase tracking-wide">
            Skill Check · Question {currentIndex + 1} of {questions.length}
          </span>
          <div className="w-48 sm:w-80 bg-slate-900 h-2.5 rounded-full mt-2 overflow-hidden border border-white/[0.08] p-0.5">
            <motion.div
              className="bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 h-full rounded-full"
              style={{ width: `${progressPercent}%` }}
              transition={{ duration: 0.4 }}
            />
          </div>
        </div>
        <div className="flex items-center gap-2 text-xs font-mono font-bold px-3 py-1.5 rounded-xl bg-white/[0.04] border border-white/10 text-slate-300">
          <Clock className="w-3.5 h-3.5 text-cyan-400 animate-pulse" />
          <span>{currentGradeMeta?.name} Diagnostic</span>
        </div>
      </AnimatedCard>

      {/* Question Card */}
      {currentQ && (
        <AnimatedCard
          key={currentQ.id}
          spotlight={true}
          glowColor="cyan"
          className="p-6 sm:p-8 space-y-6"
        >
          <div className="flex items-center justify-between gap-3 pb-4 border-b border-white/[0.08]">
            <div className="flex flex-wrap items-center gap-2">
              <span className="px-2.5 py-1 rounded-lg text-xs font-mono font-black uppercase bg-blue-950/70 text-blue-300 border border-blue-800/60 shadow-glow-sm">
                {currentQ.subject_name || 'STEM'}
              </span>
              <span className="px-3 py-1 rounded-lg text-xs font-bold bg-white/[0.04] text-slate-300 border border-white/10">
                {currentQ.chapter_name}
              </span>
              <span className="text-xs text-slate-400 font-bold">{currentQ.concept_name}</span>
            </div>
            <span className="text-xs px-2.5 py-0.5 rounded-full border border-amber-800/60 text-amber-300 bg-amber-950/60 font-mono capitalize font-bold">
              {currentQ.difficulty}
            </span>
          </div>

          <h2 className="text-lg sm:text-xl font-bold text-white leading-relaxed">
            {currentQ.question_text}
          </h2>

          {/* Options */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
            {currentQ.options.map((opt: any) => {
              const isSelected = currentAnswer.option === opt.id;
              return (
                <button
                  key={opt.id}
                  onClick={() => handleSelectOption(opt.id)}
                  className={`p-4 rounded-2xl text-left border text-sm font-bold transition-all flex items-start gap-3.5 shadow-sm outline-none cursor-pointer ${
                    isSelected
                      ? 'border-cyan-400 bg-cyan-950/70 text-white shadow-glow-cyan ring-1 ring-cyan-400'
                      : 'border-white/[0.08] bg-white/[0.03] text-slate-300 hover:border-white/20 hover:bg-white/[0.06]'
                  }`}
                >
                  <span
                    className={`w-6 h-6 rounded-lg flex items-center justify-center text-xs font-mono font-black shrink-0 ${
                      isSelected
                        ? 'bg-cyan-500 text-slate-950'
                        : 'bg-white/[0.08] text-slate-400 border border-white/10'
                    }`}
                  >
                    {opt.id}
                  </span>
                  <span className="mt-0.5 leading-snug">{opt.text}</span>
                </button>
              );
            })}
          </div>

          {/* Written Reasoning Input */}
          <div>
            <label className="text-xs font-mono font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center gap-2">
              <BrainCircuit className="w-4 h-4 text-cyan-400 animate-pulse" />
              Reasoning Deduction (Assists cognitive model evaluation):
            </label>
            <textarea
              value={currentAnswer.reasoning}
              onChange={(e) => handleReasoningChange(e.target.value)}
              placeholder="e.g. State your governing formula or principle (e.g. F = ma, V = IR, or Le Chatelier's principle)..."
              className="w-full h-20 p-4 rounded-2xl glass-input-dark text-xs resize-none font-medium text-white placeholder-slate-500"
            />
          </div>

          {/* Stepper Navigation Buttons */}
          <div className="flex items-center justify-between pt-4 border-t border-white/[0.08]">
            <GlowButton
              variant="ghost"
              size="sm"
              onClick={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
              disabled={currentIndex === 0}
              icon={ArrowLeft}
            >
              Previous
            </GlowButton>

            {currentIndex < questions.length - 1 ? (
              <GlowButton
                variant="electric"
                size="md"
                onClick={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
                icon={ArrowRight}
              >
                Next Question
              </GlowButton>
            ) : (
              <GlowButton
                variant="electric"
                size="lg"
                onClick={handleSubmitDiagnostic}
                disabled={submitting}
                loading={submitting}
                icon={CheckCircle2}
              >
                {submitting ? 'Analyzing Probes...' : 'Finish Diagnostic'}
              </GlowButton>
            )}
          </div>
        </AnimatedCard>
      )}
    </AnimatedPage>
  );
};
