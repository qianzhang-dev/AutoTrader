import React, { useEffect } from 'react';
import { Grid, List, ListItem, ListItemIcon, ListItemText } from '@material-ui/core';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";
import RemoveRedEyeIcon from '@material-ui/icons/RemoveRedEye';
import ErrorOutlineIcon from '@material-ui/icons/ErrorOutline';
import HomeIcon from '@material-ui/icons/Home';

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
                <ListItem component={Link} to={'/alerts'}>
                    <ListItemIcon>
                        <ErrorOutlineIcon />
                    </ListItemIcon>
                    <ListItemText primary="Alerts" />
                </ListItem>
                <ListItem component={Link} to={'/monitor'}>
                    <ListItemIcon>
                        <RemoveRedEyeIcon />
                    </ListItemIcon>
                    <ListItemText primary="Monitor" />
                </ListItem>
                </List>
        </Grid>
    )
}
