import React, { useEffect, useState } from 'react';
import { Button } from '@material-ui/core';
import { LoginDialog } from './LoginDialog';
import { SignupDialog } from './SignupDialog';

export function UserInfoNotLogin() {
    const [isLoginDialogOpen, setIsLoginDialogOpen] = useState(false);
    const [isSignupDialogOpen, setIsSignupDialogOpen] = useState(false);

    return (
        <div>
            <Button color="primary" onClick={() => setIsLoginDialogOpen(true)}>
                Log in
            </Button>

            <Button color="primary" onClick={() => setIsSignupDialogOpen(true)}>
                Sign up
            </Button>

            <LoginDialog isOpen={isLoginDialogOpen} setIsOpen={setIsLoginDialogOpen} />
            <SignupDialog isOpen={isSignupDialogOpen} setIsOpen={setIsSignupDialogOpen} />
        </div>
    )
}
