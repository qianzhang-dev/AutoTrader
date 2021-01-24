/* data interfaces */
export interface IUserInfoData {
    isLogin: boolean,
    id: string,
    name: string,
    avatarSrc: string,
};

export interface IUserInfoAction {
    type: 'Update/UpdateByLoginSucc',
    value: IUserInfoData
}

/* hook interfaces */
export interface IUserInfoProps  {
    userInfoData: IUserInfoData
}

export interface IDialogProps {
    isOpen: boolean,
    setIsOpen: React.Dispatch<any>
}
