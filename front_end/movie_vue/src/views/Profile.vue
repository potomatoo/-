<template>
  <div class="mx-auto" id="profile">
    
    <v-container>
      <h2>{{ username }}님의 추천 영화</h2>
      <v-row
        justify="center"
      >
        <WeatherRecommend></WeatherRecommend>
        <hr style="color: black; width: 100%" >
        <WorldcupRecommend></WorldcupRecommend>
      </v-row>
    </v-container>
    
    
  </div>
</template>

<script>
// import Timeline from '../components/Timeline'
// import ReviewList from '../components/ReviewList'
import WeatherRecommend from '../components/WeatherRecommend'
import WorldcupRecommend from '../components/WorldcupRecommend'
// import jwtDecode from 'jwt-decode'
import { mapGetters } from 'vuex';
import router from '../router';
// import axios from 'axios'

// const SERVER_URL = 'http://localhost:8000'
export default {
  name: "profile",
  
  data () {
    return {
      inset: false,
      username: null,
      my_reviews: [],
      my_movies: [],
      reviews_info: [],
      recommends: [],
    }
  },
  components: {
    WeatherRecommend,
    WorldcupRecommend,
    // ReviewList,
  },
  methods: {
    getInfo() {
      this.username = sessionStorage.getItem('username')
      
    }
  
  }, 
  computed: {
    ...mapGetters(['isLoggedIn']),
  },
  created () {
    if (this.isLoggedIn) {
      this.getInfo()
    } else{
      router.push('/login')
    }
  }
  
};
</script>

<style>
</style>