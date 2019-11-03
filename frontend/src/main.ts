import { BlobServiceClient } from "@azure/storage-blob";
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.css'
import Vue from "vue";
import App from "./App";
import router from "./router";
import store from "./store";
import { createProvider } from "./vue-apollo";

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  router,
  store,
  apolloProvider: createProvider(),
  render: (h) => h(App),
}).$mount("#app");
