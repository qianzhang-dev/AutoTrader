import axios from "axios";
import { API_BASE_URL, HEADERS } from "../utils";
import { userInfoData } from "../models/data/userInfo";

export function getJSON(url: string) {
    return axios.get(API_BASE_URL + url, {
        headers: {
            ...HEADERS,
            'Authorization': userInfoData.getState().authToken
        }
    });
}

export function postJSON(url: string, params: any) {
    return axios.post(API_BASE_URL + url, params, {
        headers: {
            ...HEADERS,
            'Authorization': userInfoData.getState().authToken
        }
    });
}

/* generate authToken */
export function createBasicAuthToken(username: string, password: string) {
    return 'Basic ' + btoa(username + ':' + password);
}
