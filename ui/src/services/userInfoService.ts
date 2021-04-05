import { API_BASE_URL, HEADERS } from "../utils";
import axios from 'axios';
import { createBasicAuthToken, postJSON } from "./utils";

export class UserInfoService {

    public loginUser(username: string, password: string) {
        return axios.post(API_BASE_URL + '/login', undefined, {
            headers: {
                ...HEADERS,
                'Authorization': createBasicAuthToken(username, password)
            }
        });
    }

    public createNewUser(username: string, password: string, email: string) {
        return postJSON('/user', {
            username: username,
            password: password,
            email: email
        });
    }
}

export const userInfoService = new UserInfoService();
