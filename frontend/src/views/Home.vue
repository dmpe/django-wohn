<template>
  <div class="home">
    <Header></Header>
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App" />
  </div>
</template>

<script lang="ts">
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
import Header from "@/components/Header.vue"; // @ is an alias to /src
import Vue from "vue";

export default Vue.extend({
  name: "Home",
  components: {
    Header,
    HelloWorld
  }
});
</script>
