import React from 'react';
import { Grid } from '@material-ui/core';
import { HomeContainer } from '../../components/home/HomeContainer';

export function HomeLayout() {

    return (
        <Grid item xs={12} container>
            <HomeContainer />
        </Grid>
    )
}
