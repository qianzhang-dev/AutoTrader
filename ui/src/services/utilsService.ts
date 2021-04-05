import { getJSON } from "./utils";

export class UtilsService {
    public getTradeOperators() {
        return getJSON('/tradeOperators');
    }
}

export const utilsService = new UtilsService();
