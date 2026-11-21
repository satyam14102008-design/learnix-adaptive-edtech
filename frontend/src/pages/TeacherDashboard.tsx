import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  GraduationCap,
  Users,
  TrendingUp,
  AlertTriangle,
  Flame,
  BarChart2,
  Plus,
  X,
  Calendar,
  BookOpen,
  CheckCircle2,
  ChevronRight,
  Sparkles,
  ShieldAlert,
  FileSpreadsheet
} from 'lucide-react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell
} from 'recharts';
import { api } from '../services/api';
import { TeacherDashboardData } from '../types';
import { AnimatedPage } from '../components/animations/AnimatedPage';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';
import { AnimatedCounter } from '../components/animations/AnimatedCounter';

export const TeacherDashboard: React.FC = () => {
  const [data, setData] = useState<TeacherDashboardData | null>(null);
  const [heatmapData, setHeatmapData] = useState<any>(null);
  const [activeTab, setActiveTab] = useState<'overview' | 'heatmap' | 'students' | 'assignments'>('overview');
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [selectedStudent, setSelectedStudent] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);

  // New assignment form state
  const [asgTitle, setAsgTitle] = useState('');
  const [asgChapter, setAsgChapter] = useState('electricity');
  const [asgDueDate, setAsgDueDate] = useState('2026-11-28');
  const [creatingAsg, setCreatingAsg] = useState(false);

  useEffect(() => {
    loadAll();
  }, []);

  const loadAll = async () => {
    try {
      const [dash, heat] = await Promise.all([
        api.getTeacherDashboard(),
        api.getConceptGaps()
      ]);
      setData(dash);
      setHeatmapData(heat);
    } catch (err) {
      console.error('Failed to load teacher dashboard:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCreateAssignment = async (e: React.FormEvent) => {
    e.preventDefault();
    setCreatingAsg(true);
    try {
      await api.createAssignment({
        title: asgTitle,
        chapter_id: asgChapter,
        target_concepts: ['c_elec_ohm'],
        due_date: asgDueDate,
      });
      setShowCreateModal(false);
      setAsgTitle('');
      loadAll();
    } catch (err) {
      console.error('Failed to create assignment:', err);
    } finally {
      setCreatingAsg(false);
    }
  };

  if (loading) {
    return (
      <div className="p-16 text-center space-y-3">
        <div className="w-12 h-12 border-4 border-cyan-500/20 border-t-cyan-400 rounded-full animate-spin mx-auto shadow-glow-cyan" />
        <div className="text-xs font-mono font-bold text-slate-400">Loading Cohort Analytics...</div>
      </div>
    );
  }

  const chartData = (data?.chapter_averages || []).map((c) => ({
    name: c.title?.length > 14 ? c.title.slice(0, 14) + '...' : c.title,
    mastery: c.average_mastery,
  }));

  return (
    <AnimatedPage className="p-4 sm:p-8 max-w-6xl mx-auto space-y-6 font-sans">
      {/* Top Banner */}
      <AnimatedCard glowColor="violet" className="p-6 sm:p-8 bg-slate-950/80 border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-6 shadow-glass-card-hover">
        <div className="space-y-2">
          <div className="flex items-center gap-2 text-xs font-mono font-bold text-violet-400 uppercase tracking-widest">
            <GraduationCap className="w-4 h-4" />
            <span>Instructor Diagnostic Cockpit</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
            STEM Cohort Learning Analytics
          </h1>
          <p className="text-slate-400 text-xs sm:text-sm max-w-lg leading-relaxed font-medium">
            Monitor real-time student mastery trajectories, diagnose cluster misconceptions, and dispatch targeted homework assignments.
          </p>
        </div>

        <GlowButton
          variant="electric"
          size="md"
          onClick={() => setShowCreateModal(true)}
          icon={Plus}
          className="shrink-0"
        >
          Create Assignment
        </GlowButton>
      </AnimatedCard>

      {/* KPI Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <AnimatedCard glowColor="blue" className="p-5">
          <div className="flex items-center justify-between text-xs text-slate-400 font-mono font-bold">
            <span>Enrolled Students</span>
            <Users className="w-4 h-4 text-cyan-400" />
          </div>
          <div className="text-2xl font-black text-white mt-2 font-mono">
            <AnimatedCounter value={data?.total_students || 5} />
          </div>
          <div className="text-[11px] text-slate-500 mt-1 font-mono">Class 10-A Section</div>
        </AnimatedCard>

        <AnimatedCard glowColor="emerald" className="p-5">
          <div className="flex items-center justify-between text-xs text-slate-400 font-mono font-bold">
            <span>Class Avg Mastery</span>
            <TrendingUp className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="text-2xl font-black text-emerald-400 mt-2 font-mono">
            <AnimatedCounter value={Math.round(data?.class_average_mastery || 64.2)} suffix="%" />
          </div>
          <div className="text-[11px] text-emerald-400/80 mt-1 font-mono font-bold">+4.2% since diagnostic</div>
        </AnimatedCard>

        <AnimatedCard glowColor="rose" className="p-5">
          <div className="flex items-center justify-between text-xs text-slate-400 font-mono font-bold">
            <span>At-Risk Students</span>
            <AlertTriangle className="w-4 h-4 text-rose-400" />
          </div>
          <div className="text-2xl font-black text-rose-400 mt-2 font-mono">
            <AnimatedCounter value={data?.at_risk_students_count || 1} />
          </div>
          <div className="text-[11px] text-rose-400/80 mt-1 font-mono font-bold">Mastery &lt; 50%</div>
        </AnimatedCard>

        <AnimatedCard glowColor="amber" className="p-5">
          <div className="flex items-center justify-between text-xs text-slate-400 font-mono font-bold">
            <span>Active Streaks</span>
            <Flame className="w-4 h-4 text-amber-400 fill-amber-400" />
          </div>
          <div className="text-2xl font-black text-amber-400 mt-2 font-mono">
            <AnimatedCounter value={data?.active_streaks_count || 4} />
          </div>
          <div className="text-[11px] text-slate-500 mt-1 font-mono">&ge; 3 consecutive days</div>
        </AnimatedCard>
      </div>

      {/* Tab Switcher */}
      <div className="flex items-center gap-2 border-b border-white/[0.08] pb-3 text-xs font-mono font-bold">
        {[
          { id: 'overview', label: 'Overview & Gap Diagnostics' },
          { id: 'heatmap', label: 'Class Topic Matrix' },
          { id: 'students', label: 'Student Cohort' },
          { id: 'assignments', label: `Assignments (${data?.recent_assignments?.length || 2})` },
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            className={`px-4 py-2 rounded-xl transition-all ${
              activeTab === tab.id
                ? 'bg-cyan-950/80 border border-cyan-800/80 text-cyan-300 shadow-glow-cyan font-black'
                : 'text-slate-400 hover:text-white hover:bg-white/[0.04]'
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Tab 1: Overview */}
      {activeTab === 'overview' && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Weakest Concepts */}
            <AnimatedCard glowColor="rose" className="p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-sm font-black text-white flex items-center gap-2">
                  <AlertTriangle className="w-4 h-4 text-rose-400" />
                  Primary Class Concept Gaps
                </h3>
                <span className="text-xs text-slate-400 font-mono">Class Average</span>
              </div>

              <div className="space-y-3">
                {data?.weakest_concepts?.map((c) => (
                  <div
                    key={c.concept_id}
                    className="p-3.5 rounded-2xl bg-white/[0.03] border border-white/[0.08] flex items-center justify-between"
                  >
                    <div>
                      <div className="text-sm font-bold text-white">{c.concept_name}</div>
                      <div className="text-[11px] text-amber-400 mt-0.5 font-mono">
                        {c.students_affected_by_misconception} student(s) hold active misconception
                      </div>
                    </div>
                    <div className="text-sm font-black font-mono text-rose-400 bg-rose-950/80 px-2 py-0.5 rounded-md border border-rose-800/60 shadow-glow-rose">
                      {c.average_mastery}%
                    </div>
                  </div>
                ))}
              </div>
            </AnimatedCard>

            {/* Chapter Mastery Comparison Chart */}
            <AnimatedCard glowColor="cyan" className="p-6">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-sm font-black text-white flex items-center gap-2">
                  <BarChart2 className="w-4 h-4 text-cyan-400" />
                  Chapter Readiness Distribution
                </h3>
                <span className="text-xs text-slate-400 font-mono">Mastery %</span>
              </div>

              <div className="h-60 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                    <XAxis dataKey="name" stroke="#64748b" fontSize={10} tickLine={false} />
                    <YAxis stroke="#64748b" fontSize={10} tickLine={false} domain={[0, 100]} />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: '#0a1020',
                        borderColor: 'rgba(255,255,255,0.1)',
                        borderRadius: '12px',
                        color: '#f8fafc',
                        fontSize: '12px',
                      }}
                    />
                    <Bar dataKey="mastery" radius={[6, 6, 0, 0]}>
                      {chartData.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={entry.mastery >= 70 ? '#10b981' : entry.mastery >= 50 ? '#38bdf8' : '#f43f5e'}
                        />
                      ))}
                    </Bar>
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </AnimatedCard>
          </div>
        </div>
      )}

      {/* Tab 2: Heatmap */}
      {activeTab === 'heatmap' && heatmapData && (
        <AnimatedCard className="p-6 overflow-x-auto">
          <h3 className="text-sm font-black text-white mb-4">
            Curriculum Concept Competency Matrix
          </h3>
          <table className="w-full text-xs font-mono">
            <thead>
              <tr className="border-b border-white/[0.08] text-slate-400">
                <th className="text-left py-2 px-3">Student Name</th>
                {heatmapData.concepts?.slice(0, 6).map((c: any) => (
                  <th key={c.id} className="text-center py-2 px-2 max-w-[100px] truncate">
                    {c.label}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {heatmapData.matrix?.map((row: any) => (
                <tr key={row.student_id} className="border-b border-white/[0.04] hover:bg-white/[0.02]">
                  <td className="py-2.5 px-3 font-bold text-white">{row.student_name}</td>
                  {row.scores?.slice(0, 6).map((sc: any, idx: number) => {
                    const score = Math.round(sc.score);
                    const bg =
                      score >= 75
                        ? 'bg-emerald-950/70 text-emerald-300 border-emerald-800/60'
                        : score >= 50
                        ? 'bg-cyan-950/70 text-cyan-300 border-cyan-800/60'
                        : 'bg-rose-950/70 text-rose-300 border-rose-800/60';
                    return (
                      <td key={idx} className="text-center py-2 px-2">
                        <span className={`px-2 py-0.5 rounded-md border font-bold ${bg}`}>
                          {score}%
                        </span>
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </AnimatedCard>
      )}

      {/* Tab 3: Students */}
      {activeTab === 'students' && (
        <AnimatedCard className="p-6">
          <h3 className="text-sm font-black text-white mb-4">Student Roster</h3>
          <div className="space-y-3">
            {data?.students?.map((s) => (
              <div
                key={s.id}
                className="p-4 rounded-2xl bg-white/[0.03] border border-white/[0.08] flex items-center justify-between"
              >
                <div className="flex items-center gap-3">
                  <div className="w-9 h-9 rounded-xl bg-cyan-950/80 border border-cyan-800/60 flex items-center justify-center text-cyan-400 font-bold font-mono">
                    {s.name.charAt(0)}
                  </div>
                  <div>
                    <div className="text-sm font-bold text-white">{s.name}</div>
                    <div className="text-[11px] text-slate-400 font-mono">Streak: {s.streak_days} days · {s.xp} XP</div>
                  </div>
                </div>
                <div className="flex items-center gap-4">
                  <span className="text-sm font-black font-mono text-cyan-400">
                    {s.mastery}%
                  </span>
                  <GlowButton
                    variant="ghost"
                    size="sm"
                    onClick={() => setSelectedStudent(s)}
                    icon={ChevronRight}
                  >
                    View
                  </GlowButton>
                </div>
              </div>
            ))}
          </div>
        </AnimatedCard>
      )}

      {/* Tab 4: Assignments */}
      {activeTab === 'assignments' && (
        <AnimatedCard className="p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-sm font-black text-white">Active Assignments</h3>
            <GlowButton variant="electric" size="sm" onClick={() => setShowCreateModal(true)} icon={Plus}>
              New
            </GlowButton>
          </div>
          <div className="space-y-3">
            {data?.recent_assignments?.map((a) => (
              <div
                key={a.id}
                className="p-4 rounded-2xl bg-white/[0.03] border border-white/[0.08] flex items-center justify-between"
              >
                <div>
                  <h4 className="text-sm font-bold text-white">{a.title}</h4>
                  <div className="text-[11px] text-slate-400 font-mono mt-0.5">
                    Chapter: {a.chapter_id} · Due: {a.due_date}
                  </div>
                </div>
                <span className="text-xs font-mono font-bold text-cyan-400 bg-cyan-950/60 border border-cyan-800/60 px-2.5 py-1 rounded-xl">
                  {Math.round((a.completed_count / (a.total_assigned || 1)) * 100)}% Complete
                </span>
              </div>
            ))}
          </div>
        </AnimatedCard>
      )}

      {/* Assignment Modal */}
      <AnimatePresence>
        {showCreateModal && (
          <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
            <div className="fixed inset-0 bg-slate-950/80 backdrop-blur-md" onClick={() => setShowCreateModal(false)} />
            <motion.div
              initial={{ scale: 0.92, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.92, opacity: 0 }}
              className="relative w-full max-w-md glass-panel-dark p-6 rounded-3xl border border-white/10 shadow-2xl z-10 space-y-4"
            >
              <div className="flex items-center justify-between pb-3 border-b border-white/[0.08]">
                <h3 className="text-base font-extrabold text-white">Create Cohort Assignment</h3>
                <button onClick={() => setShowCreateModal(false)} className="text-slate-400 hover:text-white">
                  <X className="w-5 h-5" />
                </button>
              </div>

              <form onSubmit={handleCreateAssignment} className="space-y-3 text-xs">
                <div>
                  <label className="text-slate-300 font-bold block mb-1">Assignment Title</label>
                  <input
                    type="text"
                    required
                    value={asgTitle}
                    onChange={(e) => setAsgTitle(e.target.value)}
                    placeholder="e.g. Electricity Practice Diagnostic"
                    className="w-full p-2.5 rounded-xl glass-input-dark text-xs text-white"
                  />
                </div>

                <div>
                  <label className="text-slate-300 font-bold block mb-1">Chapter</label>
                  <select
                    value={asgChapter}
                    onChange={(e) => setAsgChapter(e.target.value)}
                    className="w-full p-2.5 rounded-xl glass-input-dark text-xs text-white bg-slate-900"
                  >
                    <option value="electricity">Electricity</option>
                    <option value="magnetic_effects">Magnetic Effects of Electric Current</option>
                    <option value="light_reflection">Light: Reflection & Refraction</option>
                  </select>
                </div>

                <div>
                  <label className="text-slate-300 font-bold block mb-1">Due Date</label>
                  <input
                    type="date"
                    value={asgDueDate}
                    onChange={(e) => setAsgDueDate(e.target.value)}
                    className="w-full p-2.5 rounded-xl glass-input-dark text-xs text-white"
                  />
                </div>

                <div className="pt-2 flex justify-end gap-2">
                  <GlowButton variant="ghost" size="sm" onClick={() => setShowCreateModal(false)}>
                    Cancel
                  </GlowButton>
                  <GlowButton variant="electric" size="sm" type="submit" loading={creatingAsg}>
                    Deploy to Class
                  </GlowButton>
                </div>
              </form>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </AnimatedPage>
  );
};
