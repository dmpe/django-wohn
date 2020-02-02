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
                <p>Test</p>
              </div>
            </div>

            <div class="col-md-6 mt-3">
              <div class="text-center">
                <form
                  id="form-register"
                  method="POST"
                >
                  <div class="form-group spacing">
                    <ValidationProvider rules="min:4" v-slot="{ errors }">
                      <div class="input-group">
                        <input
                          id="inputUsername"
                          type="text"
                          name="inputUsername"
                          class="form-control"
                          placeholder="Username"
                          required
                        >
                        <label
                          class="sr-only"
                          for="inputUsername"
                        >Username</label>
                        <span>{{ errors[0] }}</span>
                      </div>
                    </ValidationProvider>
                  </div>

                  <div class="form-group spacing">
                    <ValidationProvider rules="email" v-slot="{ errors }">
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
                        <span>{{ errors[0] }}</span>
                      </div>
                    </ValidationProvider>
                  </div>

                  <ValidationObserver>
                    <ValidationProvider rules="confirmed:confirmation" v-slot="{ errors }">
                      <div class="form-group spacing">
                        <TheInputPassword
                          password="inputPassword2"
                          button="buttonEYE2"
                        />
                      </div>
                      <span>{{ errors[0] }}</span>
                    </ValidationProvider>

                    <ValidationProvider v-slot="{ errors }" vid="confirmation">
                      <div class="form-group spacing">
                        <TheInputPassword
                          password="inputPassword3"
                          v-model="confirmation"
                          button="buttonEYE3"
                        />
                      </div>
                      <span>{{ errors[0] }}</span>
                    </ValidationProvider>
                  </ValidationObserver>

                  <div class="form-group spacing">
                    <MathCaptcha />
                  </div>

                  <div class="form-group spacing">
                    <ValidationProvider rules="required" v-slot="{ errors }">
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
                        <span>{{ errors[0] }}</span>
                      </div>
                    </ValidationProvider>
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






