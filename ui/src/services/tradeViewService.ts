import { IObjectKeyIsStr } from "../models/interfaces";
import { initMarketDataWidgetProps } from "../models/tradeViewWidgetProps/marketDataWidgetProps";

class TradeViewService {

    private _widgetSrcs: IObjectKeyIsStr = {
        'MARKET_DATA': 'https://s3.tradingview.com/external-embedding/embed-widget-market-quotes.js'
    }

    private _watchlist = [
        {
            id: "0",
            ticker: "NASDAQ:MSFT",
            displayName: "Microsoft"
        },
        {
            id: "1",
            ticker: "NASDAQ:AAPL",
            displayName: "Apple"
        }
    ];

    private generateMarketDataWidgetProps() {
        let props = initMarketDataWidgetProps();
        props.symbolsGroups[1].symbols = this._watchlist.map((stock, index) => {
            return {
                name: stock.ticker,
                displayName: stock.displayName
            }
        });
        return props;
    }

    private generateProps(type: string) {
        switch (type) {
            case 'MARKET_DATA':
                return this.generateMarketDataWidgetProps();

            default:
                return {}
        }
    }

    public createWidgetEl(type: string) {
        const widgetApi = document.createElement("script");
        widgetApi.src = this._widgetSrcs[type];
        widgetApi.type = "text/javascript";
        widgetApi.async = true;
        widgetApi.text = JSON.stringify(this.generateProps(type));

        return widgetApi;
    }
}

const tradeViewService = new TradeViewService();

export { tradeViewService };
