<template>
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
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "NotFoundError",
  data() {
    return {

    }
  },
});
</script>

<style lang="stylus" scoped>

.red
  border-style: dashed

</style>

