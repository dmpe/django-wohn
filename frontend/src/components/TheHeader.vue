<template>
  <b-navbar
    class="headerFooterBackground"
    toggleable="sm"
    type="light"
    role="navigation"
  >
    <b-navbar-brand
      class="mb-0"
      href="/"
    >
      melive.xyz
      <span class="navbar-text d-md-inline-flex d-none d-md-block">
        <!-- be inline next to brand; hiden on small screens, i.e. display only on >= md (d-lg-block d-xl-block) -->
        Your next student colocation
      </span>
    </b-navbar-brand>

    <b-button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarLoginForm"
      aria-controls="navbarLoginForm"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon" />
    </b-button>

    <!-- // {# Full text search functionality, see #50, #35 #}
         <form role="form" class="form-inline my-2 my-lg-0 flex-fill justify-content-center" method="POST">
          {% csrf_token %}
          <div class="input-group">
            <input class="form-control py-2 border-right-0 border" type="search" placeholder="Search" id="example-search-input">
            <span class="input-group-append">
              <div class="input-group-text bg-transparent"><i class="fa fa-search"></i></div>
            </span>
          </div>
        </form>	 -->

    <!-- LOGIC: if not registered and not loged in, then show -->
    <!-- LOGIC: BUT on {register, reset_password, new_password, login}.html do not show -->
    <!-- LOGIC: CREATE logout button + click to userprofile as well -->
    <div
      id="navbarLoginForm"
      class="collapse navbar-collapse flex-row-reverse"
    >
      <div class="d-flex flex-row">
        <div v-if="isAuthenticated">
          <b-link
            to="administrace"
            type="button"
            class="btn btn-warning m-1"
          >
            My Profile
          </b-link>
          <b-link
            to="logout"
            type="button"
            class="btn btn-dark m-1"
          >
            Logout
          </b-link>
        </div>

        <div v-else>
          <b-link
            to="login"
            type="button"
            class="btn btn-success ml-0 mt-1 mb-1 mr-1"
          >
            Login
          </b-link>
          <b-link
            to="register"
            type="button"
            class="btn btn-danger m-1 pr-1"
          >
            Register to add new listings
          </b-link>
        </div>
      </div>
    </div>
  </b-navbar>
</template>

<script lang="ts">
import Vue from "vue";

export default {
  name: "TheHeader",
  data() {
    return {
      isAuthenticated:false
    };
  }
};
</script>
