<template>
  <b-row>
    <div class="card">
      <div class="row no-gutters">
        <div class="col-md-7 mt-3 mb-md-0">
          <a href="#">
            <img
              class="card-img img-fluid rounded"
              src="https://picsum.photos/600/200">
          </a>
        </div>
        <div class="col-md-5 mt-3 mb-md-0">
          <div class="card-body">
            <h4 class="card-title">
              Project One
            </h4>
            <p class="card-text">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium veniam exercitationem expedita laborum at voluptate. Labore, voluptates totam at aut nemo deserunt rem magni pariatur quos perspiciatis atque eveniet unde.
            </p>
            <a
              class="btn btn-primary"
              href="#"
            >View Project</a>
          </div>
        </div>
      </div>
    </div>
  </b-row>
</template>

<script lang="ts">
import Vue from "vue";
import gql from "graphql-tag";
import { returnLastFive } from "@/graphql/realestate/returnLastFive.ts";

export default Vue.extend({
  name: "Properties",
  apollo: {
    returnLastFive: {
      query: returnLastFive
    }
  },
  data() {
    return {
      returnLastFive: []
    };
  }
});
</script>
