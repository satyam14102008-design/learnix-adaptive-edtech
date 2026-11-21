import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { BrainCircuit, Sparkles, Cpu, CheckCircle2 } from 'lucide-react';

interface LoadingStateProps {
  stages?: string[];
  currentStageIndex?: number;
  className?: string;
  subtext?: string;
}

const DEFAULT_STAGES = [
  'Reading student reasoning...',
  'Evaluating misconception vectors...',
  'Updating continuous learner profile...',
  'Synthesizing personalized feedback...',
  'Adapting optimal next challenge...',
];

export const LoadingState: React.FC<LoadingStateProps> = ({
  stages = DEFAULT_STAGES,
  currentStageIndex,
  className = '',
  subtext = 'Powered by Learnix Adaptive Inference',
}) => {
  const [internalStage, setInternalStage] = useState(0);

  useEffect(() => {
    if (currentStageIndex !== undefined) return;
    const interval = setInterval(() => {
      setInternalStage((prev) => (prev + 1) % stages.length);
    }, 1800);
    return () => clearInterval(interval);
  }, [stages.length, currentStageIndex]);

  const activeIndex = currentStageIndex !== undefined ? currentStageIndex : internalStage;

  return (
    <div className={`flex flex-col items-center justify-center p-8 text-center ${className}`}>
      {/* Futuristic Orbiting Core */}
      <div className="relative w-20 h-20 mb-6 flex items-center justify-center">
        {/* Outer Pulsing Glow */}
        <div className="absolute inset-0 rounded-full bg-cyan-500/20 blur-xl animate-pulse-glow" />

        {/* Outer Ring */}
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 6, repeat: Infinity, ease: 'linear' }}
          className="absolute inset-0 rounded-full border border-dashed border-cyan-400/40"
        />

        {/* Middle Counter-Rotating Ring */}
        <motion.div
          animate={{ rotate: -360 }}
          transition={{ duration: 4, repeat: Infinity, ease: 'linear' }}
          className="absolute inset-2 rounded-full border border-violet-400/30"
        >
          <div className="w-2 h-2 rounded-full bg-violet-400 shadow-[0_0_8px_#a78bfa] absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2" />
        </motion.div>

        {/* Center Glowing AI Core */}
        <motion.div
          animate={{ scale: [1, 1.08, 1] }}
          transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
          className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-violet-600 flex items-center justify-center shadow-glow-cyan text-white relative z-10"
        >
          <BrainCircuit className="w-5 h-5 text-white animate-pulse" />
        </motion.div>
      </div>

      {/* Morphing Stage Message */}
      <div className="h-8 flex items-center justify-center">
        <AnimatePresence mode="wait">
          <motion.div
            key={activeIndex}
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={{ duration: 0.25 }}
            className="flex items-center gap-2 text-sm md:text-base font-extrabold text-cyan-300"
          >
            <Sparkles className="w-4 h-4 text-cyan-400 animate-spin [animation-duration:3s]" />
            <span>{stages[activeIndex] || stages[0]}</span>
          </motion.div>
        </AnimatePresence>
      </div>

      <p className="text-xs text-slate-500 font-mono mt-1 tracking-wider uppercase">
        {subtext}
      </p>
    </div>
  );
};
