import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Zap, ArrowRight, Lock, Mail, User as UserIcon } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { CosmicBackground } from '../components/animations/CosmicBackground';
import { AnimatedCard } from '../components/animations/AnimatedCard';
import { GlowButton } from '../components/animations/GlowButton';

export const SignupPage: React.FC = () => {
  const navigate = useNavigate();
  const { signup } = useAuth();

  const [name, setName] = useState('');
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
      await signup(email, password, name, role, 'Class 10');
      navigate(role === 'teacher' ? '/teacher' : '/diagnostic');
    } catch (err: any) {
      setError(err.message || 'Signup failed');
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
        <div className="text-center space-y-2">
          <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-violet-600 flex items-center justify-center mx-auto shadow-glow-cyan text-white">
            <Zap className="w-6 h-6 fill-white" />
          </div>
          <h1 className="text-2xl font-black text-white tracking-tight">
            Create Learnix Account
          </h1>
          <p className="text-xs text-slate-400 font-medium">
            Start mastering Classes 9-12 STEM with continuous AI guidance
          </p>
        </div>

        {error && (
          <div className="p-3 rounded-xl bg-rose-950/60 border border-rose-800/60 text-rose-300 text-xs text-center font-bold font-mono">
            {error}
          </div>
        )}

        {/* Role Toggle */}
        <div className="flex rounded-xl bg-white/[0.04] p-1 border border-white/10 text-xs font-mono font-bold">
          <button
            type="button"
            onClick={() => setRole('student')}
            className={`flex-1 py-2 rounded-lg transition-all ${
              role === 'student'
                ? 'bg-cyan-500 text-slate-950 shadow-glow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            I am a Student
          </button>
          <button
            type="button"
            onClick={() => setRole('teacher')}
            className={`flex-1 py-2 rounded-lg transition-all ${
              role === 'teacher'
                ? 'bg-cyan-500 text-slate-950 shadow-glow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            I am a Teacher
          </button>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="space-y-1">
            <label className="text-xs font-mono font-bold text-slate-400">Full Name</label>
            <div className="relative">
              <UserIcon className="w-4 h-4 text-slate-500 absolute left-3.5 top-3" />
              <input
                type="text"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Alex Chen"
                className="w-full pl-10 pr-4 py-2.5 rounded-xl glass-input-dark text-xs text-white"
              />
            </div>
          </div>

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
                placeholder="At least 6 characters"
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
            Create Account & Begin
          </GlowButton>
        </form>

        <div className="text-center text-xs text-slate-400">
          Already have an account?{' '}
          <Link to="/login" className="text-cyan-400 hover:underline font-bold">
            Sign in
          </Link>
        </div>
      </AnimatedCard>
    </div>
  );
};
