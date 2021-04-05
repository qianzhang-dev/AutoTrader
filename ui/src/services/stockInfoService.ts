import { ITicker } from "../models/interfaces";
import { getJSON } from "./utils";

export class StockInfoService {
    private isInitated: boolean = false;
    private tickers: ITicker[] = [];

    public async init() {
        await this.getAllTickers()
        .then(res => {
            this.tickers = res as unknown as ITicker[];
            this.isInitated = true;
        })
        .catch(err => {
            console.log("Error: Failed to retrieve tickers info.")
        })
    }
    
    public isInitialized() {
        return this.isInitated;
    }

    public getTickers() {
        return this.tickers;
    }

    public getAllTickers() {
        return getJSON('/tickers');
    }
}

export const stockInfoService = new StockInfoService();
stockInfoService.init();
