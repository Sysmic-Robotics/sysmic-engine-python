import React from 'react'
import Field from './Field'
import Robot from './Robot'


interface GameplayProps {
  width: number;
  height: number;
}



const Gameplay: React.FC<GameplayProps> = ({ width, height })  =>{
    const robots = [
        {
          id: 1,
          team: 0,
          position: { x: 0, y: 0 },
        },
        {
          id: 1,
          team: 0,
          position: { x: 100, y: 50 },
        },
        {
          id: 2,
          team: 1,
          position: { x: 20, y: 40 },
        }
      ];
    return (
      <>
          <Field width={width} height={height}/>
          {robots.map((robot) => (
              <Robot key={robot.id} id={robot.id} team={robot.team} position={robot.position} field_data={{w:width, h:height}}/>
          ))}
          
          
      </>
    );
  }
  
  export default Gameplay;