import { Grid } from '@material-ui/core';
import React, { useEffect, useMemo, useReducer, useState } from 'react';
import { MarketDataWidget } from '../tradeViewWidgets/MarketDataWidget';

export function HomeContainer() {


    return (
        <Grid item xs={12} container>
            <Grid item xs={12} container>
                <MarketDataWidget />
            </Grid> 
        </Grid>
    )
}
