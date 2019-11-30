<template>
  <div>
  <TheHeader />
  <ProfileNav />
  <TheFooter />
  </div>
</template>


<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import ProfileNav from "@/components/TheNavSidebar.vue";

export default Vue.extend({
  name: "UserProfile",
  components: {
    TheHeader,
    ProfileNav,
    TheFooter,
  }
});

</script>


