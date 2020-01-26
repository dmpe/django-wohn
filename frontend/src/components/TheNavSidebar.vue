<template>
  <div class="col-md-6 col-lg-6 col-xl-3 pt-3 d-none d-md-block">
    <aside>
      <ul class="nav nav-pills d-flex flex-column">
        <li class="nav-item">
          <a
            href="/administrace"
            class="nav-link active"
          >
            <i
              class="fas fa-home fa-lg"
              aria-hidden="true"
            />
            <span class="ml-3">Homepage</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="/administrace/profile"
            class="nav-link"
          >
            <i
              class="fas fa-user fa-lg"
              aria-hidden="true"
            />
            <span class="ml-3">My profile</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="/administrace/properties"
            class="nav-link"
          >
            <i
              class="fas fa-hotel fa-lg"
              aria-hidden="true"
            />
            <span class="ml-3">Properties</span>
            <span class="badge badge-success badge-pill"> {{ myProperties }}</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="/administrace/messages"
            class="nav-link"
          >
            <i
              class="fas fa-envelope fa-lg"
              aria-hidden="true"
            />
            <span class="ml-3">Messages</span>
            <span class="badge badge-danger badge-pill"> {{ unreadMessages }}</span>
          </a>
        </li>
        <!-- IDEA: if user is advertisor, see stage-2 #}
        {% if request.user.is_active and request.user.is_staff %} -->
        <li class="horizontal_line d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          Advertising
        </li>
        <li class="nav-item">
          <a
            href="/administrace/properties"
            class="nav-link"
          >
            <i
              class="fas fa-ad fa-lg"
              aria-hidden="true"
            />
            <span class="ml-3">My property ads</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="/administrace/statistics"
            class="nav-link"
          >
            <i
              class="fas fa-signal fa-lg"
              aria-hidden="true"
            />
            <span class="ml-3">Statistics</span>
          </a>
        </li>

      </ul>
    </aside>

    <div class="row d-block d-xs-block d-sm-block d-md-none">
      <ul class="d-flex flex-row list-group flex-wrap">
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="/administrace"
            class="nav-link"
          >
            <i
              class="fas fa-home fa-lg"
              aria-hidden="true"
            />
          </a>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="/administrace/profile"
            class="nav-link"
          >
            <i
              class="fas fa-user fa-lg"
              aria-hidden="true"
            />
          </a>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="/administrace/properties"
            class="nav-link"
          >
            <i
              class="fas fa-hotel fa-lg"
              aria-hidden="true"
            />
            <span class="badge badge-success badge-pill"> {{ myProperties }}</span>
          </a>
        </li>

        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="/administrace/messages"
            class="nav-link"
          >
            <i
              class="fas fa-envelope fa-lg"
              aria-hidden="true"
            />
            <span class="badge badge-danger badge-pill"> {{ unreadMessages }}</span>
          </a>
        </li>
        {% if request.user.is_active and request.user.is_staff %}
        <li class="list-group-item justify-content-between align-items-center">
          <a
            href="/administrace/properties"
            class="nav-link"
          >
            <i
              class="fas fa-ad fa-lg"
              aria-hidden="true"
            />
          </a>
        </li>
        <li class="list-group-item justify-content-between align-items-center">
          <a
            href="/administrace/statistics"
            class="nav-link"
          >
            <i
              class="fas fa-signal fa-lg"
              aria-hidden="true"
            />
          </a>
        </li>

      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
import gql from "graphql-tag";
import { myProperties } from "@/graphql/user/properties.ts";

export default {
  name: "ProfileNav",
  // apollo: {
  //   myProperties: {
  //     query: myProperties
  //   }
  // },
  data() {
    return {
      unreadMessages: 0,
      myProperties: 0,
    };
  }
};
</script>


