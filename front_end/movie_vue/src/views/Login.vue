
<template>
  <v-row
  align="center"
  justify="center"
  >
    <v-col cols="6">
      <LoginForm />
    </v-col>
  </v-row>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
    name: "Login",
    components: {
        LoginForm,
    }
}
</script>

<style>

</style>