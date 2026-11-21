import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Zap, ArrowRight, Lock, Mail, BrainCircuit, GraduationCap } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { CosmicBackground } from '../components/animations/CosmicBackground';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';

export const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const { login, demoLogin } = useAuth();

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState<'student' | 'teacher'>('student');
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      await login(email, password);
      navigate(role === 'teacher' ? '/teacher' : '/dashboard');
    } catch (err: any) {
      setError(err.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  const handleQuickDemo = async (demoRole: 'student' | 'teacher') => {
    setLoading(true);
    try {
      await demoLogin(demoRole);
      navigate(demoRole === 'teacher' ? '/teacher' : '/dashboard');
    } catch (err: any) {
      setError(err.message || 'Demo login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#030712] text-slate-100 flex items-center justify-center p-4 font-sans relative selection:bg-cyan-500/20 selection:text-cyan-300 overflow-hidden">
      {/* Background Cosmic Grid */}
      <CosmicBackground />

      <AnimatedCard
        spotlight={true}
        glowColor="cyan"
        className="w-full max-w-md p-8 border-white/10 bg-slate-950/80 shadow-glass-card-hover relative z-10 space-y-6"
      >
        {/* Brand Header */}
        <div className="text-center space-y-2">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-violet-600 flex items-center justify-center mx-auto shadow-glow-cyan text-white">
            <Zap className="w-6 h-6 fill-white" />
          </div>
          <h1 className="text-2xl font-black text-white tracking-tight">
            Welcome to Learnix AI
          </h1>
          <p className="text-xs text-slate-400 font-medium">
            Sign in to access your continuous learner model
          </p>
        </div>

        {/* 1-Click Demo Evaluation Buttons */}
        <div className="p-4 rounded-2xl bg-white/[0.03] border border-white/[0.08] space-y-2.5">
          <div className="text-[10px] font-mono font-bold text-center text-cyan-400 uppercase tracking-widest">
            ⚡ Instant Evaluation Demo Logins
          </div>
          <div className="grid grid-cols-2 gap-2">
            <button
              type="button"
              onClick={() => handleQuickDemo('student')}
              className="py-2.5 px-3 rounded-xl text-xs font-bold bg-cyan-950/70 hover:bg-cyan-900/80 border border-cyan-800/60 text-cyan-300 flex items-center justify-center gap-1.5 shadow-sm transition-all"
            >
              <Zap className="w-3.5 h-3.5 fill-cyan-400" />
              Student (Alex)
            </button>
            <button
              type="button"
              onClick={() => handleQuickDemo('teacher')}
              className="py-2.5 px-3 rounded-xl text-xs font-bold bg-violet-950/70 hover:bg-violet-900/80 border border-violet-800/60 text-violet-300 flex items-center justify-center gap-1.5 shadow-sm transition-all"
            >
              <GraduationCap className="w-3.5 h-3.5" />
              Teacher View
            </button>
          </div>
        </div>

        {error && (
          <div className="p-3 rounded-xl bg-rose-950/60 border border-rose-800/60 text-rose-300 text-xs text-center font-bold font-mono">
            {error}
          </div>
        )}

        {/* Traditional Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-1">
            <label className="text-xs font-mono font-bold text-slate-400">Email Address</label>
            <div className="relative">
              <Mail className="w-4 h-4 text-slate-500 absolute left-3.5 top-3" />
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="alex.chen@learnix.ai"
                className="w-full pl-10 pr-4 py-2.5 rounded-xl glass-input-dark text-xs text-white"
              />
            </div>
          </div>

          <div className="space-y-1">
            <label className="text-xs font-mono font-bold text-slate-400">Password</label>
            <div className="relative">
              <Lock className="w-4 h-4 text-slate-500 absolute left-3.5 top-3" />
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                className="w-full pl-10 pr-4 py-2.5 rounded-xl glass-input-dark text-xs text-white"
              />
            </div>
          </div>

          <GlowButton
            type="submit"
            variant="electric"
            size="md"
            loading={loading}
            icon={ArrowRight}
            className="w-full"
          >
            Sign In to Cockpit
          </GlowButton>
        </form>

        <div className="text-center text-xs text-slate-400">
          Don't have an account?{' '}
          <Link to="/signup" className="text-cyan-400 hover:underline font-bold">
            Create account
          </Link>
        </div>
      </AnimatedCard>
    </div>
  );
};
