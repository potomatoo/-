<template>
  <div class="mx-auto" id="profile">
    
    <v-container>
      <h2>{{ username }}'s profile</h2>
      <v-row
        justify="center"
      >
        <WeatherRecommend></WeatherRecommend>
      </v-row>
    </v-container>
    
    
  </div>
</template>

<script>
// import Timeline from '../components/Timeline'
// import ReviewList from '../components/ReviewList'
// import RecommandList from '../components/RecommandList'
import WeatherRecommend from '../components/WeatherRecommend'
// import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex';
// import router from '../router';
// import axios from 'axios'

// const SERVER_URL = 'http://localhost:8000'
export default {
  name: "profile",
  
  data () {
    return {
      username: null,
      my_reviews: [],
      my_movies: [],
      reviews_info: [],
      reccomands: [],
    }
  },
  components: {
    WeatherRecommend
    // ReviewList,
  },
  methods: {
  
  }, 
  computed: {
    ...mapGetters(['isLoggedIn']),
  },
  created () {

  }
};
</script>

<style>
</style>