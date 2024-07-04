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
          position: { x: 100, y: -200 },
        }
      ];
    return (
      <>
          <Field width={width} height={height}/>
          {robots.map((robot) => (
              <Robot key={robot.id} {...robot}/>
          ))}
          
          
      </>
    );
  }
  
  export default Gameplay;