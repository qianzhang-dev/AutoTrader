import { createStore } from 'redux';
import { IUserInfoAction, IUserInfoData } from '../interfaces';

export function initialUserInfo(): IUserInfoData {
    return {
        isLogin: false,
        id: '',
        name: '',
        avatarSrc: ''
    }
}

function userInfoReducer(userInfo: IUserInfoData = initialUserInfo(), action: IUserInfoAction) {
    switch (action.type) {
        case 'Update/UpdateByLoginSucc':
            return action.value;

        default:
            return action.value;
    }
}

export let userInfoData = createStore(userInfoReducer);

