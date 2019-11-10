<template>
  <div class="about">
    <TheHeader />
    <h1>This is an about page</h1>
    <TheFooter />
  </div>
</template>


<script lang="ts">
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue"; // @ is an alias to /src
import Vue from "vue";

export default Vue.extend({
  name: "About",
  components: {
    TheHeader,
    TheFooter,
  }
});
</script>
