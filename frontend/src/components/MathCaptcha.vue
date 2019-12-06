<template>
	<b-input-group class="mb-1" prepend="Solve Math Captcha">
    <b-form-input id="input-default" name="mathcaptcha" :placeholder="placeholder" :state="inputCaptchaAnswer"> </b-form-input>
	</b-input-group>
</template>


<script lang="ts">
import Vue from "vue";
import jQuery from "jquery";
let $ = jQuery;

export default Vue.extend({
  name: "MathCaptcha",
  data() {
    return {
      placeholder: "testing",
      inputCaptchaAnswer: false,
    };
  },
  methods: {
    generateCaptcha(): number[]  {
      let rnd1 = Math.ceil(Math.random()*20);
      let rnd2 = Math.ceil(Math.random()*20);
      let total:number = rnd1 + rnd2;
      return [rnd1, rnd2, total];
    }
  },
  computed: {
    prepareCap(): number[] {
      let results: number[] = this.generateCaptcha();
      return results;
    },
    changeState(): boolean {
      return this.inputCaptchaAnswer;
    }
  },
});
</script>
