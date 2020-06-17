<template>
  <div class="mx-auto" id="profile">
    
    <v-container>
      <h2>{{ username }}님의 추천 영화</h2>
      <v-row>
        <hr style="color: black; width: 100%" >
        <h3 class="d-flex justify-content-start ml-4 mt-5">선호하는 장르의 영화입니다.</h3>
        <GenreRecommend class="d-flex justify-content-center"></GenreRecommend>
        <hr style="color: black; width: 100%" >
        <h3 class="d-flex justify-content-start ml-4 mt-5">현재 날씨와 어울리는 영화입니다.</h3>
        <WeatherRecommend></WeatherRecommend>
        <hr style="color: black; width: 100%" >
        <h3 class="d-flex justify-content-start ml-4 mt-5">나만의 배우가 출연한 영화입니다.</h3>
        <WorldcupRecommend></WorldcupRecommend>
      </v-row>
    </v-container>
    
    
  </div>
</template>

<script>
import WeatherRecommend from '../components/WeatherRecommend'
import WorldcupRecommend from '../components/WorldcupRecommend'
import GenreRecommend from '../components/GenreRecommend'
import { mapGetters } from 'vuex';
import router from '../router';

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
    GenreRecommend
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