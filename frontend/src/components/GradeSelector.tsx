import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { GraduationCap, Sparkles, BookOpen, ChevronRight } from 'lucide-react';
import { useGrade } from '../context/GradeContext';

interface GradeSelectorProps {
  compact?: boolean;
  className?: string;
}

export const GradeSelector: React.FC<GradeSelectorProps> = ({ compact = false, className = '' }) => {
  const { selectedGrade, setSelectedGrade, grades } = useGrade();
  const [hoveredGrade, setHoveredGrade] = useState<number | null>(null);

  const getGradeGradient = (grade: number) => {
    switch (grade) {
      case 9:
        return 'from-emerald-500 to-teal-600 shadow-glow-emerald';
      case 10:
        return 'from-blue-600 to-indigo-600 shadow-glow-blue';
      case 11:
        return 'from-violet-600 to-purple-600 shadow-glow-violet';
      case 12:
        return 'from-amber-500 to-orange-600 shadow-glow-amber';
      default:
        return 'from-cyan-500 to-blue-600 shadow-glow-cyan';
    }
  };

  return (
    <div className={`relative flex items-center ${className}`}>
      {/* 3D Glass Pill Container */}
      <motion.div
        initial={{ opacity: 0, y: -8 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
        className="flex items-center gap-1.5 p-1.5 bg-slate-900/75 backdrop-blur-2xl border border-white/10 rounded-2xl shadow-glass-card relative z-20"
      >
        {grades.map((g) => {
          const isSelected = selectedGrade === g.grade;
          const grad = getGradeGradient(g.grade);

          return (
            <motion.button
              key={g.id}
              onClick={() => setSelectedGrade(g.grade)}
              onMouseEnter={() => setHoveredGrade(g.grade)}
              onMouseLeave={() => setHoveredGrade(null)}
              whileHover={{ y: -1.5, scale: 1.02 }}
              whileTap={{ scale: 0.96 }}
              transition={{ type: 'spring', stiffness: 500, damping: 30 }}
              className={`relative px-3.5 py-1.5 rounded-xl font-bold text-xs tracking-tight transition-colors duration-200 flex items-center gap-2 select-none outline-none ${
                isSelected ? 'text-white' : 'text-slate-400 hover:text-white hover:bg-white/[0.06]'
              }`}
            >
              {/* Active Animated Background Morph */}
              {isSelected && (
                <motion.div
                  layoutId="activeGradeBackground"
                  className={`absolute inset-0 rounded-xl bg-gradient-to-r ${grad}`}
                  transition={{ type: 'spring', stiffness: 450, damping: 32 }}
                >
                  {/* Subtle top reflection sheen */}
                  <div className="absolute inset-x-0 top-0 h-1/2 bg-white/20 rounded-t-xl" />
                </motion.div>
              )}

              {/* Pill Content */}
              <span className="relative z-10 flex items-center gap-1.5">
                <span
                  className={`w-1.5 h-1.5 rounded-full transition-all duration-300 ${
                    isSelected
                      ? 'bg-white shadow-[0_0_8px_white] scale-125'
                      : g.grade === 9
                      ? 'bg-emerald-400'
                      : g.grade === 10
                      ? 'bg-blue-400'
                      : g.grade === 11
                      ? 'bg-violet-400'
                      : 'bg-amber-400'
                  }`}
                />
                <span className="font-extrabold tracking-tight">{g.name}</span>

                {!compact && (
                  <span
                    className={`text-[10px] font-semibold px-1.5 py-0.5 rounded-md transition-colors ${
                      isSelected ? 'bg-white/20 text-white' : 'bg-white/[0.06] text-slate-400'
                    }`}
                  >
                    {g.badge}
                  </span>
                )}
              </span>
            </motion.button>
          );
        })}
      </motion.div>

      {/* Floating Details Tooltip Card when hovering a grade */}
      <AnimatePresence>
        {hoveredGrade && (
          <motion.div
            initial={{ opacity: 0, y: 10, scale: 0.96 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 8, scale: 0.96 }}
            transition={{ duration: 0.2 }}
            className="absolute top-full left-0 mt-2.5 w-72 bg-slate-900/95 backdrop-blur-2xl rounded-2xl p-4 shadow-glass-card-hover border border-white/10 z-30 pointer-events-none"
          >
            {(() => {
              const preview = grades.find((g) => g.grade === hoveredGrade);
              if (!preview) return null;
              return (
                <div className="space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="font-extrabold text-sm text-white">{preview.name} Syllabus</span>
                    <span className="text-[10px] font-mono text-cyan-400 bg-cyan-950/60 border border-cyan-800/60 px-2 py-0.5 rounded-full font-bold">
                      {preview.total_chapters || 4} Chapters
                    </span>
                  </div>
                  <p className="text-xs text-slate-300 leading-relaxed">{preview.description}</p>
                  <div className="pt-2 border-t border-white/[0.08] flex items-center justify-between text-[11px] text-slate-400 font-medium">
                    <span>Target Mastery</span>
                    <span className="font-mono text-emerald-400 font-bold">{preview.average_mastery}%</span>
                  </div>
                </div>
              );
            })()}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};
