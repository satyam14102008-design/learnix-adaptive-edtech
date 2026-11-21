import React from 'react';
import { motion } from 'framer-motion';
import { Sparkles, Loader2 } from 'lucide-react';

interface GlowButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  type?: 'button' | 'submit' | 'reset';
  variant?: 'primary' | 'electric' | 'secondary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  disabled?: boolean;
  className?: string;
  icon?: any;
}

export const GlowButton: React.FC<GlowButtonProps> = ({
  children,
  onClick,
  type = 'button',
  variant = 'primary',
  size = 'md',
  loading = false,
  disabled = false,
  className = '',
  icon: Icon,
}) => {
  const getSizeStyles = () => {
    switch (size) {
      case 'sm':
        return 'px-3 py-1.5 text-xs rounded-xl gap-1.5';
      case 'lg':
        return 'px-6 py-3.5 text-sm md:text-base rounded-2xl gap-2.5 font-black';
      case 'md':
      default:
        return 'px-4 py-2 text-xs md:text-sm rounded-xl gap-2 font-bold';
    }
  };

  const getVariantStyles = () => {
    switch (variant) {
      case 'electric':
        return 'bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-600 hover:from-cyan-400 hover:to-indigo-500 text-white shadow-glow-cyan border border-cyan-400/30';
      case 'secondary':
        return 'bg-slate-900/80 hover:bg-slate-800 text-slate-200 hover:text-white border border-white/10 shadow-sm';
      case 'ghost':
        return 'bg-transparent hover:bg-white/[0.06] text-slate-300 hover:text-white border border-transparent';
      case 'danger':
        return 'bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 text-white shadow-glow-rose border border-rose-500/30';
      case 'primary':
      default:
        return 'bg-gradient-to-r from-blue-600 via-indigo-600 to-violet-600 hover:from-blue-500 hover:to-violet-500 text-white shadow-glow-blue border border-blue-400/30';
    }
  };

  return (
    <motion.button
      type={type}
      onClick={onClick}
      disabled={disabled || loading}
      whileHover={disabled || loading ? {} : { scale: 1.025, y: -2 }}
      whileTap={disabled || loading ? {} : { scale: 0.97 }}
      transition={{ type: 'spring', stiffness: 500, damping: 25 }}
      className={`relative inline-flex items-center justify-center select-none outline-none font-sans transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none ${getSizeStyles()} ${getVariantStyles()} ${className}`}
    >
      {/* Top subtle gloss sheen */}
      <span className="absolute inset-x-0 top-0 h-1/2 bg-white/15 rounded-t-xl pointer-events-none" />

      {loading ? (
        <Loader2 className="w-4 h-4 animate-spin text-white" />
      ) : Icon ? (
        <Icon className="w-4 h-4 shrink-0" />
      ) : null}

      <span className="relative z-10 flex items-center gap-1.5">{children}</span>
    </motion.button>
  );
};
