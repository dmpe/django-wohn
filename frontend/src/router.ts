import Vue from "vue";
import Router from "vue-router";
import Administrace from "./views/Administrace.vue";
import Contact from "./views/Contact.vue";
import Home from "./views/Home.vue";
import Privacy from "./views/Privacy.vue";
import Terms from "./views/Terms.vue";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: {
        title: "Home Page - Example App",
        metaTags: [
          {
            name: "description",
            content: "The home page of our example app.",
          },
        ],
      },
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue"),
    },
    {
      path: "/contact",
      name: "contact",
      component: Contact,
    },
    {
      path: "/terms",
      name: "terms",
      component: Terms,
    },
    {
      path: "/privacy",
      name: "privacy",
      component: Privacy,
    },
    {
      path: "/administrace",
      name: "administrace",
      component: Administrace,
    },
  ],
});

router.afterEach((to, from) => {
  document.title = to.meta.title;
});

export default router;
