<template>
  <footer class="footer headerFooterBackground">
    <div class="float-left d-none d-md-block d-lg-block">
      <!-- hiden on sm,,,,,,,,,,all screens, i.e. display only on >= md -->
      <span class="pl-3">Made with <i
        class="fas fa-heart footer_heartIcon"
        aria-hidden="true"
      /> by <a
        href="https://www.linkedin.com/in/dmitrijpetrov/"
        target="_blank"
        rel="noopener noreferrer"
      >@dmpe</a></span>
      <figcaption class="figure-caption">
        <small class="pl-3 text-muted font-italic">Source Code available under the <a
          href="https://choosealicense.com/licenses/mit/"
          rel="noopener noreferrer"
          target="_blank"
        >MIT license</a> <a
          href="https://github.com/dmpe/django-wohn"
          target="_blank"
          rel="noopener noreferrer"
        >on GitHub</a></small>
      </figcaption>
    </div>

    <div class="float-right">
      <ul class="list-inline">
        <li class="list-inline-item mx-3 my-1">
          <a
            href="about"
            class=""
          >About</a>
        </li>
        <li class="list-inline-item mx-3 my-1">
          <a
            href="contact"
            class=""
          >Contact us</a>
        </li>
        <li class="list-inline-item mx-3 my-1">
          <a
            href="privacy"
            class=""
          >Privacy Policy</a>
        </li>
        <li class="list-inline-item mx-3 my-1">
          <a
            href="terms"
            class=""
          >Terms of Use</a>
        </li>
      </ul>
    </div>
  </footer>
</template>

<style lang="stylus" scoped>

.footer
    position absolute
    bottom 0
    left 0px
    width 100%
    line-height 1rem
    padding-top 15px

.footer_heartIcon
    color red

</style>

<script lang="ts">
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";

export default {
  name: "TheFooter",
  data() {
    return {

    };
  }
};
</script>
