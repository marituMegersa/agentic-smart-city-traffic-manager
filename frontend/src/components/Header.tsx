import React from 'react';

export const Header: React.FC = () => (
  <header style={{ padding: '1rem', background: '#0f172a', color: '#fff', display: 'flex', justifyContent: 'space-between' }}>
    <h2 style={{ margin: 0 }}>agentic-smart-city-traffic-manager</h2>
    <span style={{ fontSize: '12px', background: '#0d9488', padding: '4px 8px', borderRadius: '4px' }}>Agent Status: Ready</span>
  </header>
);
