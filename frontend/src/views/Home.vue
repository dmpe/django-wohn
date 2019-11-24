<template>
  <div class="home">
    <TheHeader />
    <!-- <img
      alt="Vue logo"
      src="../assets/logo.png"
    > -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App" /> -->
    <Properties />
    <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
import TheHeader from "@/components/TheHeader.vue";
import TheFooter from "@/components/TheFooter.vue";
import Properties from "@/components/Properties.vue";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap/dist/css/bootstrap.css";

export default Vue.extend({
  name: "Home",
  components: {
    TheHeader,
    Properties,
    TheFooter,
  }
});
</script>
