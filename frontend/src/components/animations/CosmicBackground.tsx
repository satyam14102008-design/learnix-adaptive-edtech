import React from 'react';

interface CosmicBackgroundProps {
  className?: string;
}

export const CosmicBackground: React.FC<CosmicBackgroundProps> = ({ className = '' }) => {
  return (
    <div className={`fixed inset-0 pointer-events-none overflow-hidden z-0 bg-[#030712] ${className}`}>
      {/* Subtle Linear-style Grid Pattern */}
      <div className="absolute inset-0 bg-grid-subtle opacity-70" />

      {/* Ambient Radial Gradient Glows */}
      <div className="absolute -top-40 left-1/4 w-[600px] h-[600px] bg-blue-600/10 rounded-full blur-[140px] pointer-events-none" />
      <div className="absolute top-1/3 -right-40 w-[550px] h-[550px] bg-violet-600/10 rounded-full blur-[140px] pointer-events-none" />
      <div className="absolute -bottom-40 left-1/3 w-[650px] h-[650px] bg-cyan-600/10 rounded-full blur-[140px] pointer-events-none" />

      {/* Top subtle vignette */}
      <div className="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-[#030712]/80 pointer-events-none" />
    </div>
  );
};
