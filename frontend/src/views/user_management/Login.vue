<template>
  <div>
    <TheHeader />
    <b-container fluid>

      <div class="row d-flex justify-content-center login_register_box">
        <div class="card">
          <div class="card-header text-center">
            <h1 class="card-title">
              Login
            </h1>
          </div>

          <div class="row card-body">
            <div class="col-md-6">
              <p>Test</p>
            </div>

            <div class="col-md-6 mt-3">
              <div class="text-center">
                <form
                  id="form-login"
                  method="POST"
                >
                  <div class="form-group spacing">
                    <div class="input-group">
                      <input
                        id="inputEmail_Username"
                        class="form-control"
                        type="text"
                        name="inputEmail_Username"
                        placeholder="Your email or username"
                      >
                      <label
                        class="sr-only"
                        for="inputEmail_Username"
                      >Your email or username</label>
                    </div>
                  </div>

                  <div class="form-group spacing">
                    <TheInputPassword
                      password="inputPassword"
                      button="buttonEYE"
                    />
                  </div>

                  <div class="form-group spacing">
                    <MathCaptcha />
                  </div>

                  <p class="float-left">
                    <a href="/reset-password">Forgot your username or password?</a>
                  </p>

                  <!-- Also includes Google Recaptcha v3 -->
                  <button
                    class="btn btn-warning float-right btn-lg"
                    type="submit"
                  >
                    Login
                  </button>
                </form>
              </div>

              <!-- <div
                id="checkEmailAlert"
                class="alert alert-{{ message.tags }} messageErrorLoginSignup"
                role="alert"
              > -->
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
  name: "Login",
  components: {
    TheHeader,
    TheInputPassword,
    MathCaptcha,
    TheFooter,
  },
  data() {
    return {

    };
  }
});
</script>
