<template>
  <div class="about">
    <TheHeader />
    <div id="renderMarkdownContent"></div>
    <TheFooter />
  </div>
</template>


<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import * as showdown from "showdown";
import { createHTMLfromMarkdown } from "@/support.ts";

createHTMLfromMarkdown("https://raw.githubusercontent.com/dmpe/django-wohn/master/README.md").then(response => {
  const converter = new showdown.Converter();
  const html = converter.makeHtml(response.data);
  console.log(html);

  const divRender: HTMLDivElement = document.getElementById("renderMarkdownContent") as HTMLDivElement;
  divRender.append(html);
});


export default Vue.extend({
  name: "About",
  components: {
    TheHeader,
    TheFooter,
  }
});

</script>
