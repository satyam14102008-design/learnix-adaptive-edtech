import React from 'react';
import { motion, useReducedMotion } from 'framer-motion';

interface AnimatedPageProps {
  children: React.ReactNode;
  className?: string;
}

export const AnimatedPage: React.FC<AnimatedPageProps> = ({ children, className = '' }) => {
  const shouldReduceMotion = useReducedMotion();

  return (
    <motion.div
      initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 12 }}
      animate={{
        opacity: 1,
        y: 0,
        transition: {
          duration: 0.35,
          ease: 'easeOut',
        },
      }}
      exit={{
        opacity: 0,
        y: shouldReduceMotion ? 0 : -8,
        transition: {
          duration: 0.2,
          ease: 'easeIn',
        },
      }}
      className={`min-h-full ${className}`}
    >
      {children}
    </motion.div>
  );
};
