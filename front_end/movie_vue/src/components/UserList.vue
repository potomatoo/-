<template>
  <div>
      <div class="text-center">
      <!-- <button :to="{ name: 'ArticleCreateView' }" type="button" class="btn btn-success btn-md" >글쓰기</button> -->
      <h1 class="pt-3">사용자 정보</h1>
        <table class="table table-hover">				
            <tbody>
                <tr v-for="user in users" :key="user.id">						
                    <td>{{ user.username }}</td>						
                </tr>
            </tbody>
        </table>
      </div>
  </div>
</template>

<script>
export default {
    name: "UserList",
    props: {
        users: {
            type: Array
        }
    },
}
</script>

<style>

</style>