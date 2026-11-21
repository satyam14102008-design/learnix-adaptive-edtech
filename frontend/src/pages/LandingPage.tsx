import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Zap,
  ArrowRight,
  CheckCircle2,
  Sparkles,
  HelpCircle,
  GraduationCap,
  BrainCircuit,
  Target,
  RotateCcw,
  Network,
  ChevronRight,
  FlaskConical,
  Dna,
  Sigma,
  Layers,
  Cpu,
  BarChart3,
  Play,
  Pause
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { CosmicBackground } from '../components/animations/CosmicBackground';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';
import { AnimatedCounter } from '../components/animations/AnimatedCounter';
import { MasteryRing } from '../components/animations/MasteryRing';
import { RevealSection } from '../components/animations/RevealSection';

export const LandingPage: React.FC = () => {
  const navigate = useNavigate();
  const { demoLogin } = useAuth();

  // Interactive Live Question Demo State
  const [selectedOpt, setSelectedOpt] = useState<string | null>(null);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [demoMastery, setDemoMastery] = useState(42);

  // Learner Model Interactive Stage (1: Concept, 2: Student Answer, 3: AI Analysis, 4: Mastery Update, 5: Next Question)
  const [activeCycleStep, setActiveCycleStep] = useState(1);
  const [isAutoCycle, setIsAutoCycle] = useState(true);

  useEffect(() => {
    if (!isAutoCycle) return;
    const interval = setInterval(() => {
      setActiveCycleStep((prev) => (prev % 5) + 1);
    }, 2800);
    return () => clearInterval(interval);
  }, [isAutoCycle]);

  const handleDemoAnswerSubmit = () => {
    if (!selectedOpt) return;
    setIsSubmitted(true);
    if (selectedOpt === 'B') {
      setDemoMastery(58);
    } else {
      setDemoMastery(34);
    }
  };

  const handleQuickDemo = async (role: 'student' | 'teacher') => {
    await demoLogin(role);
    if (role === 'teacher') {
      navigate('/teacher');
    } else {
      navigate('/dashboard');
    }
  };

  const cycleSteps = [
    {
      step: 1,
      title: 'Target Concept',
      desc: 'Pinpoints prerequisites & core knowledge nodes',
      icon: Network,
      color: 'from-cyan-500 to-blue-500',
      activeColor: 'border-cyan-400 text-cyan-300 shadow-glow-cyan',
    },
    {
      step: 2,
      title: 'Student Answer',
      desc: 'Captures choices and multi-step written reasoning',
      icon: Target,
      color: 'from-blue-500 to-indigo-500',
      activeColor: 'border-blue-400 text-blue-300 shadow-glow-blue',
    },
    {
      step: 3,
      title: 'AI Analysis',
      desc: 'Parses misconception patterns & reasoning traps',
      icon: BrainCircuit,
      color: 'from-indigo-500 to-violet-500',
      activeColor: 'border-violet-400 text-violet-300 shadow-glow-violet',
    },
    {
      step: 4,
      title: 'Mastery Update',
      desc: 'Calculates continuous BKT & IRT ability vectors',
      icon: Sparkles,
      color: 'from-violet-500 to-pink-500',
      activeColor: 'border-pink-400 text-pink-300 shadow-glow-rose',
    },
    {
      step: 5,
      title: 'Next Question',
      desc: 'Serves zone of proximal development challenges',
      icon: Zap,
      color: 'from-pink-500 to-cyan-500',
      activeColor: 'border-emerald-400 text-emerald-300 shadow-glow-emerald',
    },
  ];

  return (
    <div className="min-h-screen bg-[#030712] text-slate-100 font-sans selection:bg-cyan-500/25 selection:text-cyan-300 overflow-x-hidden relative">
      {/* Background Ambient Grid & Glowing Orbs */}
      <CosmicBackground />

      {/* Top Navigation */}
      <nav className="relative z-30 border-b border-white/[0.08] bg-[#070c18]/80 backdrop-blur-2xl">
        <div className="max-w-6xl mx-auto px-6 h-18 flex items-center justify-between">
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => navigate('/')}>
            <motion.div
              whileHover={{ rotate: 12, scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
              className="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-violet-600 flex items-center justify-center shadow-glow-cyan text-white"
            >
              <Zap className="w-5 h-5 fill-white" />
            </motion.div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-xl tracking-tight text-white">Learnix</span>
              <span className="text-[10px] font-black font-mono px-2 py-0.5 rounded-md bg-gradient-to-r from-cyan-500 to-blue-600 text-white shadow-glow-sm">
                AI
              </span>
            </div>
          </div>

          <div className="hidden md:flex items-center gap-7 text-xs font-mono font-bold tracking-wider uppercase text-slate-400">
            <a href="#learner-model" className="hover:text-cyan-400 transition-colors">Cognitive Model</a>
            <a href="#interactive-demo" className="hover:text-cyan-400 transition-colors">Interactive Demo</a>
            <a href="#curriculum" className="hover:text-cyan-400 transition-colors">STEM Curriculum</a>
          </div>

          <div className="flex items-center gap-3">
            <GlowButton
              variant="electric"
              size="sm"
              onClick={() => handleQuickDemo('student')}
              icon={Zap}
            >
              Start as Student
            </GlowButton>
            <GlowButton
              variant="secondary"
              size="sm"
              onClick={() => handleQuickDemo('teacher')}
              icon={GraduationCap}
              className="hidden sm:inline-flex"
            >
              Teacher View
            </GlowButton>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative pt-20 pb-20 px-6 max-w-5xl mx-auto z-10 text-center">
        {/* Release / Capability Badge */}
        <motion.div
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-950/60 border border-cyan-800/60 text-cyan-300 text-xs font-mono font-bold mb-8 shadow-glow-cyan"
        >
          <Sparkles className="w-3.5 h-3.5 text-cyan-400 animate-spin [animation-duration:5s]" />
          <span>Classes 9 to 12 STEM: Physics · Chemistry · Biology · Mathematics</span>
        </motion.div>

        {/* Massive Premium Headline */}
        <motion.h1
          initial={{ opacity: 0, y: 18 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1, duration: 0.5 }}
          className="text-4xl sm:text-6xl md:text-7xl font-black tracking-tight text-white max-w-4xl mx-auto leading-[1.08]"
        >
          Master Every Concept.{' '}
          <span className="bg-gradient-to-r from-cyan-400 via-blue-500 to-violet-500 bg-clip-text text-transparent">
            Learn at Your Own Pace.
          </span>
        </motion.h1>

        {/* Supporting Text */}
        <motion.p
          initial={{ opacity: 0, y: 18 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.5 }}
          className="mt-6 text-base sm:text-lg text-slate-300 max-w-2xl mx-auto font-medium leading-relaxed"
        >
          An AI tutor that understands how you learn, identifies your knowledge gaps, and builds a personalized path to mastery.
        </motion.p>

        {/* CTA Buttons */}
        <motion.div
          initial={{ opacity: 0, y: 18 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3, duration: 0.5 }}
          className="mt-10 flex flex-wrap items-center justify-center gap-4"
        >
          <GlowButton
            variant="electric"
            size="lg"
            onClick={() => handleQuickDemo('student')}
            icon={Zap}
          >
            Start Learning Free
            <ArrowRight className="w-4 h-4 ml-1" />
          </GlowButton>
          <GlowButton
            variant="secondary"
            size="lg"
            onClick={() => {
              const el = document.getElementById('learner-model');
              el?.scrollIntoView({ behavior: 'smooth' });
            }}
            icon={Network}
          >
            Explore Cognitive Model
          </GlowButton>
        </motion.div>

        {/* Real Metrics Ticker */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4, duration: 0.5 }}
          className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto"
        >
          <AnimatedCard className="p-4 text-center">
            <div className="text-2xl sm:text-3xl font-black font-mono text-cyan-400">
              <AnimatedCounter value={42} />
            </div>
            <div className="text-xs text-slate-400 font-bold mt-1">Chapters (Grades 9-12)</div>
          </AnimatedCard>

          <AnimatedCard className="p-4 text-center">
            <div className="text-2xl sm:text-3xl font-black font-mono text-emerald-400">
              <AnimatedCounter value={120} suffix="+" />
            </div>
            <div className="text-xs text-slate-400 font-bold mt-1">Concepts Mapped</div>
          </AnimatedCard>

          <AnimatedCard className="p-4 text-center">
            <div className="text-2xl sm:text-3xl font-black font-mono text-violet-400">
              <AnimatedCounter value={4} />
            </div>
            <div className="text-xs text-slate-400 font-bold mt-1">STEM Subjects</div>
          </AnimatedCard>

          <AnimatedCard className="p-4 text-center">
            <div className="text-2xl sm:text-3xl font-black font-mono text-amber-400">
              <AnimatedCounter value={100} suffix="%" />
            </div>
            <div className="text-xs text-slate-400 font-bold mt-1">Adaptive Guidance</div>
          </AnimatedCard>
        </motion.div>
      </section>

      {/* Interactive Visual Learner Model Demo */}
      <RevealSection id="learner-model" className="py-20 px-6 max-w-5xl mx-auto z-10">
        <div className="text-center mb-12">
          <span className="text-xs font-mono font-bold text-cyan-400 uppercase tracking-widest">
            Continuous Closed-Loop Feedback
          </span>
          <h2 className="text-2xl sm:text-4xl font-black text-white mt-1.5 tracking-tight">
            The Learnix Adaptive Learner Model
          </h2>
          <p className="text-slate-400 text-sm mt-2 max-w-xl mx-auto font-medium">
            Watch how every keystroke updates your cognitive profile through continuous Bayesian Knowledge Tracing.
          </p>
        </div>

        {/* Multi-Node Stepper Card */}
        <AnimatedCard className="p-6 sm:p-8 border-white/10 bg-slate-950/80 shadow-glass-card-hover">
          {/* Controls Bar */}
          <div className="flex items-center justify-between pb-6 border-b border-white/[0.08] mb-8">
            <div className="flex items-center gap-2">
              <span className="w-2.5 h-2.5 rounded-full bg-cyan-400 shadow-[0_0_8px_#38bdf8] animate-pulse" />
              <span className="text-xs font-mono font-bold text-slate-300 uppercase tracking-wider">
                Live State: Step {activeCycleStep} of 5
              </span>
            </div>
            <button
              onClick={() => setIsAutoCycle(!isAutoCycle)}
              className="flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-mono font-bold bg-white/[0.06] hover:bg-white/[0.1] text-cyan-300 border border-white/10 transition-colors"
            >
              {isAutoCycle ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
              <span>{isAutoCycle ? 'Pause Cycle' : 'Auto Play'}</span>
            </button>
          </div>

          {/* Interactive Steps Grid with Connecting Line */}
          <div className="grid grid-cols-1 md:grid-cols-5 gap-3 relative">
            {cycleSteps.map((s) => {
              const Icon = s.icon;
              const isActive = activeCycleStep === s.step;

              return (
                <div
                  key={s.step}
                  onClick={() => {
                    setActiveCycleStep(s.step);
                    setIsAutoCycle(false);
                  }}
                  className={`p-4 rounded-2xl border transition-all duration-300 cursor-pointer relative ${
                    isActive
                      ? `bg-slate-900/95 border-white/20 ${s.activeColor} scale-102`
                      : 'bg-white/[0.02] border-white/[0.06] text-slate-400 hover:bg-white/[0.05] hover:text-slate-200'
                  }`}
                >
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-[10px] font-mono font-extrabold px-1.5 py-0.5 rounded-md bg-white/[0.08]">
                      0{s.step}
                    </span>
                    <Icon className={`w-4 h-4 ${isActive ? 'text-cyan-400 animate-pulse' : 'text-slate-500'}`} />
                  </div>
                  <h4 className="text-xs font-extrabold text-white tracking-tight">{s.title}</h4>
                  <p className="text-[11px] text-slate-400 mt-1 leading-snug">{s.desc}</p>
                </div>
              );
            })}
          </div>

          {/* Deep Interactive Detail Box */}
          <div className="mt-6 p-4 rounded-2xl bg-white/[0.03] border border-white/[0.08] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="space-y-1">
              <span className="text-[10px] font-mono font-bold text-cyan-400 uppercase tracking-wider">
                Current Engine Transformation
              </span>
              <p className="text-xs text-slate-200 font-medium">
                {activeCycleStep === 1 && "Graph traversal identifies Ohm's Law and Resistivity as active targets in Class 10 Physics."}
                {activeCycleStep === 2 && "Learner selects option B while typing explanation referencing cross-sectional area scaling."}
                {activeCycleStep === 3 && "Gemini reasoning model inspects misconception: validates volume conservation and area reduction."}
                {activeCycleStep === 4 && "Mastery probability rises from 42% to 58% (+16%). Forgetting curve decay reset for 72 hours."}
                {activeCycleStep === 5 && "Adaptive arena queues a Level 3 question on Combination of Resistors in parallel circuits."}
              </p>
            </div>
            <GlowButton
              variant="electric"
              size="sm"
              onClick={() => handleQuickDemo('student')}
              icon={ArrowRight}
              className="shrink-0"
            >
              Test Live
            </GlowButton>
          </div>
        </AnimatedCard>
      </RevealSection>

      {/* Interactive Question Demo Section */}
      <RevealSection id="interactive-demo" className="py-16 px-6 max-w-4xl mx-auto z-10">
        <div className="text-center mb-8">
          <span className="text-xs font-mono font-bold text-cyan-400 uppercase tracking-widest">
            Tactile Practice Experience
          </span>
          <h2 className="text-2xl sm:text-3xl font-black text-white mt-1 tracking-tight">
            Try a Live Question Right Now
          </h2>
          <p className="text-slate-400 text-xs mt-1 font-medium">
            Select an answer to witness live cognitive feedback and mastery updating.
          </p>
        </div>

        <AnimatedCard className="p-6 sm:p-8 bg-slate-950/80 border-white/10 shadow-glass-card-hover">
          <div className="flex items-center justify-between pb-4 border-b border-white/[0.08]">
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-1 rounded-lg text-[11px] font-mono font-bold bg-cyan-950/70 text-cyan-300 border border-cyan-800/60 shadow-glow-sm">
                Electricity · Resistance & Stretch
              </span>
              <span className="px-2 py-0.5 rounded-md text-[10px] font-mono font-bold bg-white/[0.06] text-slate-400">
                Class 10
              </span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-mono text-slate-400">Mastery:</span>
              <span className={`text-sm font-mono font-black ${demoMastery >= 50 ? 'text-emerald-400' : 'text-amber-400'}`}>
                {demoMastery}%
              </span>
            </div>
          </div>

          <div className="py-6">
            <h3 className="text-base sm:text-lg font-bold text-white leading-relaxed">
              A uniform wire has electrical resistance <span className="font-mono text-cyan-300">R</span>. If you stretch it to double its length while preserving constant volume, what is its new resistance?
            </h3>

            {/* Answer Options */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mt-6">
              {[
                { id: 'A', text: '2 R (Resistance simply doubles with length)' },
                { id: 'B', text: '4 R (Length doubles AND cross-section halves)' },
                { id: 'C', text: 'R / 2 (Resistance decreases inversely)' },
                { id: 'D', text: 'Remains R (No change in resistivity of material)' },
              ].map((opt) => (
                <motion.button
                  key={opt.id}
                  whileHover={!isSubmitted ? { scale: 1.015, y: -1 } : {}}
                  whileTap={!isSubmitted ? { scale: 0.98 } : {}}
                  disabled={isSubmitted}
                  onClick={() => setSelectedOpt(opt.id)}
                  className={`p-4 rounded-2xl text-left border text-xs font-bold transition-all flex items-center gap-3 ${
                    selectedOpt === opt.id
                      ? 'border-cyan-400 bg-cyan-950/60 text-white shadow-glow-cyan ring-1 ring-cyan-400'
                      : 'border-white/[0.08] bg-white/[0.03] text-slate-300 hover:bg-white/[0.06] hover:border-white/20'
                  } ${
                    isSubmitted && opt.id === 'B'
                      ? 'border-emerald-400 bg-emerald-950/60 text-emerald-200 ring-2 ring-emerald-400/40'
                      : ''
                  }`}
                >
                  <span
                    className={`w-7 h-7 rounded-xl flex items-center justify-center text-xs font-mono font-black shrink-0 ${
                      selectedOpt === opt.id
                        ? 'bg-cyan-500 text-slate-950'
                        : 'bg-white/[0.08] text-slate-400 border border-white/10'
                    }`}
                  >
                    {opt.id}
                  </span>
                  <span className="leading-snug">{opt.text}</span>
                </motion.button>
              ))}
            </div>

            {/* Action Check Button */}
            <div className="mt-6 flex items-center justify-between">
              {!isSubmitted ? (
                <GlowButton
                  variant="electric"
                  size="md"
                  onClick={handleDemoAnswerSubmit}
                  disabled={!selectedOpt}
                  icon={ArrowRight}
                >
                  Analyze My Answer
                </GlowButton>
              ) : (
                <GlowButton
                  variant="secondary"
                  size="md"
                  onClick={() => {
                    setIsSubmitted(false);
                    setSelectedOpt(null);
                    setDemoMastery(42);
                  }}
                  icon={RotateCcw}
                >
                  Reset Challenge
                </GlowButton>
              )}
            </div>

            {/* Feedback Breakdown */}
            <AnimatePresence>
              {isSubmitted && (
                <motion.div
                  initial={{ opacity: 0, y: 12 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -8 }}
                  className={`mt-5 p-4 rounded-2xl border text-xs leading-relaxed ${
                    selectedOpt === 'B'
                      ? 'border-emerald-500/50 bg-emerald-950/40 text-emerald-200 shadow-glow-emerald'
                      : 'border-rose-500/50 bg-rose-950/40 text-rose-200 shadow-glow-rose'
                  }`}
                >
                  <div className="font-extrabold mb-1.5 flex items-center gap-2 text-sm">
                    {selectedOpt === 'B' ? (
                      <>
                        <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                        <span>Mastery upgraded to 58% (+16%)! Excellent cognitive reasoning.</span>
                      </>
                    ) : (
                      <>
                        <HelpCircle className="w-4 h-4 text-rose-400" />
                        <span>Misconception Detected: Wire thickness changes during stretching!</span>
                      </>
                    )}
                  </div>
                  <p className="text-slate-300">
                    {selectedOpt === 'B'
                      ? 'Since wire volume remains invariant (V = L · A), stretching to 2L halves the cross-sectional area (A/2). From R = ρ·(L/A), (2)/(0.5) = 4R!'
                      : 'Common student trap: Many assume only length changes. But stretching pulls the atoms further apart and narrows the cross-section by half. Combining both gives (2 × 2) = 4R.'}
                  </p>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </AnimatedCard>
      </RevealSection>

      {/* 4 STEM Subjects Across Grades 9-12 */}
      <RevealSection id="curriculum" className="py-20 px-6 max-w-5xl mx-auto z-10 border-t border-white/[0.08]">
        <div className="text-center mb-12">
          <span className="text-xs font-mono font-bold text-cyan-400 uppercase tracking-widest">
            Complete Curriculum Spectrum
          </span>
          <h2 className="text-2xl sm:text-4xl font-black text-white mt-1.5 tracking-tight">
            Classes 9, 10, 11 & 12 STEM Architecture
          </h2>
          <p className="text-slate-400 text-xs sm:text-sm mt-1 max-w-xl mx-auto">
            42 fully connected chapters with granular formula taxonomies, misconception diagnostics, and cross-grade progression.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          {[
            {
              name: 'Physics',
              icon: Zap,
              colorScheme: 'blue' as const,
              badge: 'Mechanics to Modern',
              topics: 'Kinematics, Optics, Electricity, Magnetism, Waves & Quantum',
              chapters: 11,
              glow: 'text-cyan-400',
            },
            {
              name: 'Chemistry',
              icon: FlaskConical,
              colorScheme: 'emerald' as const,
              badge: 'Organic & Inorganic',
              topics: 'Atomic Models, Chemical Bonds, Thermodynamics & Kinetics',
              chapters: 10,
              glow: 'text-emerald-400',
            },
            {
              name: 'Biology',
              icon: Dna,
              colorScheme: 'rose' as const,
              badge: 'Cellular to Genetic',
              topics: 'Cell Structures, Genetics, Biotechnology & Human Systems',
              chapters: 10,
              glow: 'text-rose-400',
            },
            {
              name: 'Mathematics',
              icon: Sigma,
              colorScheme: 'amber' as const,
              badge: 'Calculus to Algebra',
              topics: 'Trigonometry, Calculus, Matrices, Probability & 3D Vectors',
              chapters: 11,
              glow: 'text-amber-400',
            },
          ].map((item) => {
            const Icon = item.icon;
            return (
              <AnimatedCard
                key={item.name}
                glowColor={item.colorScheme}
                className="p-5 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-4">
                    <div className="w-10 h-10 rounded-xl bg-white/[0.06] border border-white/10 flex items-center justify-center">
                      <Icon className={`w-5 h-5 ${item.glow}`} />
                    </div>
                    <span className="text-[10px] font-mono font-bold text-slate-400 px-2 py-0.5 rounded-full bg-white/[0.04] border border-white/[0.08]">
                      {item.chapters} Chapters
                    </span>
                  </div>
                  <h3 className="text-base font-extrabold text-white">{item.name}</h3>
                  <span className="text-[10px] font-mono font-bold text-cyan-400 block mt-0.5">
                    {item.badge}
                  </span>
                  <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                    {item.topics}
                  </p>
                </div>

                <div className="pt-4 mt-4 border-t border-white/[0.06] flex items-center justify-between text-xs font-bold text-slate-300">
                  <span>Grades 9-12</span>
                  <span className="text-cyan-400 flex items-center gap-1 font-mono text-[11px]">
                    Adaptive <ChevronRight className="w-3.5 h-3.5" />
                  </span>
                </div>
              </AnimatedCard>
            );
          })}
        </div>
      </RevealSection>

      {/* Footer */}
      <footer className="border-t border-white/[0.08] py-10 px-6 max-w-5xl mx-auto z-10 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-400 font-medium">
        <div className="flex items-center gap-2">
          <div className="w-6 h-6 rounded-lg bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-white">
            <Zap className="w-3.5 h-3.5 fill-white" />
          </div>
          <span>
            <strong className="text-white">Learnix AI</strong> — Adaptive STEM Learning System (Grades 9-12)
          </span>
        </div>
        <div className="flex items-center gap-5 font-mono text-xs">
          <button
            onClick={() => handleQuickDemo('student')}
            className="hover:text-cyan-400 transition-colors"
          >
            Student View
          </button>
          <button
            onClick={() => handleQuickDemo('teacher')}
            className="hover:text-cyan-400 transition-colors"
          >
            Instructor View
          </button>
          <a
            href="https://github.com"
            target="_blank"
            rel="noreferrer"
            className="text-slate-500 hover:text-slate-300 transition-colors"
          >
            Docs
          </a>
        </div>
      </footer>
    </div>
  );
};
