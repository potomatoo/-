<template>
  <v-row justify="center">
    <v-col cols="12">
      <UserList :users="users" />
    </v-col>
  </v-row>
</template>

<script>
import UserList from "@/components/UserList.vue";
import axios from 'axios'

const SERVER_URL = "http://localhost:8000";

export default {
  name: "AdminPoistion",

  data() {
    return {
      users: []
    };
  },

  components: {
    UserList
  },

  methods: {
    addUsers() {
        const token = sessionStorage.getItem("jwt");
        const options = {
            headers: {
            Authorization: "JWT " + token
            }
        };
        axios.get(`${SERVER_URL}/api/v1/userList/`, options)
            .then(res => {
                this.users = res.data;                
            })
                .catch(error => {
                console.log(error.response);
            });
        },
  },

  created() {
    this.addUsers()
  }
};
</script>

<style>
</style>