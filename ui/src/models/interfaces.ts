
/* utils */
export interface IObjectKeyIsStr {
    [key: string]: string
}

/* data interfaces */
export interface IUserInfoData {
    isLogin: boolean,
    id: string,
    username: string,
    email: string
};

export interface IUserInfoAction {
    type: 'Update/UpdateByLoginSucc',
    value: IUserInfoData
}

export interface IApiCallStatusAction{
    type: 'SUCC' | 'FAIL' | 'LOADING' | 'INIT'
}

/* hook interfaces */
export interface IUserInfoProps  {
    userInfoData: IUserInfoData
}

export interface IDialogProps {
    isOpen: boolean,
    setIsOpen: React.Dispatch<any>
}

export interface IDialogContent {
    msg: string
}

/* controller interfaces */
export interface ITextFieldController {
    id: string,
    label: string,
    value: string,
    setValue: any,
    type?: 'text' | 'password',
    required?: boolean,
    variant?: 'filled'
}
