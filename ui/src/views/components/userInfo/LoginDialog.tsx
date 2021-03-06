import React, { useEffect, useMemo, useReducer, useState } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, TextField } from '@material-ui/core';
import { func } from 'prop-types';
import { IDialogProps, IUserInfoData } from '../../../models/interfaces';
import { apiCallStatusReducer, initApiCallStatus } from '../../../models/data/apiCallStatus';
import { DialogFailContent, DialogLoadingContent, DialogSuccContent } from '../utils';
import { TextFieldController } from '../controller/TextFieldController';
import { userInfoService } from '../../../services/userInfoService';
import { userInfoData } from '../../../models/data/userInfo';
import { createBasicAuthToken } from '../../../services/utils';


export function LoginDialog(props: IDialogProps) {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [status, updateStatus] = useReducer(apiCallStatusReducer, initApiCallStatus());

    function cleanDialog() {
        setUsername('');
        setPassword('');
        updateStatus({ type: 'INIT' });
    }

    const handleClose = () => {
        props.setIsOpen(false);
        cleanDialog();
    }

    const handleLogin = () => {
        updateStatus({ type: 'LOADING' });
        userInfoService.loginUser(username, password)
        .then(s => {
            userInfoData.dispatch({ type: 'Update/UpdateByLoginSucc', value: {
                ...s.data as unknown as IUserInfoData,
                authToken: createBasicAuthToken(username, password)
            }})
            updateStatus({ type: 'SUCC'});
        })
        .catch(err => {
            console.log(err);
            updateStatus({ type: 'FAIL' });
        })
    }
    
    const renderUsername = useMemo(() => {
        return (
            <TextFieldController
                id='signup-username'
                label='Username'
                value={username}
                setValue={setUsername}
                required={true}
            />
        )
    }, [username]);

    const renderPassword = useMemo(() => {
        return (
            <TextFieldController
                id="signup-pwd"
                value={password}
                setValue={setPassword}
                required={true}
                type='password'
                label="Password"
            />
        )
    }, [password]);

    const renderLoginForm = useMemo(() => {
        return (
            <Grid xs={12} container direction="column" spacing={4}>
                <Grid item>
                    {renderUsername}
                </Grid>
                <Grid item>
                    {renderPassword}
                </Grid>
            </Grid>
        )
    }, [username, password]);

    const renderDialogContent = useMemo(() => {
        switch (status) {
            case 'INIT':
                return renderLoginForm;
            case 'FAIL':
                return <DialogFailContent msg="Login failed." />;
            
            case 'LOADING':
                return <DialogLoadingContent />;
            
            case 'SUCC':
                return <DialogSuccContent msg="Successfully logined in!" />;
        }
    }, [status, username, password])


    return (
        <Dialog 
            open={props.isOpen} 
            onClose={handleClose}
            aria-labelledby="form-login"
        >
            <DialogTitle id="form-login"> Log in </DialogTitle>
            <DialogContent>
                { renderDialogContent }
            </DialogContent>
            <DialogActions>
                {
                    status === "LOADING" &&
                    <Button onClick={handleClose} color="default">
                        Cancel
                    </Button>
                }
                
                {
                    status === "INIT" &&
                    <Button onClick={handleLogin} color="primary">
                        Login
                    </Button>
                }
            </DialogActions>
        </Dialog>
    )
}
