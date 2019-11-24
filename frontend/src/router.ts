import Vue from "vue";
import Router from "vue-router";

import Administrace from "./views/user_management/profile/Homepage.vue";
import UserProfile from "./views/user_management/profile/UserProfile.vue";
import UserProperties from "./views/user_management/profile/UserProperties.vue";
import ResetPassword from "./views/user_management/ResetPassword.vue";
import Login from "./views/user_management/Login.vue";
import Register from "./views/user_management/Register.vue";
import Contact from "./views/Contact.vue";
import Home from "./views/Home.vue";
import Privacy from "./views/Privacy.vue";
import Terms from "./views/Terms.vue";
import NotFound from "./views/NotFound.vue";
import PropertyID from "./views/PropertyID.vue";


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
      path: "/login",
      name: "login",
      component: Login,
      meta: {
        title: "Login - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "Login page - Manage your real-estate listings",
          },
        ],
      },
    },
    {
      path: "/register",
      name: "register",
      component: Register,
      meta: {
        title: "Register - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "Sign up to Melive.xyz",
          },
        ],
      },
    },
    {
      path: "/reset-password",
      name: "resetpassword",
      component: ResetPassword,
      meta: {
        title: "Reset your password - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "Reset your profile password on Melive.xyz",
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
      children: [
        {
          path: "profile",
          name: "user-profile",
          component: UserProfile,
          meta: {
            title: "User Profile",
          },
        },
        {
          path: "properties",
          name: "user-properties",
          component: UserProperties,
          meta: {
            title:  "My properties",
          },
        }
      ]
    },
    {
      path: "/property/:id",
      name: "property-id",
      component: PropertyID
    },
    {
      // Any not listed above
      path: "*",
      name: "NotFound",
      component: NotFound,
      meta: {
        title: "Try again - 404 error - Melive.xyz",
        metaTags: [
          {
            name: "description",
            content: "We have not found what you have looked for. Try again.",
          },
        ],
      },
    }
  ],
});

router.afterEach((to, from) => {
  document.title = to.meta.title;
});

export default router;
