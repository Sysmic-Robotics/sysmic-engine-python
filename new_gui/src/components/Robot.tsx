// src/components/FootballPlayer.tsx
import React from 'react';

interface RobotProps {
    id: number;
    team: number; //  0 blue - 1 yellow
    position: {
      x: number;
      y: number;
    };
    field_data:{
        w:number;
        h:number;
    }
}

interface Position{
    x: number;
    y: number;
}
// Define the Robot component
const Robot: React.FC<RobotProps> = ({ id, team, position, field_data }) => {
    // Determine the color based on the team
    const color = team === 0 ? 'blue' : 'yellow';
    // Get the local coordinates
    let localPosition : Position = to_local_coordinates(position.x, position.y);
    // Define the styles for the circle
    const circleStyle: React.CSSProperties = {
        width: '20px',
        height: '20px',
        borderRadius: '50%',
        backgroundColor: color,
        position: 'relative',
        left: `${localPosition.x}px`,
        top: `${localPosition.y}px`,
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        color: 'white',
        fontSize: '12px',
    };

    // Convert robocup coords to css coords
    function to_local_coordinates(x : number,y : number) : Position{
        let new_x : number = x;
        let new_y : number = y;
        // Traslation
        new_x += field_data.w/2 ;
        new_y -= field_data.h/2;
        new_x = Math.min(field_data.w, Math.max(0, new_x));
        new_y = Math.min(0, Math.max(-field_data.h, new_y));
        return {x : new_x, y : new_y};
    }

    return <div style={circleStyle}>{id}</div>;
};

export default Robot;
