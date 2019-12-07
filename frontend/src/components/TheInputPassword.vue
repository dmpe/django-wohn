<template>
  <div class="input-group">
    <input
      v-bind:id="password-input"
      v-bind:type="[iconCollapsed ? 'password' : 'text']"
      v-bind:name="password-input"
      class="form-control"
      placeholder="Password"
    >
    <div class="input-group-append">
      <span
        id="inputGroupAppend"
        class="input-group-text"
      >
        <button
          v-bind:id="button-input"
          v-on:click="iconCollapsed = !iconCollapsed; icon = !icon"
          class="resetIconStylesEYE"
          aria-hidden="true"
          type="button"
        >
          <span v-show="icon">
            <i class="fas fa-lg fa-eye" />
          </span>
          <span v-show="!icon">
            <i class="fas fa-lg fa-eye-slash" />
          </span>
        </button>
      </span>
    </div>
    <label
      v-bind:for="password-input"
      class="sr-only"
    >Password</label>
  </div>
</template>


<style lang="stylus" scoped>
.resetIconStylesEYE
    border none
    background none
    padding-top 0rem
    padding-right 0.75rem
    padding-bottom 0rem
    padding-left 0.75rem
</style>

<script lang="ts">
import Vue from "vue";
import jQuery from "jquery";
import { type } from "os";
const $ = jQuery;

export default {
  name: "TheInputPassword",
  props: {
    password-input: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: false
    },
    button-input: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      iconCollapsed: true,
      icon: true
    };
  },
};
</script>



