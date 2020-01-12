<template>
  <div>
    <TheHeader />
    <b-container fluid>
      <!--
  https://github.com/mfogel/django-timezone-field
  https://github.com/dmpe/django-wohn/issues/18
      -->
      <div class="row">
        <ProfileNav />

        <div class="row col-md-9 col-lg-9 col-xl-10 pt-3">
          <div class="col-xs-12 col-md-5 col-lg-5 col-xl-3 pr-2">
            ,   ,,,,,,,,    <div, class="col-md-12">
              <img
                src="firstof user.image.user_profile_image.url gravatar_url"
                alt="My Profile picture"
                class="rounded img-fluid"
              >

              <img
                src=""
                alt="My Profile picture"
                class="rounded img-fluid"
              >
            </div,>
          </div>
          <div class="col-md-12">
            <div class="pt-2">
              <form
                id="form-user-profile-image"
                class=""
                action="POST"
                enctype="multipart/form-data"
              >
                <div class="input-group mb-3">
                  <div class="custom-file">
                    <input
                      id="customFile"
                      type="file"
                      name="image"
                      class="custom-file-input"
                    >
                    <label
                      class="custom-file-label"
                      for="customFile"
                      aria-describedby="inputGroupFileAddon02"
                    >Image...</label>
                  </div>
                  <div class="input-group-append">
                    <button
                      id="inputGroupFileAddon02"
                      type="submit"
                      class="btn input-group-text"
                    >
                      Upload
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>

        <div class="col-xs-12 col-md-7 col-lg-7 col-xl-9 pt-2">
          <form
            id="form-user-settings"
            method="POST"
            class="mb-5"
          >
            <div class="form-row">
              <div class="form-group col-xs-5 col-sm-6 col-md-12 col-lg-6 col-xl-3">
                <!-- {{ form.user_gender | add_class:"form-control"}} -->
              </div>
              <div class="form-group col-xs-5 col-sm-6 col-md-12 col-lg-6 col-xl-4">
                <!-- {{ form.first_name | add_class:"form-control"}} -->
              </div>
              <div class="form-group col-xs-5 col-sm-6 col-md-12 col-lg-6 col-xl-4">
                <!-- {{ form.last_name | add_class:"form-control"}} -->
              </div>
              <div class="form-group col-xs-5 col-sm-6 col-md-12 col-lg-6 col-xl-3">
                <!-- {{ form.user_first_lastname_visibility | add_class:"form-control"}} -->
              </div>
              <div class="form-group col-xs-5 col-sm-6 col-md-12 col-lg-6 col-xl-4">
                <!-- {{ form.user_int_tel.label_tag }} {{ form.user_int_tel.errors }} -->
                <input
                  id="phone"
                  type="tel"
                  name="phone"
                  class="form-control"
                >
              </div>
              <div class="form-group col-xs-5 col-sm-6 col-md-12 col-lg-6 col-xl-4">
                <!-- {{ form.user_country | add_class:"form-control"}} -->
              </div>
              <div class="form-group col-xs-5 col-sm-6 col-md-12 col-lg-6 col-xl-4">
                <!-- {{ form.user_timezone | add_class:"form-control"}} -->
              </div>
              <div class="form-group col-sm-5 col-sm-6 col-md-12 col-lg-6 col-xl-4">
                <!-- {{ form.user_units_system | add_class:"form-control"}} -->
              </div>
            </div>
            <button
              type="submit"
              class="btn btn-warning mb-5 btn-lg btn-block"
            >
              Save
            </button>
          </form>

          <form
            id="form-user-username"
            method="POST"
            class="mb-5"
          >
            <div class="row">
              <div class="form-group col-md-3 col-sm-5">
                <label for="user_id_username">Current username</label>
                <input
                  class="form-control"
                  type="text"
                  name="user_id_username"
                  value=" "
                  readonly=""
                >
              </div>

              <div class="form-group col-md-3 col-sm-5">
                <!-- {{ form.inputUsername | add_class:"form-control"}} -->
              </div>
            </div>
            <button
              type="submit"
              class="btn btn-warning mb-5 btn-lg"
            >
              Save
            </button>
          </form>

          <form
            id="form-user-email"
            method="POST"
            class="mb-5"
          >
            <div class="row">
              <div class="form-group col-md-3 col-sm-5">
                <label for="user_id_email">Current email</label>
                <input
                  class="form-control"
                  type="text"
                  name=""
                  value=" "
                  readonly=""
                >
              </div>

              <div class="form-group col-md-3 col-sm-5">
                <!-- {{ form.inputEmail | add_class:"form-control"}} -->
              </div>
            </div>
            <button
              type="submit"
              class="btn btn-warning mb-5 btn-lg"
            >
              Save
            </button>
          </form>

          <form
            id="form-user-password"
            method="POST"
            class="mb-5"
          >
            <div class="row">
              <div class="form-group col-md-3 col-sm-5">
                <!-- {{ form.inputNewPassword | add_class:"form-control"}} -->
              </div>
              <div class="form-group col-md-3 col-sm-5">
                <!-- {{ form.inputConfirmNewPassword | add_class:"form-control"}} -->
              </div>
            </div>
            <button
              type="submit"
              class="btn btn-warning mb-5 btn-lg"
            >
              Save
            </button>
          </form>
        </div>
        <!--
				<p>Change currency, because default is CZK</p>
				<p>Change mt^2 to sq. foot</p> -->
      </div>
    </b-container>
  </div>
  </b-container>
  <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import ProfileNav from "@/components/TheNavSidebar.vue";
import BootstrapVue from "bootstrap-vue";

export default Vue.extend({
  name: "UserProfile",
  components: {
    TheHeader,
    ProfileNav,
    TheFooter,
  }
});

</script>
