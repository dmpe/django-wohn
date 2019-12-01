<template>
  <div class="input-group">
    <input
      v-bind:id="passwordInput"
      v-bind:type="[iconCollapsed ? 'password' : 'text']"
      v-bind:name="passwordInput"
      class="form-control"
      placeholder="Password"
    >
    <div class="input-group-append">
      <span
        id="inputGroupAppend"
        class="input-group-text"
      >
        <button
          v-bind:id="buttonInput"
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
      v-bind:for="passwordInput"
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
import { type } from 'os';
let $ = jQuery;

export default {
  name: "TheInputPassword",
  props: {
    passwordInput: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: false
    },
    buttonInput: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      iconCollapsed: true,
      icon: true
    }
  },
};
</script>



