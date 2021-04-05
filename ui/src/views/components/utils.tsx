import React from "react";
import { CircularProgress, Grid } from "@material-ui/core";
import { IDialogContent } from "../../models/interfaces";

export function DialogSuccContent(props: IDialogContent) {
    return (
        <Grid item xs={12} container justify="center">
            {props.msg}
        </Grid>
    )
}

export function DialogFailContent(props: IDialogContent) {
    return (
        <Grid item xs={12} container justify="center">
            {props.msg}
        </Grid>
    )
}

export function DialogLoadingContent() {
    return (
        <Grid item xs={12} container justify="center">
            <CircularProgress />
        </Grid>
    )
}


