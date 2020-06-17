<template>
  <v-card>
    <h1 class="pt-3 d-flex justify-content-center">사용자 권한 수정</h1>
    <v-container fluid>
      <v-row v-for="user in this.users" :key="user.id">
        <v-col cols="12" sm="4" md="4">
          <v-checkbox
            v-model="user.is_staff"
            :label="`${user.username}: ${user.is_staff.toString()}`"
            color="red"
            hide-details
          ></v-checkbox>
        </v-col>
      </v-row>
      <v-btn color="secondary" class="small" @click="save()">변경사항 저장</v-btn>
    </v-container>
  </v-card>
</template>

<script>
import axios from "axios";

export default {
  name: "UserList",
  data() {
    return {
      selected: [],
      users: []
    };
  },
  methods: {
    getUserList() {
      const SERVER_URL = "http://localhost:8000";
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(`${SERVER_URL}/api/v1/userList/`, options)
        .then(res => {
          console.log(res);
          this.users = res.data;
        })
        .catch(err => {
          console.error(err);
        });
    },

    save() {
      const SERVER_URL = "http://localhost:8000";
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      this.users.forEach(user => {
        const data = {
          username: user.username,
          is_staff: user.is_staff
        };
        axios
          .post(`${SERVER_URL}/api/v1/${user.id}/user_update/`, data, options)
          .then(res => {
            console.log(res.data);
          });
      });
    }
  },
  created() {
    this.getUserList();
  }
};
</script>

<style>
</style>