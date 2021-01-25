import { Container, Grid } from '@material-ui/core';
import React, { useEffect } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AutoTraderContentLayout } from './content/AutoTraderContentLayout';
import { AutoTraderSideBarLayout } from './navBar/AutoTraderSideBarLayout';

export function AutoTraderMainLayout() {


    return (
        <Container maxWidth="xl">
            <Router>
                <Grid container>
                    <Grid item xs={12} sm={2} container>
                        <AutoTraderSideBarLayout />
                    </Grid>
                    <Grid item xs={12} sm={10} container>
                        <AutoTraderContentLayout />
                    </Grid>
                </Grid>
            </Router>
        </Container>
    ) 
}
