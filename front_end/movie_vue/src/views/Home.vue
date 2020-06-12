<template>
  <div class="text-center">
    <MovieList :movies="movies" />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from "@/components/MovieList.vue";
import axios from 'axios'

const SERVER_URL = "http://localhost:8000";

export default {
  name: "Home",

  data() {
    return {
      movies: []
    };
  },

  components: {
    MovieList
  },

  methods: {
    addMovies() {
      const token = sessionStorage.getItem("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };

      axios.get(`${SERVER_URL}/api/v1/movie/`, options)
        .then(res => {
          console.log(res)
          this.movies = res.data;
        })
        .catch(error => {
          console.log(error.response);
        });
    },

  },
  
  created() {
    this.addMovies()
  }

};
</script>
