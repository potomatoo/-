<template>
  <div class="signup-form mx-auto">
    <div v-if="getErrors.length">
      <v-alert dense outlined type="error" v-for="(error, idx) in getErrors" :key="idx">{{ error }}</v-alert>
    </div>

    <h1>Sign up</h1>

    <form class="signup-input" @submit.prevent="signup(userInput)">
      <div class="form-group">
        <v-text-field
          v-model="userInput.username"
          label="Username"
          name="Username"
          prepend-icon="mdi-account"
          required
        ></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.email"
          label="Email"
          name="Email"
          prepend-icon="mdi-email"
          required
        ></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.password"
          label="Password"
          name="Password"
          prepend-icon="mdi-lock"
          type="password"
          required
        ></v-text-field>
      </div>

      <div class="form-group m-0">
        <v-text-field
          v-model="userInput.passwordConfirm"
          label="Password Confirmation"
          name="Password Confirmation"
          prepend-icon="mdi-lock"
          type="password"
          required
        ></v-text-field>
      </div>
      <div class="d-flex justify-content-end pr-2">
        <button>Sign up</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  name: "SignupForm",
  data() {
    return {
      userInput: {
        username: "",
        email: "",
        password: "",
        passwordConfirm: ""
      }
    };
  },
  methods: {
    ...mapActions(["signup"])
  },
  computed: {
    ...mapGetters(["getErrors"])
  }
};
</script>

<style>
.errMessage {
  list-style-type: none;
}
</style>