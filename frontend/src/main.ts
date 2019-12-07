import { BlobServiceClient } from "@azure/storage-blob";
import BootstrapVue from "bootstrap-vue";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "bootstrap/dist/css/bootstrap.css";
import "@/assets/app.styl";
import Vue from "vue";
import App from "./App";
import router from "./router";
import store from "./store";
import { createProvider } from "./vue-apollo";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);
Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  router,
  store,
  apolloProvider: createProvider(),
  render: h => h(App),
}).$mount("#app");
