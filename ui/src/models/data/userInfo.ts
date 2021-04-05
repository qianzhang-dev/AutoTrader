import { createStore } from 'redux';
import { IUserInfoAction, IUserInfoData } from '../interfaces';

export function initialUserInfo(): IUserInfoData {
    return {
        isLogin: false,
        id: '',
        username: '',
        email: '',
        authToken: ''
    }
}

function userInfoReducer(userInfo: IUserInfoData = initialUserInfo(), action: IUserInfoAction) {
    switch (action.type) {
        case 'Update/UpdateByLoginSucc':
            return { 
                isLogin: true,
                id: action.value.id,
                username: action.value.username,
                email: action.value.email,
                authToken: action.value.authToken
            };

        default:
            return userInfo;
    }
}

export let userInfoData = createStore(userInfoReducer);

