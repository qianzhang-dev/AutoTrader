import React, { useEffect } from 'react';
import { Container, Grid } from '@material-ui/core';
import { UserInfoLayout } from './UserInfoLayout';
import { NavBarLayout } from './NavBarLayout';


export function AutoTraderSideBarLayout() {


    return (
        <Grid item xs={12} container direction="column">
            <Grid item><UserInfoLayout /></Grid>
            <Grid item><NavBarLayout /></Grid>
        </Grid>
    ) 
}
