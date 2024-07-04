// src/components/FootballPlayer.tsx
import React from 'react';

interface RobotProps {
    id: number;
    team: number; //  0 blue - 1 yellow
    position: {
      x: number;
      y: number;
    };
}

// Define the Robot component
const Robot: React.FC<RobotProps> = ({ id, team, position }) => {
    // Determine the color based on the team
    const color = team === 0 ? 'blue' : 'yellow';

    // Define the styles for the circle
    const circleStyle: React.CSSProperties = {
        width: '20px',
        height: '20px',
        borderRadius: '50%',
        backgroundColor: color,
        position: 'relative',
        left: `${position.x}px`,
        top: `${position.y}px`,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: 'white',
        fontSize: '12px',
    };

    return <div style={circleStyle}>{id}</div>;
};

export default Robot;
