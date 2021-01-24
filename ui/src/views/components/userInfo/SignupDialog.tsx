import React, { useEffect } from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogTitle, Grid, TextField } from '@material-ui/core';
import { IDialogProps } from '../../../models/interfaces';


export function SignupDialog(props: IDialogProps ) {

    const handleClose = () => {
        props.setIsOpen(false);
    }

    return (
        <Dialog 
            open={props.isOpen} 
            onClose={handleClose}
            aria-labelledby="form-signup"
        >
            <DialogTitle id="form-signup"> Sign up </DialogTitle>
            <DialogContent>
                <Grid xs={12} container direction="column" spacing={4}>
                    <Grid item>
                        <TextField
                            required
                            id="signup-username"
                            label="Username"
                            variant="filled"
                        >
                        </TextField>
                    </Grid>
                    <Grid item>
                        <TextField
                            required
                            id="signup-pwd"
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
                    Sign up
                </Button>
            </DialogActions>
        </Dialog>
    )
}
