import React, { useState, useEffect, useMemo, useCallback } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
  Node,
  Edge
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import {
  Network,
  Zap,
  X,
  ArrowRight,
  AlertTriangle,
  Sparkles,
  BookOpen,
  Filter,
  Layers,
  GraduationCap
} from 'lucide-react';
import { ConceptNode } from '../components/ConceptNode';
import { api } from '../services/api';
import { GraphNodeData } from '../types';
import { useSubject } from '../context/SubjectContext';
import { useGrade } from '../context/GradeContext';
import { SubjectBar } from '../components/SubjectBar';
import { GradeSelector } from '../components/GradeSelector';
import { GlowButton } from '../components/animations/GlowButton';
import { AnimatedCard } from '../components/animations/AnimatedCard';

export const ConceptGraphPage: React.FC = () => {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const { selectedSubject, setSelectedSubject, currentSubjectMeta } = useSubject();
  const { selectedGrade, currentGradeMeta } = useGrade();

  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [allNodes, setAllNodes] = useState<Node[]>([]);
  const [allEdges, setAllEdges] = useState<Edge[]>([]);
  const [chapters, setChapters] = useState<any[]>([]);
  const [selectedChapter, setSelectedChapter] = useState<string>('all');
  const [selectedNodeData, setSelectedNodeData] = useState<GraphNodeData | null>(null);
  const [loading, setLoading] = useState(true);

  const nodeTypes = useMemo(() => ({ conceptNode: ConceptNode }), []);

  // Sync with searchParams if provided
  useEffect(() => {
    const urlSubj = searchParams.get('subject_id');
    if (urlSubj && urlSubj !== selectedSubject) {
      setSelectedSubject(urlSubj);
    }
  }, [searchParams]);

  useEffect(() => {
    async function loadGraph() {
      setLoading(true);
      try {
        const res = await api.getConceptGraph({
          grade: selectedGrade,
          subject_id: selectedSubject !== 'all' ? selectedSubject : undefined,
        });

        // Add glowing neon styles to edges for dark mode
        const styledEdges = (res.edges || []).map((e: Edge) => ({
          ...e,
          animated: true,
          style: {
            stroke: 'rgba(56, 189, 248, 0.45)',
            strokeWidth: 2,
          },
        }));

        setAllNodes(res.nodes || []);
        setAllEdges(styledEdges);
        setNodes(res.nodes || []);
        setEdges(styledEdges);
        setChapters(res.chapters || []);
        setSelectedChapter('all');
      } catch (err) {
        console.error('Failed to load concept graph:', err);
      } finally {
        setLoading(false);
      }
    }
    loadGraph();
  }, [selectedGrade, selectedSubject]);

  const handleFilterChapter = (chapterId: string) => {
    setSelectedChapter(chapterId);
    if (chapterId === 'all') {
      setNodes(allNodes);
      setEdges(allEdges);
    } else {
      const filteredNodes = allNodes.filter((n: any) => n.data.chapter_id === chapterId);
      const filteredNodeIds = new Set(filteredNodes.map((n: any) => n.id));
      const filteredEdges = allEdges.filter(
        (e: any) => filteredNodeIds.has(e.source) && filteredNodeIds.has(e.target)
      );
      setNodes(filteredNodes);
      setEdges(filteredEdges);
    }
  };

  const onNodeClick = useCallback((_: React.MouseEvent, node: Node) => {
    setSelectedNodeData(node.data as unknown as GraphNodeData);
  }, []);

  const title =
    selectedSubject === 'all'
      ? `${currentGradeMeta?.name} All Subjects Knowledge Map`
      : `${currentGradeMeta?.name} ${selectedSubject.charAt(0).toUpperCase() + selectedSubject.slice(1)} Knowledge Map`;

  return (
    <div className="h-[calc(100vh-4rem)] flex flex-col font-sans relative overflow-hidden bg-[#030712] text-slate-100">
      {/* Top Filter and Controls Bar */}
      <div className="z-10 px-4 sm:px-6 py-3 border-b border-white/[0.08] bg-[#070c18]/90 backdrop-blur-xl flex flex-col md:flex-row md:items-center justify-between gap-3 shadow-glass-card">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-cyan-950/80 border border-cyan-800/60 flex items-center justify-center text-cyan-400 shadow-glow-cyan animate-pulse">
            <Network className="w-5 h-5" />
          </div>
          <div>
            <h1 className="text-base font-extrabold text-white tracking-tight">{title}</h1>
            <p className="text-xs text-slate-400 font-medium">
              {allNodes.length} Concepts connected · Interactive prerequisite topology
            </p>
          </div>
        </div>

        {/* Global Grade & Subject Selector */}
        <div className="flex items-center gap-2 overflow-x-auto">
          <GradeSelector compact={true} />
          <SubjectBar compact={true} />
        </div>
      </div>

      {/* Secondary Chapter Filter Sub-bar */}
      {chapters.length > 0 && (
        <div className="z-10 px-4 sm:px-6 py-2 bg-slate-950/60 border-b border-white/[0.06] flex items-center gap-1.5 overflow-x-auto no-scrollbar text-xs">
          <span className="text-[10px] font-mono font-bold text-slate-400 uppercase tracking-wider shrink-0 flex items-center gap-1">
            <Filter className="w-3 h-3 text-cyan-400" /> Chapter:
          </span>
          <button
            onClick={() => handleFilterChapter('all')}
            className={`px-3 py-1 rounded-xl font-bold font-mono transition-all shrink-0 ${
              selectedChapter === 'all'
                ? 'bg-cyan-500 text-slate-950 shadow-glow-sm'
                : 'text-slate-400 hover:text-white hover:bg-white/[0.04]'
            }`}
          >
            All Chapters ({chapters.length})
          </button>
          {chapters.map((ch) => (
            <button
              key={ch.id}
              onClick={() => handleFilterChapter(ch.id)}
              className={`px-3 py-1 rounded-xl font-bold font-mono transition-all shrink-0 max-w-[200px] truncate ${
                selectedChapter === ch.id
                  ? 'bg-cyan-500 text-slate-950 shadow-glow-sm'
                  : 'text-slate-400 hover:text-white hover:bg-white/[0.04]'
              }`}
            >
              {ch.title}
            </button>
          ))}
        </div>
      )}

      {/* React Flow Interactive Graph Canvas */}
      <div className="flex-1 w-full h-full relative z-0">
        {loading ? (
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="w-12 h-12 border-4 border-cyan-500/20 border-t-cyan-400 rounded-full animate-spin shadow-glow-cyan" />
          </div>
        ) : (
          <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            nodeTypes={nodeTypes}
            onNodeClick={onNodeClick}
            fitView
            attributionPosition="bottom-left"
          >
            <Background color="rgba(56, 189, 248, 0.1)" gap={28} size={1.5} />
            <Controls className="!bg-slate-900/90 !border-white/10 !rounded-xl !shadow-glass-card overflow-hidden !text-slate-200" />
            <MiniMap
              nodeColor={(n: any) => {
                const s = n.data?.status;
                if (s === 'mastered') return '#10b981';
                if (s === 'learning') return '#38bdf8';
                if (s === 'needs_improvement') return '#f59e0b';
                return '#f43f5e';
              }}
              className="!bg-slate-900/90 !border-white/10 !rounded-xl !shadow-glass-card"
            />
          </ReactFlow>
        )}
      </div>

      {/* Floating Concept Inspector Drawer */}
      {selectedNodeData && (
        <div className="absolute top-24 right-4 sm:right-6 z-20 w-84 sm:w-96 glass-panel-dark rounded-3xl p-6 border border-white/10 shadow-glass-card-hover animate-in fade-in slide-in-from-right duration-300">
          <div className="flex items-start justify-between pb-3 border-b border-white/[0.08]">
            <div>
              <div className="flex items-center gap-1.5">
                <span className="text-[10px] font-mono font-bold text-cyan-300 uppercase tracking-widest px-2 py-0.5 rounded-md bg-cyan-950/80 border border-cyan-800/60 shadow-glow-sm">
                  {selectedNodeData.subject_name || 'STEM'}
                </span>
                <span className="text-[10px] font-bold text-slate-400 truncate max-w-[150px]">
                  {selectedNodeData.chapter_name}
                </span>
              </div>
              <h3 className="text-base font-extrabold text-white mt-1">
                {selectedNodeData.label}
              </h3>
            </div>
            <button
              onClick={() => setSelectedNodeData(null)}
              className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-white/[0.06] transition-colors"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          <div className="py-4 space-y-3 text-xs">
            {selectedNodeData.formula && (
              <div className="p-3 rounded-xl bg-white/[0.04] border border-white/[0.08] font-mono">
                <span className="text-slate-400 font-medium">Core Principle / Formula: </span>
                <span className="font-bold text-cyan-300 block mt-1">{selectedNodeData.formula}</span>
              </div>
            )}

            <div className="flex items-center justify-between py-1.5 border-b border-white/[0.06]">
              <span className="text-slate-400 font-medium">Mastery Level</span>
              <span className="font-extrabold font-mono text-cyan-400 text-sm">
                {selectedNodeData.mastery}%
              </span>
            </div>

            <div className="flex items-center justify-between py-1.5 border-b border-white/[0.06]">
              <span className="text-slate-400 font-medium">Model Confidence</span>
              <span className="font-mono text-white font-bold">
                {Math.round(selectedNodeData.confidence * 100)}%
              </span>
            </div>

            <div className="flex items-center justify-between py-1.5 border-b border-white/[0.06]">
              <span className="text-slate-400 font-medium">Attempts History</span>
              <span className="text-white font-mono font-bold">
                {selectedNodeData.correct_attempts} / {selectedNodeData.total_attempts} Correct
              </span>
            </div>

            {selectedNodeData.misconceptions && selectedNodeData.misconceptions.length > 0 && (
              <div className="p-3 rounded-xl bg-amber-950/40 border border-amber-800/60 text-amber-200">
                <div className="flex items-center gap-1.5 font-bold mb-1 text-amber-300">
                  <AlertTriangle className="w-3.5 h-3.5 text-amber-400" />
                  <span>Flagged Misconception:</span>
                </div>
                <div className="text-[11px] leading-tight font-medium">
                  {selectedNodeData.misconceptions.join(', ')}
                </div>
              </div>
            )}
          </div>

          <GlowButton
            variant="electric"
            size="md"
            onClick={() => navigate(`/arena?concept_id=${selectedNodeData.id}`)}
            icon={Zap}
            className="w-full mt-2"
          >
            Practice Concept in Arena
            <ArrowRight className="w-3.5 h-3.5 ml-1" />
          </GlowButton>
        </div>
      )}
    </div>
  );
};
