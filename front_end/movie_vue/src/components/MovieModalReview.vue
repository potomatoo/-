<template>
  <v-card class="movie-review-modal" tile>
    <v-card-title>
      <span class="headline">리뷰 남기기</span>
    </v-card-title>

    <v-container fluid>
      <div class="text-center py-3">
        <h1>{{ movie.title }}</h1>
      </div>

      <div class="text-center">
        <v-rating
          readonly
          v-model="rating"
          color="orange"
          half-increments
          background-color="orange lighten-3"
          size="30"
        ></v-rating>
      </div>

      <v-row>
        <v-col cols="12">
          <v-text-field label="제목" v-model="title"></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-textarea label="내용" v-model="content"></v-textarea>
        </v-col>
        <v-col cols class="mt-3">
          <v-btn @click="createReview" @click.stop="closeReview">
            <v-icon>mdi-pencil</v-icon>작성하기
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";

export default {
  name: "MovieModalReview",

  data() {
    return {
      title: "",
      content: ""
    };
  },

  props: {
    movie: {
      type: Object,
      required: false
    },
    rating: {
      type: Number,
      required: false
    }
  },

  methods: {
    closeReview() {
        console.log('close')
      this.$emit("closeEvent", true);
    },

    createReview() {
      const token = sessionStorage.getItem("jwt");
      const user_id = jwtDecode(token).user_id;
      const reviewURL = `http://localhost:8000/api/v1/${this.movie.id}/review/create/`;
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      const data = {
        title: this.title,
        content: this.content,
        rank: this.rating,
        movie: this.movie.id,
        user: user_id
      };
      console.log(data);
      axios.post(reviewURL, data, options)
        .then(res => {
          console.log(res);
          this.$emit("reviewUpdateEvent", true);
        })
        .catch(err => {
          console.error(err)
        });
    }
  }
};
</script>

<style>
</style>