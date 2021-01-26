import React, { useMemo, useReducer, useState } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, TextField } from '@material-ui/core';
import { IDialogProps, IUserInfoData } from '../../../models/interfaces';
import { userInfoData } from '../../../models/data/userInfo';
import { TextFieldController } from '../controller/TextFieldController';
import { userInfoService } from '../../../services/userInfoService';
import { userInfo } from 'os';
import { apiCallStatusReducer, initApiCallStatus } from '../../../models/data/apiCallStatus';
import { DialogFailContent, DialogLoadingContent, DialogSuccContent } from '../utils';


export function SignupDialog(props: IDialogProps ) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [status, updateStatus] = useReducer(apiCallStatusReducer, initApiCallStatus());

    function cleanDialog() {
        setUsername('');
        setPassword('');
        setEmail('');
        updateStatus({ type: 'INIT' });
    }

    const handleClose = () => {
        props.setIsOpen(false);
        cleanDialog();
    }

    const handleSignup = () => {
        updateStatus({ type: 'LOADING' });

        userInfoService.createNewUser(username, password, email)
        .then(s => {
            userInfoData.dispatch({type: 'Update/UpdateByLoginSucc', value: s.data as unknown as IUserInfoData})
            updateStatus({ type: 'SUCC' });
            console.log(s);
        })
        .catch(err => {
            updateStatus({ type: 'FAIL' });
            console.log(err);
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

    const renderEmail  = useMemo(() => {
        return (
            <TextFieldController
                id="signup-email"
                value={email}
                setValue={setEmail}
                label="Email"
            />
        )
    }, [email]);

    const renderSignupForm = useMemo(() => {
        return (
            <Grid xs={12} container direction="column" spacing={4}>
                <Grid item>
                    {renderUsername}
                </Grid>
                <Grid item>
                    {renderPassword}
                </Grid>
                <Grid item>
                    {renderEmail}
                </Grid>
            </Grid>
        )
    }, [username, password, email]);

    const renderDialogContent = useMemo(() => {
        switch (status) {
            case 'INIT':
                return renderSignupForm;
            case 'FAIL':
                return <DialogFailContent msg="Sign up failed." />;
            
            case 'LOADING':
                return <DialogLoadingContent />;
            
            case 'SUCC':
                return <DialogSuccContent msg="Successfully signed up!" />;
        }
    }, [status, username, password, email])

    return (
        <Dialog 
            open={props.isOpen} 
            onClose={handleClose}
            aria-labelledby="form-signup"
        >
            <DialogTitle id="form-signup"> Sign up </DialogTitle>
            <DialogContent>
                {renderDialogContent}
            </DialogContent>
            <DialogActions>
                {
                    status !== 'LOADING' &&
                    <Button onClick={handleClose} color="default">
                        Close
                    </Button>
                }

                {
                    status === 'INIT' &&
                    <Button onClick={handleSignup} color="primary">
                        Sign up
                    </Button>
                }
            </DialogActions>
        </Dialog>
    )
}
