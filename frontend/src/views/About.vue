<template>
  <div class="about">
    <TheHeader />
    <b-container fluid>
      <b-row>
        <b-col
          md="6"
          offset-md="3"
        >
          <div id="renderMarkdownContent" />
        </b-col>
      </b-row>
    </b-container>
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
  converter.setOption("ghCompatibleHeaderId", true);
  converter.setOption("tables", true);
  converter.setOption("ghCodeBlocks", true);
  converter.setOption("tasklists", true);
  converter.setOption("smartIndentationFix", true);
  converter.setOption("openLinksInNewWindow", true);
  converter.setOption("emoji", true);
  showdown.setFlavor("github");

  const html = converter.makeHtml(response.data);

  const divRender: HTMLDivElement = document.getElementById("renderMarkdownContent") as HTMLDivElement;
  divRender.insertAdjacentHTML("afterbegin", html);
});


export default Vue.extend({
  name: "About",
  components: {
    TheHeader,
    TheFooter,
  }
});

</script>
