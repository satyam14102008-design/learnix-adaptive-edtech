import React from 'react';
import { motion, useReducedMotion } from 'framer-motion';

interface RevealSectionProps {
  children: React.ReactNode;
  delay?: number;
  className?: string;
  id?: string;
}

export const RevealSection: React.FC<RevealSectionProps> = ({
  children,
  delay = 0,
  className = '',
  id,
}) => {
  const shouldReduceMotion = useReducedMotion();

  return (
    <motion.section
      id={id}
      initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-50px' }}
      transition={{ duration: 0.5, delay, ease: 'easeOut' }}
      className={className}
    >
      {children}
    </motion.section>
  );
};
