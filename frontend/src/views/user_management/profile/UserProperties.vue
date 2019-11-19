<template>
  <div>
    <TheHeader />

    <b-container fluid>
      <div class="row">
        <ProfileNav />

        <div class="col-md-10">
          <form
            id="form-new-user-property"
            method="POST"
            class="mb-5"
          />
        </div>
      </div>
    </b-container>
    <TheFooter />
  </div>
</template>


<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import ProfileNav from "@/components/TheNavSidebar.vue";

export default Vue.extend({
  name: "UserProperties",
  components: {
    TheHeader,
    ProfileNav,
    TheFooter,
  }
});
</script>
