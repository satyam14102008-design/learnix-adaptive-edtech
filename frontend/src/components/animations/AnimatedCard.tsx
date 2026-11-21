import React, { useRef, useState } from 'react';
import { motion } from 'framer-motion';

interface AnimatedCardProps {
  children: React.ReactNode;
  className?: string;
  onClick?: () => void;
  hoverLift?: boolean;
  spotlight?: boolean;
  glowColor?: 'blue' | 'cyan' | 'violet' | 'emerald' | 'amber' | 'rose';
}

export const AnimatedCard: React.FC<AnimatedCardProps> = ({
  children,
  className = '',
  onClick,
  hoverLift = true,
  spotlight = true,
  glowColor = 'blue',
}) => {
  const cardRef = useRef<HTMLDivElement>(null);
  const [mousePos, setMousePos] = useState<{ x: number; y: number }>({ x: 0, y: 0 });
  const [isHovered, setIsHovered] = useState(false);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!cardRef.current || !spotlight) return;
    const rect = cardRef.current.getBoundingClientRect();
    setMousePos({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top,
    });
  };

  const getGlowRgba = () => {
    switch (glowColor) {
      case 'cyan':
        return 'rgba(6, 182, 212, 0.15)';
      case 'violet':
        return 'rgba(139, 92, 246, 0.15)';
      case 'emerald':
        return 'rgba(16, 185, 129, 0.15)';
      case 'amber':
        return 'rgba(245, 158, 11, 0.15)';
      case 'rose':
        return 'rgba(244, 63, 94, 0.15)';
      case 'blue':
      default:
        return 'rgba(56, 189, 248, 0.15)';
    }
  };

  return (
    <motion.div
      ref={cardRef}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      onClick={onClick}
      whileHover={hoverLift ? { y: -4, transition: { duration: 0.25, ease: [0.16, 1, 0.3, 1] } } : {}}
      className={`relative rounded-3xl border border-white/[0.08] bg-slate-950/60 backdrop-blur-xl overflow-hidden transition-all duration-300 shadow-glass-card hover:border-white/[0.18] hover:shadow-glass-card-hover ${
        onClick ? 'cursor-pointer' : ''
      } ${className}`}
    >
      {/* Dynamic Cursor Spotlight Layer */}
      {spotlight && isHovered && (
        <div
          className="pointer-events-none absolute -inset-px transition-opacity duration-300 rounded-3xl"
          style={{
            background: `radial-gradient(400px circle at ${mousePos.x}px ${mousePos.y}px, ${getGlowRgba()}, transparent 70%)`,
          }}
        />
      )}

      {/* Subtle top edge highlight */}
      <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent pointer-events-none" />

      {/* Content */}
      <div className="relative z-10">{children}</div>
    </motion.div>
  );
};
