import Vue from "vue";
import App from "./App";
import BootstrapVue from 'bootstrap-vue';
import router from "./router";
import store from "./store";
import { BlobServiceClient } from "@azure/storage-blob";
import { createProvider } from "./vue-apollo";
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  apolloProvider: createProvider(),
  render: h => h(App)
}).$mount("#app");
