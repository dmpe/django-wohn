<template>
  <div>
    <TheHeader />
    <b-container fluid>
      <NotFoundError />
    </b-container>
    <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import NotFoundError from "@/components/error_handlers/NotFoundError.vue";

export default Vue.extend({
  name: "NotFound",
  components: {
    TheHeader,
    NotFoundError,
    TheFooter,
  }
});
</script>
