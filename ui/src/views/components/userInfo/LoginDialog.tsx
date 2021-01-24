import React, { useEffect, useState } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, TextField } from '@material-ui/core';
import { func } from 'prop-types';
import { IDialogProps } from '../../../models/interfaces';


export function LoginDialog(props: IDialogProps) {

    const handleClose = () => {
        props.setIsOpen(false);
    }

    return (
        <Dialog 
            open={props.isOpen} 
            onClose={handleClose}
            aria-labelledby="form-login"
        >
            <DialogTitle id="form-login"> Log in </DialogTitle>
            <DialogContent>
                <Grid xs={12} container direction="column" spacing={4}>
                    <Grid item>
                        <TextField
                            required
                            id="login-username"
                            label="Username"
                            variant="filled"
                        >
                        </TextField>
                    </Grid>
                    <Grid item>
                        <TextField
                            required
                            id="login-pwd"
                            type="password"
                            label="Password"
                            variant="filled"
                        >
                        </TextField>
                    </Grid>
                </Grid>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="default">
                    Cancel
                </Button>
                <Button onClick={handleClose} color="primary">
                    Login
                </Button>
            </DialogActions>
        </Dialog>
    )
}
