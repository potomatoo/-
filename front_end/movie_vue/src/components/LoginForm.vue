<template>
  <div id="login-form" class="mx-auto">
    <div class="text-center">
      <h1>Log in</h1>
    </div>

    <form class="login-input" @submit.prevent="login(userData)">
      <div v-if="getErrors.length" class="error-list alert alert-danger">
        <ul>
          <li v-for="(error, idx) in getErrors" :key="idx">{{ error }}</li>
        </ul>
      </div>

      <div class="form-group">
        <v-text-field v-model="userData.username" label="Username" name="Username" required></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field v-model="userData.password1" label="Password" name="Password" type="password" required></v-text-field>
      </div>
      <div>
        <button>Login</button>
      </div>
    </form>
  </div>
</template>


<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "LoginForm",
  data() {
    return {
      userData: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    ...mapActions(["login"])
  },
  computed: {
    ...mapGetters(["getErrors"])
  }
};
</script>

<style>
</style>