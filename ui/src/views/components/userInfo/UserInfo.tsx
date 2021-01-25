import React, { useEffect, useState } from 'react';
import { IUserInfoProps } from '../../../models/interfaces';

export function UserInfo(props: IUserInfoProps) {
    console.log(props.userInfoData);
    return (
        <div>
            {props.userInfoData.username}
        </div>
    )
}
