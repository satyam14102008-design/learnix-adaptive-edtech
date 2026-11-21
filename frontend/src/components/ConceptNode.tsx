import React, { memo } from 'react';
import { Handle, Position } from '@xyflow/react';
import { GraphNodeData } from '../types';
import { Sparkles, AlertCircle, CheckCircle2 } from 'lucide-react';

export const ConceptNode = memo(({ data, selected }: { data: GraphNodeData; selected?: boolean }) => {
  const getStatusColor = (status: string) => {
    switch (status) {
      case 'mastered':
        return {
          border: 'border-emerald-500/40 hover:border-emerald-400',
          bg: 'bg-slate-950/85 hover:bg-slate-900/95',
          badge: 'bg-emerald-950/80 text-emerald-300 border-emerald-700/60 shadow-glow-emerald',
          glow: 'shadow-[0_8px_25px_-5px_rgba(16,185,129,0.25)]',
          dot: 'bg-emerald-400',
        };
      case 'learning':
        return {
          border: 'border-cyan-500/40 hover:border-cyan-400',
          bg: 'bg-slate-950/85 hover:bg-slate-900/95',
          badge: 'bg-cyan-950/80 text-cyan-300 border-cyan-700/60 shadow-glow-cyan',
          glow: 'shadow-[0_8px_25px_-5px_rgba(6,182,212,0.25)]',
          dot: 'bg-cyan-400',
        };
      case 'needs_improvement':
        return {
          border: 'border-amber-500/40 hover:border-amber-400',
          bg: 'bg-slate-950/85 hover:bg-slate-900/95',
          badge: 'bg-amber-950/80 text-amber-300 border-amber-700/60 shadow-glow-amber',
          glow: 'shadow-[0_8px_25px_-5px_rgba(245,158,11,0.25)]',
          dot: 'bg-amber-400',
        };
      case 'weak':
      default:
        return {
          border: 'border-rose-500/40 hover:border-rose-400',
          bg: 'bg-slate-950/85 hover:bg-slate-900/95',
          badge: 'bg-rose-950/80 text-rose-300 border-rose-700/60 shadow-glow-rose',
          glow: 'shadow-[0_8px_25px_-5px_rgba(244,63,94,0.25)]',
          dot: 'bg-rose-400',
        };
    }
  };

  const colors = getStatusColor(data.status);

  return (
    <div
      className={`relative px-4 py-3.5 rounded-2xl border backdrop-blur-2xl transition-all duration-300 min-w-[210px] max-w-[270px] cursor-pointer shadow-glass-card ${
        colors.border
      } ${colors.bg} ${colors.glow} ${
        selected
          ? 'ring-2 ring-cyan-400 scale-105 shadow-glow-cyan'
          : 'hover:-translate-y-1 hover:scale-102 hover:border-white/20'
      }`}
    >
      {/* React Flow Handles for Directed Graph Edges */}
      <Handle
        type="target"
        position={Position.Top}
        className="!w-2.5 !h-2.5 !bg-cyan-400 !border-2 !border-slate-900 shadow-glow-sm"
      />
      <Handle
        type="source"
        position={Position.Bottom}
        className="!w-2.5 !h-2.5 !bg-indigo-400 !border-2 !border-slate-900 shadow-glow-sm"
      />

      {/* Top Meta Line: Subject/Chapter and Mastery Score */}
      <div className="flex items-center justify-between gap-2 mb-1.5">
        <span className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider truncate flex items-center gap-1.5">
          <span className={`w-2 h-2 rounded-full ${colors.dot} animate-pulse`} />
          <span className="text-cyan-400 font-bold">
            {data.subject_name ? `${data.subject_name} · ` : ''}
          </span>
          <span className="truncate text-slate-400">{data.chapter_name || 'Topic'}</span>
        </span>
        <span className={`px-2 py-0.5 rounded-full text-[10px] font-mono font-extrabold border ${colors.badge}`}>
          {data.mastery}%
        </span>
      </div>

      {/* Concept Name */}
      <div className="text-xs font-bold text-white leading-snug line-clamp-2">
        {data.label}
      </div>

      {/* Formula Pill */}
      {data.formula && (
        <div className="mt-2 text-[10px] font-mono font-bold text-cyan-300 bg-white/[0.04] px-2.5 py-1 rounded-lg border border-white/[0.08] truncate">
          {data.formula}
        </div>
      )}

      {/* Misconception Alert Tag */}
      {data.misconceptions && data.misconceptions.length > 0 && (
        <div className="mt-2 flex items-center gap-1.5 text-[10px] text-amber-300 font-bold bg-amber-950/60 px-2 py-1 rounded-lg border border-amber-800/60 shadow-glow-amber animate-pulse">
          <AlertCircle className="w-3.5 h-3.5 text-amber-400 shrink-0" />
          <span className="truncate">Misconception flagged</span>
        </div>
      )}
    </div>
  );
});
