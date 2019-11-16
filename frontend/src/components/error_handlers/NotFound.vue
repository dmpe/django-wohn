<template>
  <b-container>
    <b-row>
      <b-col
        md="8"
        class="red"
      >
        <b-img
          fluid-grow
          src="https://picsum.photos/500/600"
        />
      </b-col>
    </b-row>
  </b-container>
</template>

<script lang="ts">
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";

export default {
  name: "NotFound",
  data() {
    return {

    };
  },
};
</script>

<style lang="stylus">

.red
  border-style: dashed

</style>

