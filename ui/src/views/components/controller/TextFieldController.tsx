import React from 'react';
import { TextField } from '@material-ui/core';
import { ITextFieldController } from '../../../models/interfaces';

export function TextFieldController(props: ITextFieldController) {
    const id = props.id;
    const label = props.label;
    const value = props.value;

    const required = !!props.required;
    const type = props.type || 'text';
    const variant = props.variant || 'filled';

    const handleChange = (ev: any) => {
        props.setValue(ev.target.value);
    }

    return (
        <TextField
            required={required}
            id={id}
            label={label}
            value={value}
            type={type}
            variant={variant}
            onChange={handleChange}
        >
        </TextField>
    )
}
