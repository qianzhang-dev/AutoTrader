import React from 'react';
import { Grid} from '@material-ui/core';
import { Switch, Route } from "react-router-dom";
import { AlertLayout } from './AlertLayout';
import { HomeLayout } from './HomeLayout';
import { MonitorLayout } from './MonitorLayout';
import { JournalLayout } from './JournalLayout';

export function AutoTraderContentLayout() {

    const routes = [
        {
            path: '/',
            exact: true,
            main: () => <div> "yes" </div>
        },
        {
            path: '/alert',
            exact: true,
            main: () => <AlertLayout />
        },
        {
            path: '/monitor',
            exact: true,
            main: () => <MonitorLayout />
        },
        {
            path: '/journal',
            exact: true,
            main: () => <JournalLayout />
        }
    ];

    return (
        <Grid item xs={12} container>
            <Switch>
                <Route key={0} path='/home' children={<HomeLayout/>} />
                <Route key={1} path='/alert' children={<AlertLayout />} />
            </Switch>
        </Grid>
    ) 
}
