const axios = require("axios").default

export function createHTMLfromMarkdown(URLlink: string) {
  var aboutMarkdown = axios.get(URLlink);
  console.log(aboutMarkdown);
  return aboutMarkdown;
}


