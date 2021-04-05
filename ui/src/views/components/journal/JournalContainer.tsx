import React, { useEffect, useMemo, useReducer, useState } from 'react';
import { Grid } from '@material-ui/core';
import { AutoCompleteCombobox } from '../utils/AutoCompleteCombobox';

export function JournalContainer() {


    return (
        <Grid item xs={12} container>
            <Grid item xs={12} container>
                <Grid item xs={12}>
                    <AutoCompleteCombobox data={} dispatch={} />
                </Grid>
                
            </Grid> 
        </Grid>
    )
}
