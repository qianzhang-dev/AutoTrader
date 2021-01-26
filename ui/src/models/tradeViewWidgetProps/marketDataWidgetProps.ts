
export function initMarketDataWidgetProps() {
    return {
    "width": '100%',
    "height": 500,
    "symbolsGroups": [
      {
        "name": "Indices",
        "originalName": "Indices",
        "symbols": [
          {
            "name": "FOREXCOM:SPXUSD",
            "displayName": "S&P 500"
          },
          {
            "name": "FOREXCOM:NSXUSD",
            "displayName": "Nasdaq 100"
          },
          {
            "name": "FOREXCOM:DJI",
            "displayName": "Dow 30"
          }
        ]
      },
      {
        "name": "Stock",
        "symbols": [
          {
            "name": "NASDAQ:MSFT",
            "displayName": "Microsoft"
          }
        ]
      }
    ],
    "showSymbolLogo": true,
    "colorTheme": "light",
    "isTransparent": false,
    "locale": "en"
  };
}
