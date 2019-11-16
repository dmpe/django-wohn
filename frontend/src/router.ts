import Administrace from "./views/Administrace.vue";
import Contact from "./views/Contact.vue";
import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Privacy from "./views/Privacy.vue";
import Terms from "./views/Terms.vue";
import NotFound from "./views/404NotFound.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: {
        title: "Home Page - Student Housing in Czechia - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "Home page",
          },
        ],
      },
    },
    {
      path: "/about",
      name: "about",
      // Route level code-splitting
      // This generates a separate chunk (about.[hash].js) for this route
      // Which is lazy-loaded when the route is visited.
      component: () =>
        import(/* WebpackChunkName: "about" */ "./views/About.vue"),
      meta: {
        title: "About Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "About page - Learn more about people behind melive.xyz",
          },
        ],
      },
    },
    {
      path: "/contact",
      name: "contact",
      component: Contact,
      meta: {
        title: "Contact owners & developers - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "Contact page",
          },
        ],
      },
    },
    {
      path: "/terms",
      name: "terms",
      component: Terms,
      meta: {
        title: "Terms of use - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "Terms page - Your terms of use on melive.xyz",
          },
        ],
      },
    },
    {
      path: "/privacy",
      name: "privacy",
      component: Privacy,
      meta: {
        title: "Privacy policy - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "Privacy page - Your privacy when using melive.xyz",
          },
        ],
      },
    },
    {
      path: "/administrace",
      name: "administrace",
      component: Administrace,
      meta: {
        title: "User Settings - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "User Setttings (administrace) page",
          },
        ],
      },
    },
    {
      // Any not listed above
      path: "*",
      name: "NotFound",
      component: NotFound
    }
  ],
});

router.afterEach((to, from) => {
  document.title = to.meta.title;
});

export default router;
