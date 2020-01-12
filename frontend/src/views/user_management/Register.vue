<template>
  <div>
    <TheHeader />
    <b-container fluid>
      <!-- Because of Facebook login -->
      <div id="fb-root" />

      <!-- TODO what if user wants to logout or deasscoiate accounts: is registeration page available to him -->
      <div class="row d-flex justify-content-center login_register_box">
        <div class="card">
          <div class="card-header text-center">
            <h1 class="card-title">
              Register
            </h1>
          </div>

          <div class="row card-body">
            <div class="col-md-6">
            <div class="text-center">
              <!-- Google Brand Guidelines on Azure/ in CSS: https://developers.google.com/identity/branding-guidelines -->
              <div class="m-3">
                <a
                  type="button"
                  class="btn btn-primary google_signin"
                  href=" "
                >
                  <img
                    class="google_icon"
                  >
                  <p class="text-center mt-1 text-white">Sign Up With Google</p>
                </a>
              </div>

              <!-- Twitter Brand Guidelines on Azure/ in CSS -->
              <div class="m-3">
                <a
                  type="button"
                  class="btn btn-info twitter_singin"
                  href=""
                >
                  <img
                    class="twitter_icon"
                  >
                  <p class="text-center mt-1 text-white">Sign Up With Twitter</p>
                </a>
              </div>

              <!-- https://developers.facebook.com/docs/facebook-login/web/login-button -->
              <div class="m-3">
                <a
                  type="button"
                  class="btn btn-white facebook_singin"
                  data-onsuccess="onSignIn"
                  href=""
                >
                  <img
                    class="facebook_icon"
                  >
                  <p class="text-center mt-1 text-white">Sign Up With Facebook</p>
                </a>
              </div>
            </div>
          </div>

          <div class="col-md-6 mt-3">
            <div class="text-center">
              <form
                id="form-register"
                method="POST"
              >
                <div class="form-group spacing">
                  <div class="input-group">
                    <input
                      id="inputUsername"
                      type="text"
                      name="inputUsername"
                      class="form-control"
                      placeholder="Username"
                      minlength="4"
                      required
                    >
                    <label
                      class="sr-only"
                      for="inputUsername"
                    >Username</label>
                    <div class="invalid-tooltip">
                      Please choose a username with >= 4 letters.
                    </div>
                  </div>
                </div>
                <div class="form-group spacing">
                  <div class="input-group">
                    <input
                      id="inputEmail"
                      class="form-control"
                      type="email"
                      name="inputEmail"
                      placeholder="Email"
                      required
                    >
                    <label
                      class="sr-only"
                      for="inputEmail"
                    >Email</label>
                    <div class="invalid-tooltip">
                      Please choose a valid email address.
                    </div>
                  </div>
                </div>
                <div class="form-group spacing">
                  <TheInputPassword
                    password="inputPassword2"
                    button="buttonEYE2"
                  />
                </div>

                <div class="form-group spacing">
                  <TheInputPassword
                    password="inputPassword3"
                    button="buttonEYE3"
                  />
                </div>

                <div class="form-group spacing">
                  <MathCaptcha />
                </div>

                <div class="form-group spacing">
                  <div class="form-check">
                    <input
                      id="invalidCheck"
                      class="form-check-input"
                      type="checkbox"
                      value=""
                      required
                    >
                    <label
                      class="form-check-label"
                      for="invalidCheck"
                    >
                      I agree to <a href="/terms">Terms and Conditions</a> as well as <a href="/privacy">Privacy Policy</a>
                    </label>
                    <div class="invalid-feedback">
                      You must agree to <a href="/terms">Terms and Conditions</a> as well as <a href="/privacy">Privacy Policy</a> before submitting.
                    </div>
                  </div>
                </div>

                <p class="float-left">
                  <a href="/reset-password">Forgot your username or password?</a>
                </p>

                <button
                  @click="submit"
                  type="submit"
                  class="btn btn-warning float-right btn-lg"
                >
                  Register
                </button>
              </form>
            </div>

            <!-- <div
                id="checkEmailAlert"
                class="alert alert-{{ message.tags }} messageErrorLoginSignup"
                role="alert"
              > -->
            <!-- {{ message }} -->
          </div>
        </div>
      </div>
    </div>
  </b-container>
  <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import TheInputPassword from "@/components/TheInputPassword.vue";
import MathCaptcha from "@/components/MathCaptcha.vue";

export default Vue.extend({
  name: "Register",
  components: {
    TheHeader,
    TheInputPassword,
    MathCaptcha,
    TheFooter,
  },
  data() {
    return {
      submitStatus: null,
    };
  },
  methods: {
    submit() {
      console.log("click");
    }
  },
});
</script>






