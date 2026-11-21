import React from 'react';
import { motion } from 'framer-motion';
import { Zap, FlaskConical, Dna, Sigma, Layers } from 'lucide-react';
import { useSubject } from '../context/SubjectContext';

interface SubjectBarProps {
  className?: string;
  compact?: boolean;
}

export const SubjectBar: React.FC<SubjectBarProps> = ({ className = '', compact = false }) => {
  const { selectedSubject, setSelectedSubject, subjects } = useSubject();

  const getSubjectIcon = (id: string) => {
    switch (id) {
      case 'physics':
        return <Zap className="w-3.5 h-3.5" />;
      case 'chemistry':
        return <FlaskConical className="w-3.5 h-3.5" />;
      case 'biology':
        return <Dna className="w-3.5 h-3.5" />;
      case 'mathematics':
        return <Sigma className="w-3.5 h-3.5" />;
      default:
        return <Layers className="w-3.5 h-3.5" />;
    }
  };

  const getActiveGradient = (id: string) => {
    switch (id) {
      case 'physics':
        return 'from-blue-600 via-indigo-600 to-cyan-500 shadow-glow-blue';
      case 'chemistry':
        return 'from-emerald-600 to-teal-500 shadow-glow-emerald';
      case 'biology':
        return 'from-rose-600 to-pink-500 shadow-glow-rose';
      case 'mathematics':
        return 'from-amber-500 to-orange-500 shadow-glow-amber';
      default:
        return 'from-cyan-500 via-blue-600 to-violet-600 shadow-glow-cyan';
    }
  };

  const items = [
    { id: 'all', name: 'All Subjects', mastery: undefined },
    ...subjects.map((s) => ({ id: s.id, name: s.name, mastery: s.average_mastery })),
  ];

  return (
    <motion.div
      initial={{ opacity: 0, y: -6 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      className={`flex items-center gap-1.5 p-1.5 rounded-2xl bg-slate-900/75 border border-white/10 backdrop-blur-2xl shadow-glass-card overflow-x-auto no-scrollbar relative z-10 ${className}`}
    >
      {items.map((item) => {
        const isSelected = selectedSubject === item.id;
        const grad = getActiveGradient(item.id);

        return (
          <motion.button
            key={item.id}
            onClick={() => setSelectedSubject(item.id)}
            whileHover={{ y: -1.5, scale: 1.02 }}
            whileTap={{ scale: 0.96 }}
            transition={{ type: 'spring', stiffness: 500, damping: 30 }}
            className={`relative px-3.5 py-1.5 rounded-xl text-xs font-extrabold flex items-center gap-1.5 shrink-0 transition-colors duration-200 select-none outline-none ${
              isSelected ? 'text-white' : 'text-slate-400 hover:text-white hover:bg-white/[0.06]'
            }`}
          >
            {/* Active Pill Spring Sliding Background */}
            {isSelected && (
              <motion.div
                layoutId="activeSubjectPill"
                className={`absolute inset-0 rounded-xl bg-gradient-to-r ${grad}`}
                transition={{ type: 'spring', stiffness: 450, damping: 32 }}
              >
                {/* Surface Reflection Sheen */}
                <div className="absolute inset-x-0 top-0 h-1/2 bg-white/20 rounded-t-xl" />
              </motion.div>
            )}

            {/* Pill Content */}
            <span className="relative z-10 flex items-center gap-1.5">
              <span className={`transition-transform duration-300 ${isSelected ? 'scale-110' : ''}`}>
                {getSubjectIcon(item.id)}
              </span>
              <span>{item.name}</span>
              {item.mastery !== undefined && !compact && (
                <span
                  className={`ml-1 text-[10px] font-mono px-1.5 py-0.5 rounded-md transition-colors ${
                    isSelected
                      ? 'bg-white/20 text-white font-bold'
                      : 'bg-white/[0.06] text-slate-400 font-semibold'
                  }`}
                >
                  {Math.round(item.mastery)}%
                </span>
              )}
            </span>
          </motion.button>
        );
      })}
    </motion.div>
  );
};
