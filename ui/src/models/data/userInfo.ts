import { createStore } from 'redux';
import { IUserInfoAction, IUserInfoData } from '../interfaces';

export function initialUserInfo(): IUserInfoData {
    return {
        isLogin: false,
        id: '',
        username: '',
        email: ''
    }
}

function userInfoReducer(userInfo: IUserInfoData = initialUserInfo(), action: IUserInfoAction) {
    switch (action.type) {
        case 'Update/UpdateByLoginSucc':
            return { ...action.value, isLogin: true};
                
        default:
            return userInfo;
    }
}

export let userInfoData = createStore(userInfoReducer);

