<template>
  <div class="input-group">
    <!-- when header already contains `buttonEYE` then here one needs a different id attr. -->
    <input
      id="inputNewPassword"
      v-bind:type="iconCollapsedInput"
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
          v-on:click="iconCollapsedInput = !iconCollapsedInput"
        >
          <span>
            <i class="fas fa-lg fa-eye" />
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
import BootstrapVue from "bootstrap-vue";
import jQuery from "jquery";
let $ = jQuery;

export default {
  name: "TheInputPassword",
  data() {
    return {

    };
  },
  computed: {
    iconCollapsedInput() {
      return this.iconCollapsed ? 'password' : 'text';
    }
  },
  methods: {
    toggleIcon: function() {
      $('button').on('click', function () {
        $(this)
          .find('[data-fa-i2svg]')
          .toggleClass('fa-eye')
          .toggleClass('fa-eye-slash');
      });
    }
  },
};
</script>



