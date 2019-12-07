<template>
  <b-input-group
    class="mb-1"
    prepend="Solve Math Captcha"
  >
    <b-form-input
      id="input-default"
      :placeholder="placeholder"
      :state="changeState()"
      name="mathcaptcha"
    />
  </b-input-group>
</template>


<script lang="ts">
import Vue from "vue";
import jQuery from "jquery";
const $ = jQuery;

export default Vue.extend({
  name: "MathCaptcha",
  data() {
    return {
      placeholder: "",
      inputCaptchaAnswer: false,
    };
  },
  computed: {
    prepareCap(): string {
      const results: number[] = this.generateCaptcha();
      return this.placeholder = "results[0] + results[1] = ...";
    },
    changeState(): boolean {
      return this.inputCaptchaAnswer;
    }
  },
  methods: {
    generateCaptcha(): number[]  {
      const rnd1 = Math.ceil(Math.random()*20);
      const rnd2 = Math.ceil(Math.random()*20);
      const total: number = rnd1 + rnd2;
      return [rnd1, rnd2, total];
    }
  },
});
</script>
