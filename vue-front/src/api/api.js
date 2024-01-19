import { fetch } from "./fetch";

/**
 * 登录
 * @returns {Promise<Response>}
 */
export function _login(data) {
  return fetch({
    url: "api/paddleApp/login",
    method: "POST",
    data: data,
  });
}

/**
 * 登录
 * @returns {Promise<Response>}
 */
export function _register(data) {
  return fetch({
    url: "api/paddleApp/register",
    method: "POST",
    data: data,
  });
}

/**
 * 获取list
 * @returns {Promise<Response>}
 */
export function _queryOcrs(params) {
  return fetch({
    url: "api/paddleApp/orc-records",
    method: "GET",
    params: params,
  });
}

/**
 * 获取list
 * @returns {Promise<Response>}
 */
export function _deleteOcrRecord(data) {
  return fetch({
    url: "api/paddleApp/delete/record",
    method: "POST",
    data: data,
  });
}
