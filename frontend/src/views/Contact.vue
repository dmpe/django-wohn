<template>
  <div class="contact">
    <TheHeader />

    <b-container>
      <div class="row">
        <div class="col-lg-6 col-md-8 col-sm-12 offset-md-3 text-center">
          <h1 class="custom-display-text-size">
            Contact us
          </h1>
        </div>
      </div>

      <div class="row">
        <div class="col-md-7 mt-3 col-sm-12">
          <div class="col align-self-center">
            <div class="card">
              <div class="card-body">
                <address>
                  Proudly developed at <br> <br>
                  Melive.xyz LLC (Delaware LLC) <br>
                  Pařížská 97/15, 110 00 <br>
                  Prague 1, Czech Republic, EU <br> <br>
                  For legal, developer-related <u>and</u> other type of questions, contact us at above address or via: <br>
                  <i class="fas fa-at" aria-hidden="true" /> Mr.
                  <script type="application/javascript">
                    <!-- http://hivelogic.com/enkoder/index.php -->
                    //<![CDATA[
                    <!--
                    var x="function f(x){var i,o=\"\",ol=x.length,l=ol;while(x.charCodeAt(l/13)!" +
                    "=92){try{x+=x;l+=l;}catch(e){}}for(i=l-1;i>=0;i--){o+=x.charAt(i);}return o" +
                    ".substr(0,ol);}f(\")25,\\\"meozpo1`r4'8$( (620\\\\e/&0 r\\\\100\\\\430\\\\a" +
                    "630\\\\g700\\\\\\\\\\\\TC_A420\\\\120\\\\n_X@Y000\\\\CLDHBc330\\\\QGFHCUl!g" +
                    "771\\\\4uwzhu}Lechaan420\\\\030\\\\C030\\\\100\\\\730\\\\030\\\\610\\\\000\\"+
                    "\\I5Z300\\\\600\\\\320\\\\7}:eu}==*9\\\"\\\\;0k7/ZPNZXQ\\\"(f};o nruter};))" +
                    "++y(^)i(tAedoCrahc.x(edoCrahCmorf.gnirtS=+o;721=%y;++y)25<i(fi{)++i;l<i;0=i" +
                    "(rof;htgnel.x=l,\\\"\\\"=o,i rav{)y,x(f noitcnuf\")"                         ;
                    while(x=eval(x));
                    //-->
                    //]]>
                  </script>
                </address>
                <i class="fab fa-twitter-square fa-3x mb-3" />
                <i class="fab fa-facebook-square fa-3x mb-3" />
                <iframe
                  class="my-1 responsive-map"
                  src="https://api.mapy.cz/frame?params=%7B%22x%22%3A14.419088677425833%2C%22y%22%3A50.08932926711133%2C%22base%22%3A%221%22%2C%22layers%22%3A%5B%5D%2C%22zoom%22%3A17%2C%22url%22%3A%22https%3A%2F%2Fen.mapy.cz%2Fs%2F3983p%22%2C%22mark%22%3A%7B%22x%22%3A%2214.419083313007807%22%2C%22y%22%3A%2250.089570190430784%22%2C%22title%22%3A%22ulice%20Pa%C5%99%C3%AD%C5%BEsk%C3%A1%2097%2F15%2C%20Praha%22%7D%2C%22overview%22%3Afalse%7D&amp;width=470&amp;height=333&amp;lang=en"
                  width="470"
                  height="333"
                  style="border:none"
                  frameBorder="0"
                />
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-5 col-sm-12">
          <form
            id="form-contact"
            method="POST"
            class="mb-5"
          >
            <div class="form-row">
              <div class="form-group col-md-12 col-sm-5" />

              <div class="form-group col-md-12 col-sm-7" />
            </div>

            <div class="form-group" />

            <div class="form-group">
              <!-- {{ form.inputText |add_class:"form-control"|attr:"rows:8"|attr:"cols:35"}} -->
            </div>

            <button
              id="recaptchaValidator"
              type="submit"
              class="btn btn-warning mb-5 btn-lg btn-block"
            >
              Submit message to Marek
            </button>
          </form>

          <!--<div
            id="checkEmailAlert"
             class="alert alert-{{ message.tags }} mb-5"
            role="alert"
          />-->
        </div>
      </div>
    </b-container>
    <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue"; // @ is an alias to /src
import BootstrapVue from "bootstrap-vue";

export default Vue.extend({
  name: "Contact",
  components: {
    TheHeader,
    TheFooter,
  }
});
</script>
