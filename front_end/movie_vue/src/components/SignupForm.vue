<template>
  <div class="signup-form mx-auto">
    <h1>Sign up</h1>

    <form class="signup-input" @submit.prevent="signup(userInput)">
      <div v-if="getErrors.length" class="error-list alert alert-danger font-weight-bold">
        <ul class="m-0 p-0">
          <li class="errMessage" v-for="(error, idx) in getErrors" :key="idx">{{ error }}</li>
        </ul>
      </div>
      <div class="form-group">
        <v-text-field v-model="userInput.username" label="Username" name="Username" required></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field v-model="userInput.email" label="Email" name="Email" required></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.password1"
          label="Password"
          name="Password1"
          type="password"
          required
        ></v-text-field>
      </div>

      <div class="form-group">
        <v-text-field
          v-model="userInput.password2"
          label="Password Confirmation"
          name="password2"
          type="password"
          required
        ></v-text-field>
      </div>

      <button>Sign up</button>
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
        email:"",
        password1: "",
        password2: ""
      }
    };
  },
  methods: {
    ...mapActions(["signup"])
  },
  computed: {
    ...mapGetters(["getErrors"])
  },
};
</script>

<style>
    .errMessage {
        list-style-type: none;
    }
</style>