<template>
  <b-input-group
    class="mb-1"
    prepend="Solve Math Captcha"
  >
    <b-form-input
      id="input-default"
      :placeholder="prepareCap"
      :state="inputCaptchaAnswer"
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
      placeholder: '',
      inputCaptchaAnswer: false,
    };
  },
  computed: {
    prepareCap(): string {
      const results: number[] = this.generateCaptcha();
      let placestring: string = results[0].toString().concat(" + ", results[1].toString(), " = ...");
      return placestring;
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
