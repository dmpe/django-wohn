const axios = require("axios").default;

export function createHTMLfromMarkdown(URLlink: string) {
  return axios.get(URLlink);
}
