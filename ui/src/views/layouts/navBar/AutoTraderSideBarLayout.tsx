import React, { useEffect } from 'react';
import { Container, Grid } from '@material-ui/core';
import { UserInfoLayout } from './UserInfoLayout';
import { NavBarLayout } from './NavBarLayout';


export function AutoTraderSideBarLayout() {


    return (
        <Grid item container direction="column">
            <UserInfoLayout />
            <NavBarLayout />
        </Grid>
    ) 
}
