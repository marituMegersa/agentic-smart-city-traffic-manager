import React from 'react';

export const AgentTrajectory: React.FC<{ steps: any[] }> = ({ steps }) => (
  <div style={{ marginTop: '1rem', border: '1px solid #cbd5e1', padding: '1rem', borderRadius: '8px' }}>
    <h4>Agent Trajectory Execution Steps</h4>
    <ul>
      {steps.map((s, idx) => (
        <li key={idx}><strong>Step {s.step}:</strong> {s.action}</li>
      ))}
    </ul>
  </div>
);
