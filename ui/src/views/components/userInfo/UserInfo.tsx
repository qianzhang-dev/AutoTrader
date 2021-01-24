import React, { useEffect, useState } from 'react';
import { IUserInfoProps } from '../../../models/interfaces';

export function UserInfo(props: IUserInfoProps) {

    return (
        <div>
            {props.userInfoData.name}
        </div>
    )
}
