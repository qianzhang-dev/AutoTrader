import React, { useEffect, useState } from 'react';
import { Grid } from '@material-ui/core';
import { initialUserInfo, userInfoData } from '../../../models/data/userInfo';
import { UserInfo } from './UserInfo';
import { UserInfoNotLogin } from './UserInfoNotLogin';

export function UserInfoContainer() {
    const [isLogin, setIsLogin] = useState(false);
    console.log(isLogin);
    useEffect(() => {
        // if (isLogin !== userInfoData.getState().isLogin) {
        //     setIsLogin(userInfoData.getState().isLogin);
        // }
    }, [userInfoData]);

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
