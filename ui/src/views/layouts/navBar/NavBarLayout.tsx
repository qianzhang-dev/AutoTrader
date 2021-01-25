import React from 'react';
import { Grid, List, ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import { Link } from "react-router-dom";
import RemoveRedEyeIcon from '@material-ui/icons/RemoveRedEye';
import ErrorOutlineIcon from '@material-ui/icons/ErrorOutline';
import HomeIcon from '@material-ui/icons/Home';
import MenuBookIcon from '@material-ui/icons/MenuBook';

export function NavBarLayout() {

    return (
        <Grid item xs={12} container>
            <List component="nav" aria-label="navigation bar">
                <ListItem component={Link} to={'/home'}>
                    <ListItemIcon>
                        <HomeIcon />
                    </ListItemIcon>
                    <ListItemText primary="Home" />
                </ListItem>
                <ListItem component={Link} to={'/alert'}>
                    <ListItemIcon>
                        <ErrorOutlineIcon />
                    </ListItemIcon>
                    <ListItemText primary="Alert" />
                </ListItem>
                <ListItem component={Link} to={'/monitor'}>
                    <ListItemIcon>
                        <RemoveRedEyeIcon />
                    </ListItemIcon>
                    <ListItemText primary="Monitor" />
                </ListItem>
                <ListItem component={Link} to={'/journal'}>
                    <ListItemIcon>
                        <MenuBookIcon />
                    </ListItemIcon>
                    <ListItemText primary="Journal" />
                </ListItem>
                </List>
        </Grid>
    )
}
