<template>
  <div class="reset_password">
    <TheHeader />
    <b-container fluid>
      <!-- {% if not user.is_authenticated %} -->

      <div class="row card passwordReset">
        <div class="card-header text-center">
          <h1 class="card-title">
            Reset your password
          </h1>
          <p class="card-subtitle text-muted">
            Step 1 of 2
          </p>
        </div>
        <div class="card-body">
          <form
            id="form-reset-password"
            method="POST"
          >
            <div class="form-group spacing">
              <input
                id="inputEmail_Username"
                class="form-control"
                type="text"
                name="inputEmail_Username"
                placeholder="Your email or username"
                required
                autofocus
              >
              <label
                class="sr-only"
                for="inputEmail_Username"
              >Your email or username</label>
            </div>

            <button
              id="recaptchaValidator"
              type="submit"
              class="btn btn-dark float-right btn-lg g-recaptcha"
              data-sitekey="6LeZy3MUAAAAALMLtwqi7aTHvXnvdY6sx5ALYVp5"
              name="g-recaptcha-response"
              data-callback="onSubmit"
            >
              Reset
            </button>
          </form>
        </div>

        <!-- {% comment %}
			If username or email is correct
				then shows alert message
			if incorrect
				then a different alert message
		{% endcomment %}
		{% if messages %}
			{% for message in  messages %} -->
        <!-- <div
          id="checkEmailAlert"
          class="alert alert-{{ message.tags }}"
          role="alert"
        > -->
          <!-- {{ message }} -->
        <!-- </div> -->
        <!-- {% endfor %}
		{% endif %} -->
      </div>

      <!-- {% comment %}
  else
    show a profile page where he can change it by himself
  {% endcomment %}
  {% else %} -->
      <script type="application/javascript">
        var timer = setTimeout(function() {
        window.location = 'https://melive.xyz/administrace/user_profile'
        }, 1000);
      </script>
      <!-- {% endif %} -->
    </b-container>
    <TheFooter />
  </div>
</template>



<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";

export default Vue.extend({
  name: "ResetPassword",
  components: {
    TheHeader,
    TheFooter,
  }
});
</script>

