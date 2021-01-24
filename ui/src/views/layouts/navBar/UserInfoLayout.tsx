import { Grid } from '@material-ui/core';
import React, { useEffect } from 'react';
import { UserInfoContainer } from '../../components/userInfo/UserInfoContainer';

export function UserInfoLayout() {
    return (
        <Grid item xs={12}>
            <UserInfoContainer />
        </Grid>
    )
}
