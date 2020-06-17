<template>
  <v-container fluid>
    <h1 class="pt-3 d-flex justify-content-center ">사용자 권한 수정</h1>
		<v-flex v-for="user in this.users" :key="user.id" xs6>
       <v-checkbox light v-model="user.is_staff" :label="`${user.username}: ${user.is_staff.toString()}`" ></v-checkbox>
		</v-flex>
		<v-btn color="secondary" class="small" @click="save()">	변경사항 저장</v-btn>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "UserList",
  data() {
    return {
			selected: [],
			users: [],
    };
	},
	methods: {
		getUserList() {
			const SERVER_URL = 'http://localhost:8000'
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
						this.users = res.data
						// this.users.forEach(user => {
						// 	if (user.is_staff) {
						// 		this.selected.push(user)
						// 	}
						// })
          })
          .catch(err => {
            console.error(err);
          });
		}
	},
	created() {
		this.getUserList()
	}
};
</script>

<style>
</style>