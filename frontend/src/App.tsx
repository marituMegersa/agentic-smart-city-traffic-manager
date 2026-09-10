import React, { useState } from 'react';

export default function App() {
  const [prompt, setPrompt] = useState('');
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleRunAgent = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch('http://localhost:8000/api/v1/agent/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Agentic AI Smart City Traffic & Mobility Manager</h1>
      <p style={{ color: '#666' }}>Autonomous urban traffic flow controller, congestion forecasting agent, and emergency vehicle routing manager.</p>
      
      <form onSubmit={handleRunAgent} style={{ marginTop: '1.5rem' }}>
        <input
          type="text"
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          placeholder="Enter prompt or query for the Agent..."
          style={{ width: '100%', padding: '0.75rem', borderRadius: '6px', border: '1px solid #ccc' }}
          required
        />
        <button
          type="submit"
          disabled={loading}
          style={{ marginTop: '1rem', padding: '0.75rem 1.5rem', background: '#0d9488', color: '#fff', border: 'none', borderRadius: '6px', cursor: 'pointer' }}
        >
          {loading ? 'Agent Executing...' : 'Run Agentic Task'}
        </button>
      </form>

      {result && (
        <div style={{ marginTop: '2rem', padding: '1rem', background: '#f0fdfa', border: '1px solid #99f6e4', borderRadius: '8px' }}>
          <h3>Agent Execution Output</h3>
          <pre style={{ background: '#fff', padding: '1rem', borderRadius: '4px' }}>
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
