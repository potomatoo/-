<template>
  <v-app id="inspire">

    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Movie</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped>
      <div class="pt-3">
        <v-list-item-title v-if="!isLoggedIn" class="text-center font-weight-bold">Please Log in</v-list-item-title>
        <v-list-item-title v-else class="text-center font-weight-bold"> {{username}}</v-list-item-title>
      </div>

      <v-list dense v-if="isLoggedIn">
        <v-list-item link to="/">
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Movie List</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="/community">
          <v-list-item-action>
            <v-icon>mdi-comment-text-multiple</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Community</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item link to="/profile">
          <v-list-item-action>
            <v-icon>mdi-movie-open</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Recommend</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click.prevent="logout">
          <v-list-item-action>
            <v-icon>mdi-alpha-l-box</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Log out</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-list-item dense v-if="isLoggedIn && username == 'admin'" link to="/AdminPosition">
        <v-list-item-action>
          <v-icon>mdi-cog</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Staff</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list dense v-if="!isLoggedIn">
        <v-list-item link to="login">
          <v-list-item-action>
            <v-icon>mdi-account-check</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Log in</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="signup">
          <v-list-item-action>
            <v-icon>mdi-account-plus</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Sign up</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-content class="row m-0">
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col>
            <router-view></router-view>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "App",
  methods: {
    ...mapActions(["login", "logout"]),

  },
  computed: {
    ...mapGetters(["isLoggedIn"])
  },
  props: {

  },

  data() {
    return {
      drawer: null,
      username: null,
    }
  },

  created() {
    this.$store.dispatch("initialLogin");
  },
  updated() {
    this.$store.commit('clearErrors')
    this.username = sessionStorage.getItem('username')
  }
};
</script>

<style>
</style>
