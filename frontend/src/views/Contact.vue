<template>
  <div class="contact">
    <TheHeader />

    <b-container>
      <div class="row">
          <div class="col-lg-6 col-md-8 col-sm-12 offset-md-3 text-center">
            <h1 class="custom-display-text-size">Contact us</h1>
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
                  <i class="fas fa-at"></i> Mr.
                  <script type="text/javascript">
                    // Generated through http://hivelogic.com/enkoder/index.php
                    //<![CDATA[
                    <!--
                    var x="function f(x){var i,o=\"\",l=x.length;for(i=0;i<l;i+=2) {if(i+1<l)o+=" +
                    "x.charAt(i+1);try{o+=x.charAt(i);}catch(e){}}return o;}f(\"ufcnitnof x({)av" +
                    " r,i=o\\\"\\\"o,=l.xelgnhtl,o=;lhwli(e.xhcraoCedtAl(1/)3=!26{)rt{y+xx=l;=+;" +
                    "lc}tahce({)}}of(r=i-l;1>i0=i;--{)+ox=c.ahAr(t)i};erutnro s.buts(r,0lo;)f}\\" +
                    "\"(8),9\\\"\\\\o[tee~v;.d&=2:>:00\\\\0o\\\\(%*>07\\\\0w\\\\3j03\\\\\\\\ -\\" +
                    "\\6\\\\\\\"7\\\\01\\\\\\\\,a_VYP33\\\\0U\\\\0M03\\\\\\\\\\\\\\\\\\\\\\\\\\\\"+
                    "U\\\\\\\\X\\\\0p02\\\\\\\\rm\\\\\\\\BJEYn_\\\\\\\\13\\\\0t\\\\35\\\\0\\\\\\" +
                    "\\\\\\\\\\F\\\\\\\\n3\\\\02\\\\\\\\26\\\\0c\\\\35\\\\0k\\\\x}yvjom';uryk||u" +
                    "bNegjonf?ewkhn3a02\\\\\\\\ _4F03\\\\\\\\34\\\\0n\\\\\\\\\\\\37\\\\0V\\\\24\\"+
                    "\\0H\\\\ZQ37\\\\04\\\\03\\\\\\\\\\\\n2\\\\03\\\\\\\\04\\\\06\\\\03\\\\\\\\3" +
                    "4\\\\0D\\\\35\\\\06\\\\00\\\\\\\\02\\\\03\\\\01\\\\\\\\20\\\\07\\\\00\\\\\\" +
                    "\\14\\\\06\\\\00\\\\\\\\\\\"\\\\f(;} ornture;}))++(y)^(iAtdeCoarchx.e(odrCh" +
                    "amCro.fngriSt+=;o27=1y%2;*=)yy)8+(9i>f({i+)i+l;i<0;i=r(foh;gten.l=x,l\\\"\\" +
                    "\\\\\"\\\\o=i,r va){,y(x fontincfu)\\\"\")"                                  ;
                    while(x=eval(x));
                    //-->
                    //]]>
                  </script>
                </address>
                <i class="fab fa-twitter-square fa-3x mb-3"></i>
                <i class="fab fa-facebook-square fa-3x mb-3"></i>
                <iframe class="my-1 responsive-map" src="https://api.mapy.cz/frame?params=%7B%22x%22%3A14.419088677425833%2C%22y%22%3A50.08932926711133%2C%22base%22%3A%221%22%2C%22layers%22%3A%5B%5D%2C%22zoom%22%3A17%2C%22url%22%3A%22https%3A%2F%2Fen.mapy.cz%2Fs%2F3983p%22%2C%22mark%22%3A%7B%22x%22%3A%2214.419083313007807%22%2C%22y%22%3A%2250.089570190430784%22%2C%22title%22%3A%22ulice%20Pa%C5%99%C3%AD%C5%BEsk%C3%A1%2097%2F15%2C%20Praha%22%7D%2C%22overview%22%3Afalse%7D&amp;width=470&amp;height=333&amp;lang=en" width="470" height="333" style="border:none" frameBorder="0"></iframe>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-5 col-sm-12">
          <form method="POST" id="form-contact" class="mb-5">

            <div class="form-row">
              <div class="form-group col-md-12 col-sm-5">

              </div>

              <div class="form-group col-md-12 col-sm-7">

              </div>
            </div>

            <div class="form-group">

            </div>

            <div class="form-group">
              {{ form.inputText |add_class:"form-control"|attr:"rows:8"|attr:"cols:35"}}
            </div>

            <button type="submit" class="btn btn-warning mb-5 btn-lg btn-block" id="recaptchaValidator">Submit message to Marek</button>
          </form>

          <div class="alert alert-{{ message.tags }} mb-5" id="checkEmailAlert" role="alert">
            {{ message }}
          </div>
       </b-container>
    <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue"; // @ is an alias to /src

export default Vue.extend({
  name: "Contact",
  components: {
    TheHeader,
    TheFooter,
  }
});
</script>
