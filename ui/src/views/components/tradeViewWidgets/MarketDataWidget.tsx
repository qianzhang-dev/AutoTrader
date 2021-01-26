import { Grid } from '@material-ui/core';
import React, { useEffect } from 'react';
import { tradeViewService } from '../../../services/tradeViewService';

export function MarketDataWidget() {


    useEffect(() => {
        // Wait for the onload here
        // widget_api.script.onload = () => setState({isLoading: false})
        const widgetApi = tradeViewService.createWidgetEl('MARKET_DATA');
        const widgetApiContainer = document.getElementById("home-market-data-widget");
        if (widgetApiContainer?.children.length === 0)
            document.getElementById("home-market-data-widget")?.appendChild(widgetApi);
    }, []);

    return (
        <Grid item xs={12} container>
            <Grid item xs={2}></Grid>
            <Grid item xs={8}><div id="home-market-data-widget"></div></Grid>
            <Grid item xs={2}></Grid>
        </Grid>
    )
}
