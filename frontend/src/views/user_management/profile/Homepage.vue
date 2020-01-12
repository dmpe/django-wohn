<template>
  <div>
    <TheHeader />
    <div class="container-fluid">
      <div class="row ">
        <ProfileNav />

        <div class="col-md-9 col-lg-9 col-xl-10">
          <h1 class="display-4 d-none d-sm-block">
            <!-- Welcome back {{ user.username }} -->
          </h1>
          <h3 />

          <div class="d-flex flex-wrap">
            <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 p-2">
            <div class="card bg-success text-white h-100">
              <a
                href="/administrace/properties"
                class="card_homepage_styling"
              >
                <div class="card-body bg-success">
                  <h6 class="text-uppercase">Properties</h6>
                  <!-- <h2 class="display-2">{{ number_of_properties }}</h2> -->
                </div>
              </a>
            </div>
          </div>

          <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 p-2">
            <div class="card bg-warning h-100">
              <div class="card-body bg-warning">
                <h6 class="text-uppercase">
                  Google Analytics Homepage Views
                </h6>
                <h2 class="display-2">
                  <!-- {{ number_of_views }} -->
                </h2>
              </div>
            </div>
          </div>

          <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 p-2">
            <div class="card bg-secondary text-white h-100">
              <a
                href="/administrace/messages"
                class="card_homepage_styling"
              >
                <div class="card-body bg-secondary">
                  <h6 class="text-uppercase">Messages</h6>
                  <!-- <h2 class="display-2">{{ unread_thread_count }}</h2> -->
                </div>
              </a>
            </div>
          </div>
        </div>

        <div class="d-flex flex-wrap">
          <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 p-2 mb-3">
            <div class="card">
              <div class="card-header">
                On our Blog
              </div>

              <div class="card-body">
                <!-- {% for blog_item in news_collection %} -->
                <div class="news_collection">
                  <p>testing...</p>
                </div>
                <!-- {% endfor %} -->
              </div>
            </div>
          </div>

          <div class="col-sm-4 col-md-4 col-lg-4 col-xl-4 p-2 d-none d-md-none d-lg-block">
            <div class="card">
              <div class="card-header">
                Do you want more features?
              </div>

              <div class="card-body">
                Submit here or <a href="https://github.com/dmpe/django-wohn/issues">open an issue at GitHub.</a>

                <form
                  id="form-admin-feedback"
                  method="POST"
                  class=""
                >
                  <div class="form-group">
                    <!-- {{ form.inputFeedback |add_class:"form-control"|attr:"rows:5"|attr:"cols:35"}} -->
                  </div>

                  <button
                    type="submit"
                    class="btn btn-warning mb-2 btn-lg btn-block"
                  >
                    Submit feedback
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
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
  name: "Login",
  components: {
    TheHeader,
    ProfileNav,
    TheFooter,
  }
});
</script>
