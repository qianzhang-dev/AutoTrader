import { API_BASE_URL, HEADERS } from "../utils";
import axios from 'axios';

export class UserInfoService {

    private getJSON(url: string) {
        return axios.get(API_BASE_URL + url, HEADERS);
    }

    private postJSON(url: string, params: any) {
        return axios.post(API_BASE_URL + url, params, HEADERS);
    }

    public createNewUser(username: string, password: string, email: string) {
        return this.postJSON('/user', {
            username: username,
            password: password,
            email: email
        });
    }
}

export const userInfoService = new UserInfoService();
