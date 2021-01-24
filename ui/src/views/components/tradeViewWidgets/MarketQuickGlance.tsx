import { render } from '@testing-library/react';
import React, { useEffect } from 'react';

export function MarketQuickGlance() {
    useEffect(() => {
        const widget_api = document.createElement("script");
        widget_api.src = "https://stat.ripe.net/widgets/widget_api.js";
        widget_api.async = true;
        // Wait for the onload here
        // widget_api.script.onload = () => setState({isLoading: false})
        document.body.appendChild(widget_api);
    }, []);

    return (
        <div></div>
    )  
}
