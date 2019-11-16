const axios = require("axios").default;

export function createHTMLfromMarkdown(URLlink: string) {
  const aboutMarkdown = axios.get(URLlink);
  console.log(aboutMarkdown);
  return aboutMarkdown;
}


