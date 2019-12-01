<template>
  <div>
    <div class="row">
      <div class="col-md-7">
        <a href="#">
          <img
            class="img-fluid rounded mt-3 mb-md-0"
            src="https://picsum.photos/300/100"
            alt=""
          >
        </a>
      </div>
      <div class="col-md-5">
        <h3>Project One</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium veniam exercitationem expedita laborum at voluptate. Labore, voluptates totam at aut nemo deserunt rem magni pariatur quos perspiciatis atque eveniet unde.</p>
        <!-- <p>{{ price_in_euro }}</p>
          <p>{{ price_in_czk }}</p>
          <p>{{ price_in_usd }}</p> -->
        <a
          class="btn btn-primary"
          href="#"
        >View Project</a>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default {
  name: "Properties",
  data() {
    return {

    };
  }
};
</script>
