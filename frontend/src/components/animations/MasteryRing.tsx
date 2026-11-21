import React from 'react';
import { motion } from 'framer-motion';

interface MasteryRingProps {
  percentage: number;
  size?: number;
  strokeWidth?: number;
  label?: string;
  showPercentage?: boolean;
  colorScheme?: 'blue' | 'cyan' | 'emerald' | 'violet' | 'amber';
}

export const MasteryRing: React.FC<MasteryRingProps> = ({
  percentage,
  size = 96,
  strokeWidth = 8,
  label,
  showPercentage = true,
  colorScheme = 'cyan',
}) => {
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const validPercentage = Math.min(Math.max(percentage, 0), 100);
  const strokeDashoffset = circumference - (validPercentage / 100) * circumference;

  const getGradientColors = () => {
    switch (colorScheme) {
      case 'emerald':
        return {
          start: '#10b981',
          end: '#06b6d4',
          glow: 'rgba(16, 185, 129, 0.4)',
        };
      case 'violet':
        return {
          start: '#8b5cf6',
          end: '#ec4899',
          glow: 'rgba(139, 92, 246, 0.4)',
        };
      case 'amber':
        return {
          start: '#f59e0b',
          end: '#ef4444',
          glow: 'rgba(245, 158, 11, 0.4)',
        };
      case 'blue':
        return {
          start: '#2563eb',
          end: '#38bdf8',
          glow: 'rgba(37, 99, 235, 0.4)',
        };
      case 'cyan':
      default:
        return {
          start: '#06b6d4',
          end: '#3b82f6',
          glow: 'rgba(6, 182, 212, 0.4)',
        };
    }
  };

  const colors = getGradientColors();
  const gradientId = `ring-grad-${colorScheme}-${size}`;

  return (
    <div className="relative inline-flex flex-col items-center justify-center">
      <div className="relative" style={{ width: size, height: size }}>
        <svg
          width={size}
          height={size}
          viewBox={`0 0 ${size} ${size}`}
          className="transform -rotate-90 origin-center overflow-visible"
        >
          <defs>
            <linearGradient id={gradientId} x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor={colors.start} />
              <stop offset="100%" stopColor={colors.end} />
            </linearGradient>
            <filter id={`glow-${gradientId}`} x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="3" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          {/* Background Track */}
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            fill="transparent"
            stroke="rgba(255, 255, 255, 0.08)"
            strokeWidth={strokeWidth}
          />

          {/* Progress Stroke with Framer Motion Animation */}
          <motion.circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            fill="transparent"
            stroke={`url(#${gradientId})`}
            strokeWidth={strokeWidth}
            strokeDasharray={circumference}
            initial={{ strokeDashoffset: circumference }}
            animate={{ strokeDashoffset }}
            transition={{ duration: 1.4, ease: [0.16, 1, 0.3, 1] }}
            strokeLinecap="round"
            style={{
              filter: `drop-shadow(0 0 6px ${colors.glow})`,
            }}
          />
        </svg>

        {/* Center Percentage Display */}
        {showPercentage && (
          <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
            <span className="font-mono font-black text-white tracking-tight" style={{ fontSize: size * 0.22 }}>
              {Math.round(validPercentage)}%
            </span>
            {label && (
              <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
                {label}
              </span>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
