<template>
	<b-input-group class="mb-1" prepend="Solve Math Captcha">
    <b-form-input id="input-default" name="mathcaptcha" placeholder="{{ placeholder }}" :state="inputCaptchaAnswer"> {{ placeholder }} </b-form-input>
	</b-input-group>
</template>


<script lang="ts">
import Vue from "vue";
import jQuery from "jquery";
let $ = jQuery;

function generateCaptcha() {
  var rnd1 = Math.ceil(Math.random()*20);
  var rnd2 = Math.ceil(Math.random()*20);
  var total:number = rnd1 + rnd2;
}

generateCaptcha();

export default {
  name: "MathCaptcha",
  data() {
    return {
      test: "testing",
      inputCaptchaAnswer: false,
    };
  },
  computed: {
    placeholder: function() {
      return this.test;
    }
  },
  mounted() {


  },
};
</script>
