import { IApiCallStatusAction } from "../interfaces";

export function initApiCallStatus(): string {
    return 'INIT';
}

export function apiCallStatusReducer(status: string = initApiCallStatus(), action: IApiCallStatusAction) {
    switch (action.type) {
        case 'INIT':
            return 'INIT';
        
        case 'SUCC':
            return 'SUCC';

        case 'FAIL':
            return 'FAIL';

        case 'LOADING':
            return 'LOADING';

        default:
            return status;
    }
}

