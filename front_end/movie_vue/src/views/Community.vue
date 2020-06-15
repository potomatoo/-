<template>
  <v-row align="center" justify="center">
    <v-col cols="10">
      <ReviewList :reviews="reviews" />
    </v-col>
  </v-row>
</template>

<script>
import ReviewList from "@/components/ReviewList.vue";
import axios from 'axios'

const SERVER_URL = "http://localhost:8000";

export default {
  name: "Community",

  data() {
    return {
      reviews: []
    };
  },

  components: {
    ReviewList
  },

  methods: {
    addReviews() {
        const token = sessionStorage.getItem("jwt");
        const options = {
            headers: {
            Authorization: "JWT " + token
            }
        };
        axios.get(`${SERVER_URL}/api/v1/review/`, options)
            .then(res => {
                this.reviews = res.data;
            })
                .catch(error => {
                console.log(error.response);
            });
        },
  },

  created() {
    this.addReviews()
  }
};
</script>

<style>
</style>