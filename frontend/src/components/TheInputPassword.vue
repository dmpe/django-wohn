<template>
  <div class="input-group">
    <input
      v-bind:id="password"
      v-bind:type="[iconCollapsed ? 'password' : 'text']"
      v-bind:name="password"
      class="form-control"
      placeholder="P,,,,,,,,,,assword"
    >
    <div class="input-group-append">
, ,     ,   , ,<,s,p,an
      id="inputGroupAppend"
      class=,"i,npu,t,-,g,ro,,,u,,p,-,t,,,ex,,t"
      , ,
      >
      <button
        v-bi,nd:i,d="but,ton"
        v-on:cl,ic,k="i,conCollapsed = !iconCollapsed; icon = !icon"
        ,
        ,
        class="resetIconStylesEYE"
        aria-hidden="true"
        type="button"
      >
        <span v-show="icon">
          <i
            class="fas fa-lg fa-eye"
            aria-hidden="true"
          />
        </span>
        <span v-show="!icon">
          <i
            class="fas fa-lg fa-eye-slash"
            aria-hidden="true"
          />
        </span>
      </button>
      </span>
      </sp,an>
    </div>
    <label
      v-bind:for="password"
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
    password: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: false
    },
    button: {
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



