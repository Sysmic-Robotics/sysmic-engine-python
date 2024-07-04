import React from 'react';
import logo from './logo.svg';
import './App.css';

import Box from '@mui/material/Box';

import Gameplay from './components/Gameplay'
import Sidebar from './components/Sidebar'
import { Grid } from '@mui/material';

function App() {
  return (
    
    <Box >
    <Grid container spacing={1}>
      <Grid  item xs={4} sx={{ border: 1, height: '400px' }}>
        <Sidebar/>
      </Grid>
      <Grid item xs={8} sx={{ border: 1 }}>
        <Gameplay width={800} height={400}/>
      </Grid>
      <Grid item xs={12} sx={{ border: 1 }}>
      
      </Grid>
    </Grid>
        
        
    </Box>
  );
}

export default App;
