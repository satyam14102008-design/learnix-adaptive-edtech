import React, { useEffect, useState } from 'react';
import { motion, useSpring, useTransform } from 'framer-motion';

interface AnimatedCounterProps {
  value: number;
  duration?: number;
  className?: string;
  prefix?: string;
  suffix?: string;
}

export const AnimatedCounter: React.FC<AnimatedCounterProps> = ({
  value,
  duration = 1.2,
  className = '',
  prefix = '',
  suffix = '',
}) => {
  const spring = useSpring(0, {
    duration: duration * 1000,
    bounce: 0,
  });

  const display = useTransform(spring, (latest) => Math.round(latest));
  const [currentVal, setCurrentVal] = useState<number>(0);

  useEffect(() => {
    spring.set(value);
  }, [value, spring]);

  useEffect(() => {
    const unsubscribe = display.on('change', (latest) => {
      setCurrentVal(latest);
    });
    return () => unsubscribe();
  }, [display]);

  return (
    <span className={`tabular-nums ${className}`}>
      {prefix}
      {currentVal.toLocaleString()}
      {suffix}
    </span>
  );
};
