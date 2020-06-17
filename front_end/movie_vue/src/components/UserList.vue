<template>
  <!-- <div>
      <div class="text-center">
      
      <h1 class="pt-3">사용자 정보</h1>
        <table class="table table-hover">				
            <tbody>
                <tr v-for="user in users" :key="user.id">						
                    <td>{{ user.username }}</td>
                    <td>
                        <input type="checkbox" id="checkbox" v-model="checked">
                        <label for="checkbox">{{ checked }}</label>                   
                    </td>						
                </tr>
            </tbody>
        </table>
      </div>
  </div>-->
  <v-container fluid>
    <h1 class="pt-3">사용자 권한 수정</h1>
    <p>{{ selected }}</p>
		<v-flex v-for="user in users" :key="user.id" xs6>
       <v-checkbox light  v-model="selected" label="user.username" value="admin"></v-checkbox>
		</v-flex>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "UserList",
  data() {
    return {
			selected: ["admin"],
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
          .get(`${SERVER_URL}/api/v1/userList`, options)
          .then(res => {
						console.log(res);
						this.users = res.data
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