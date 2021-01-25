import React, { useEffect, useState } from 'react';
import { Grid } from '@material-ui/core';
import { userInfoData } from '../../../models/data/userInfo';
import { UserInfo } from './UserInfo';
import { UserInfoNotLogin } from './UserInfoNotLogin';

export function UserInfoContainer() {
    const [isLogin, setIsLogin] = useState(false);

    useEffect(() => {
        const userInfoDataUnsubscribe = userInfoData.subscribe(() => {console.log("Match"); setIsLogin(true)});
        return function cleanUp() {
            userInfoDataUnsubscribe();
        }
    }, []);

    return (
        <Grid item container>
            {
                isLogin &&
                <UserInfo userInfoData={userInfoData.getState()}/>
            }
            {
                !isLogin &&
                <UserInfoNotLogin />
            }
        </Grid>
    )
}
