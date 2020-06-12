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
        <v-text-field
          v-model="userData.username"
          label="Username"
          name="Username"
          prepend-icon="mdi-account"
          required
        ></v-text-field>
      </div>

      <div class="form-group m-0">
        <v-text-field
          v-model="userData.password"
          label="Password"
          name="Password"
          prepend-icon="mdi-lock"
          type="password"
          required
        ></v-text-field>
      </div>
      <div class='d-flex justify-content-end'>
        <button class="pr-2">Login</button>
      </div>
    </form>

    <div class="pt-5 d-flex justify-content-between align-items-center">
      <p class="m-0">계정이 없으신가요?</p>
      <v-spacer></v-spacer>
      <v-btn text color="primary" href="/signup" class="p-0">회원가입</v-btn>
    </div>
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