<template>
  <div class="contact">
    <TheHeader />

    <b-container>
      <b-row>
        <div class="col-lg-6 col-md-8 col-sm-12 offset-md-3 text-center">
          <h1 class="custom-display-text-size">
            Contact us
          </h1>
        </div>
      </b-row>

      <b-row>
        <div class="col-md-7 mt-3 col-sm-12">
          <div class="col align-self-center">
            <div class="card">
              <div class="card-body">
                <address>
                  Proudly developed at <br> <br>
                  Melive.xyz LLC <br>
                  Pařížská 97/15, 110 00 <br>
                  Prague 1, Czech Republic, EU <br> <br>
                  For legal, developer-related <u>and</u> other type of questions, contact us at above address or via: <br>
                  <i
                    class="fas fa-at"
                    aria-hidden="true"
                  /> Mr. Malinkovsky
                  <a
                    href=""
                    class="mywebaddress"
                    data-name="devil"
                    data-domain="web"
                    data-tld="de"
                    onclick="window.location.href = 'mailto:' + this.dataset.name + '@' + this.dataset.domain + '.' + this.dataset.tld; return false;"
                  />
                </address>
                <i
                  class="fab fa-twitter-square fa-3x mb-3"
                  aria-hidden="true"
                />
                <i
                  class="fab fa-facebook-square fa-3x mb-3"
                  aria-hidden="true"
                />
                <iframe
                  title="Mapy.cz Location of Melive.xyz office"
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
          <b-form
            id="form-contact"
            @submit="onSubmit"
            method="POST"
            class="mb-5"
          >
            <ValidationProvider rules="min:2" v-slot="{ errors }">
              <b-form-group
                label="Name"
                label-for="input-name"
              >
                <b-form-input
                  id="input-name"
                  v-model="form.name"
                  trim
                />
                <span>{{ errors[0] }}</span>
              </b-form-group>
            </ValidationProvider>

            <ValidationProvider name="Email" rules="email" v-slot="{ errors }">
              <b-form-group
                label="Email"
                label-for="input-email"
              >
                <b-form-input
                  id="input-email"
                  v-model="form.email"
                  trim
                />
                <span>{{ errors[0] }}</span>
              </b-form-group>
            </ValidationProvider>

            <ValidationProvider name="Subject" rules="min:5" v-slot="{ errors }">
              <b-form-group
                label="Subject"
                label-for="input-subject-line"
              >
                <b-form-input
                  id="input-subject-line"
                  name="input-subject-line"
                  v-model="form.subject"
                  trim
                />
                <span>{{ errors[0] }}</span>
              </b-form-group>
            </ValidationProvider>

              <b-form-group
                label="Choce reason to contact us"
                label-for="options-select"
              >
                <b-form-select
                  id="options-select"
                  v-model="form.selected"
                  :options="form.options"
                />
              </b-form-group>

            <ValidationProvider name="Message" rules="required" v-slot="{ errors }">
              <b-form-group
                label="Your message"
                label-for="textarea-large"
              >
                <b-form-textarea
                  id="textarea-large"
                  v-model="form.textarea"
                  placeholder="..."
                  size="lg"
                  rows="5"
                  max-rows="10"
                />
                <span>{{ errors[0] }}</span>
              </b-form-group>
            </ValidationProvider>

            <b-form-group>
              <b-button
                type="submit"
                class="btn btn-warning mb-5 btn-lg btn-block"
              >
                Submit your message
              </b-button>
            </b-form-group>
          </b-form>

        </div>
      </b-row>
    </b-container>
    <TheFooter />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";
import BootstrapVue from "bootstrap-vue";
import gql from "graphql-tag";
import { contactUs } from "@/graphql/user/contact_us.ts";

export default Vue.extend({
  name: "Contact",
  components: {
    TheHeader,
    TheFooter,
  },
  data() {
    return {
      form: {
        name: '',
        email: '',
        subject: '',
        textarea: '',
        selected: "general",
        options: [
          { value: "general", text: "General Questions/Others" },
          { value: "ads", text: "Advertising" },
          { value: "help_me", text: "Bugs/Issues on the website" },
          { value: "com_abs_similar", text: "Fraud/Takedowns/Bans/Abuse" },
        ]
      }
    };
  },
  methods: {
		sendMessageInquery () {

      const options = this.form.options
      const name = this.form.name
      const email = this.form.email
      const textarea = this.form.textarea
      const subject = this.form.subject

      try {
        this.$apollo.mutate({
          mutation: contactUs,
          variables: {
            options,
            name,
            email,
            textarea,
            subject
          },
        })
      } catch (e) {
        console.error(e)
      }
    },
    onSubmit(evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
    },
	},

});
</script>
