<template>
  <div class="home">
    <TheHeader />
    <b-container fluid>
      <Properties />
    </b-container>
    <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue";
import TheFooter from "@/components/TheFooter.vue";
import Properties from "@/componen,,,,,,,,,,ts/Properties.vue";
import BootstrapVue from "bootstrap-vue";

export default Vue.extend({
  name: "Home",
  components: {
    TheHeader,
    Properties,
    TheFooter,
  }
});
</script>
