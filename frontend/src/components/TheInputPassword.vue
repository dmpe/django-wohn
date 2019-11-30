<template>
  <div class="input-group">
    <!-- when header already contains `buttonEYE` then here one needs a different id attr. -->
    <input
      id="inputNewPassword"
      v-bind:type="[iconCollapsed ? 'password' : 'text']"
      name="inputNewPassword"
      class="form-control"
      placeholder="Password"
    >
    <div class="input-group-append">
      <span
        id="inputGroupAppend"
        class="input-group-text"
      >
        <button
          id="buttonEYE2"
          class="resetIconStylesEYE"
          aria-hidden="true"
          type="button"
          v-on:click="iconCollapsed = !iconCollapsed; icon = !icon"
        >
          <span v-show="icon">
            <i class="fas fa-lg fa-eye"/>
          </span>
          <span v-show="!icon">
            <i class="fas fa-lg fa-eye-slash"/>
          </span>
        </button>
      </span>
    </div>
    <label
      class="sr-only"
      for="inputNewPassword"
    >Password</label>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
// import BootstrapVue from "bootstrap-vue";
import jQuery from "jquery";
let $ = jQuery;

export default {
  name: "TheInputPassword",
  data() {
    return {
      iconCollapsed: true,
      icon: true
    }
  },
  methods: {
    // toggleIcon() {
    //   $('span').on('click', function () {
    //     $(this)
    //       .find('[data-fa-i2svg]')
    //       .toggleClass('fa-eye-slash')
    //       .toggleClass('fa-eye');
    //   });
    // }
  },
};
</script>



