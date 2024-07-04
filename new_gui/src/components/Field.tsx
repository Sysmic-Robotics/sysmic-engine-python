// src/FootballField.tsx
import React from 'react';

interface FieldProps {
  width: number;
  height: number;
}

const Field: React.FC<FieldProps> = ({ width, height }) => {
  const fieldStyle = {
    fill: 'green',
    stroke: 'white',
    strokeWidth: 2
  };

  const lineStyle = {
    stroke: 'white',
    strokeWidth: 2
  };

  return (
    <svg width={width} height={height}>
      {/* Field */}
      <rect width={width} height={height} style={fieldStyle} />

      {/* Center Line */}
      <line x1={width / 2} y1={0} x2={width / 2} y2={height} style={lineStyle} />

      {/* Center Circle */}
      <circle cx={width / 2} cy={height / 2} r={height / 10} style={lineStyle} fill="none" />

      {/* Penalty Areas */}
      <rect x={0} y={height / 4} width={width / 6} height={height / 2} style={lineStyle} fill="none" />
      <rect x={width - width / 6} y={height / 4} width={width / 6} height={height / 2} style={lineStyle} fill="none" />

      {/* Goal Areas */}
      <rect x={0} y={height / 3} width={width / 12} height={height / 3} style={lineStyle} fill="none" />
      <rect x={width - width / 12} y={height / 3} width={width / 12} height={height / 3} style={lineStyle} fill="none" />

      {/* Goals */}
      <rect x={-10} y={height / 2.5} width={10} height={height / 5} style={lineStyle} fill="none" />
      <rect x={width} y={height / 2.5} width={10} height={height / 5} style={lineStyle} fill="none" />
    </svg>
  );
};

export default Field;