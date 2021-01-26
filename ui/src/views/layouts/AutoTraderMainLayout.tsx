import { Container, Grid } from '@material-ui/core';
import React, { useEffect } from 'react';
import { BrowserRouter as Router, Switch } from 'react-router-dom';
import { AutoTraderContentLayout } from './content/AutoTraderContentLayout';
import { AutoTraderSideBarLayout } from './navBar/AutoTraderSideBarLayout';

export function AutoTraderMainLayout() {

    return (
        <Container maxWidth="xl">
            <Router>
                <Grid container style={{border: '2pt'}}>
                    <Grid item xs={1} sm={1} xl={1} container>
                        <AutoTraderSideBarLayout />
                    </Grid>
                    <Grid item xs={11} sm={11} xl={11} container>
                        <AutoTraderContentLayout />
                    </Grid>
                </Grid>
            </Router>
        </Container>
    ) 
}
