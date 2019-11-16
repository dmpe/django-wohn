<template>
  <div class="about">
    <TheHeader />
    <NotFound />
    <TheFooter />
  </div>
</template>


<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import NotFound from "@/components/error_handlers/NotFound.vue";


export default Vue.extend({
  name: "404NotFound",
  components: {
    TheHeader,
    NotFound,
    TheFooter,
  }
});
</script>
