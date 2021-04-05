import { Grid } from '@material-ui/core';
import React from 'react';
import { journalService } from '../../../services/journalService';
import { utilsService } from '../../../services/utilsService';
import { JournalContainer } from '../../components/journal/JournalContainer';

export function JournalLayout() {
    console.log(utilsService.getTradeOperators());

    return (
        <Grid item xs={12} container>
            <JournalContainer />
        </Grid>
    )
}
