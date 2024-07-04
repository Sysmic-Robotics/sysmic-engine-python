import React from 'react';
import Stack from '@mui/material/Stack';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    ...theme.typography.body2,
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  }));

const Sidebar: React.FC = () => {
    return (
        <Stack style={{maxHeight: '100%', overflow: 'auto'}} spacing={2}>
            <Item>Item 1</Item>
            <Item>Item 2</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
            <Item>Item 3</Item>
        </Stack>
    );
};

export default Sidebar;
