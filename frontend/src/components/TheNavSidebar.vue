<template>
  <div>
    <aside class="col-md-3 col-lg-3 col-xl-2 pt-3 d-none d-md-block">
      <ul class="nav nav-pills d-flex flex-column">
        <li class="nav-item">
          <a
            href="/administrace"
            class="nav-link {% if url_name == 'userMng:userMng_index' %}active{% endif %}"
          >
            <i class="fas fa-home fa-lg" />
            <span class="ml-3">Homepage</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="/administrace/profile"
            class="nav-link {% if url_name == 'userMng:user_profile' %}active{% endif %}"
          >
            <i class="fas fa-user fa-lg" />
            <span class="ml-3">My profile</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="/administrace/properties"
            class="nav-link {% if url_name == 'userMng:user_properties' %}active{% endif %}"
          >
            <i class="fas fa-hotel fa-lg" />
            <span class="ml-3">Properties</span>
            <span class="badge badge-success badge-pill"> {{ number_of_properties }}</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="{% url 'pinax_messages:inbox' %}"
            class="nav-link {% if url_name == 'pinax_messages:inbox' %}active{% endif %}"
          >
            <i class="fas fa-envelope fa-lg" />
            <span class="ml-3">Messages</span>
            <span class="badge badge-danger badge-pill"> {{ unread_thread_count }}</span>
          </a>
        </li>
        {# IDEA: if user is advertisor, see stage-2 #}
        {% if request.user.is_active and request.user.is_staff %}
        <li class="horizontal_line d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          Advertising
        </li>
        <li class="nav-item">
          <a
            href="{% url 'userMng:my_property_ads' %}"
            class="nav-link {% if url_name == 'userMng:my_property_ads' %}active{% endif %}"
          >
            <i class="fas fa-ad fa-lg" />
            <span class="ml-3">My property ads</span>
          </a>
        </li>
        <li class="nav-item">
          <a
            href="{% url 'userMng:ad_statistics' %}"
            class="nav-link {% if url_name == 'userMng:ad_statistics' %}active{% endif %}"
          >
            <i class="fas fa-signal fa-lg" />
            <span class="ml-3">Statistics</span>
          </a>
        </li>
        {% endif %}
      </ul>
    </aside>

    <div class="row d-block d-xs-block d-sm-block d-md-none">
      <ul class="d-flex flex-row list-group flex-wrap">
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="/administrace"
            class="nav-link {% if url_name == 'userMng:userMng_index' %}active{% endif %}"
          >
            <i class="fas fa-home fa-lg" />
          </a>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="/administrace/profile"
            class="nav-link {% if url_name == 'userMng:user_profile' %}active{% endif %}"
          >
            <i class="fas fa-user fa-lg" />
          </a>
        </li>
        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="/administrace/properties"
            class="nav-link {% if url_name == 'userMng:user_properties' %}active{% endif %}"
          >
            <i class="fas fa-hotel fa-lg" />
            <span class="badge badge-success badge-pill"> {{ number_of_properties }}</span>
          </a>
        </li>

        <li class="list-group-item d-flex justify-content-between align-items-center">
          <a
            href="{% url 'pinax_messages:inbox' %}"
            class="nav-link {% if url_name == 'pinax_messages:inbox' %}active{% endif %}"
          >
            <i class="fas fa-envelope fa-lg" />
            <span class="badge badge-danger badge-pill"> {{ unread_thread_count }}</span>
          </a>
        </li>
        {% if request.user.is_active and request.user.is_staff %}
        <li class="list-group-item justify-content-between align-items-center">
          <a
            href="{% url 'userMng:my_property_ads' %}"
            class="nav-link {% if url_name == 'userMng:my_property_ads' %}active{% endif %}"
          >
            <i class="fas fa-ad fa-lg" />
          </a>
        </li>
        <li class="list-group-item justify-content-between align-items-center">
          <a
            href="{% url 'userMng:ad_statistics' %}"
            class="nav-link {% if url_name == 'userMng:ad_statistics' %}active{% endif %}"
          >
            <i class="fas fa-signal fa-lg" />
          </a>
        </li>
        {% endif %}
      </ul>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TheHeader from "@/components/TheHeader.vue"; // @ is an alias to /src
import TheFooter from "@/components/TheFooter.vue";

export default Vue.extend({
  name: "ProfileNav",
  components: {
    TheHeader,
    TheFooter,
  }
});
</script>


